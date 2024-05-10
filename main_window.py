# -*- coding: utf-8 -*-
"""The Main Module of SerumSage(Serum Indices Interpretation)

Author: Lei Wang
Date: October 17, 2023
"""
__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import os
import configparser

from PyQt5.QtCore import QObject, QTimer, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QGraphicsScene, QFileDialog, QLabel, QInputDialog, QLineEdit

import ui_design.Ui_main_window as MainWindowUI
import sys_cfg_dialog as SysCfgDialog
from tube_img_folder_processor import TubeImgFolderProcessor
from HIL_predictor import HIL_predictor
from utils.utils import (
    get_files_with_extensions,
    convert_HIL_indices_to_class
)
from utils.chromo_cv_utils import cv_imread
from lic_man.lm_comm_lib import verify_admin_password
from logger import log
from utils.constants import CONFIG_FP, ICON_FP, TUBE_IMG_DIR_FP, DETECT_OUTPUT_DIR_FP, INI_SYS_SECTION, SCAN_INTERVAL, TUBE_IMG_FOLDER, DETECT_OUTPUT_FOLDER, OD_MODEL_FP, FORECAST_MODEL_FP, ENCODING, PUBLIC_KEY_FP, ADMIN_PWD_HASH_SIGN_FP, MASTER_PWD_HASH_SIGN_FP, SCAN_INTERVAL_DEFAULT_VAL


class MainWindow(QMainWindow, QObject):
    """Main Window of SerumSage
    """

    def __init__(self, usr_name="", expiry_date="", parent=None):
        log.info("SerumSage on Init.")

        super(MainWindow, self).__init__(parent)
        QObject.__init__(self)

        # user info and expiry date
        self.usr_name = usr_name
        self.expiry_date = expiry_date

        # setup main window ui
        self.main_window_ui = MainWindowUI.Ui_MainWindow()
        self.main_window_ui.setupUi(self)
        self.setWindowIcon(QIcon(ICON_FP))

        # setup about dialog
        self.main_window_ui.serumSegaAboutAction.triggered.connect(
            self.showAboutDialog)

        # setup tube image show for continue detection
        self.tube_scene_4cd = QGraphicsScene()
        self.tube_scene_4cd.setBackgroundBrush(Qt.white)
        self.pix_map_item_4cd = None
        self.main_window_ui.tubeImgGView4CD.setScene(self.tube_scene_4cd)
        self.main_window_ui.tubeImgGView4CD.show()

        # setup tube image show for single detection
        self.tube_scene_4sd = QGraphicsScene()
        self.tube_scene_4sd.setBackgroundBrush(Qt.white)
        self.pix_map_item_4sd = None
        self.main_window_ui.tubeImgGView4SD.setScene(self.tube_scene_4sd)
        self.main_window_ui.tubeImgGView4SD.show()

        # read config
        self.sys_cfg = configparser.ConfigParser()

        # check if config file exists, if no create one with default values
        if os.path.exists(CONFIG_FP) is False:
            self.sys_cfg.add_section(INI_SYS_SECTION)
            self.sys_cfg.set(INI_SYS_SECTION, SCAN_INTERVAL, str(SCAN_INTERVAL_DEFAULT_VAL))
            self.sys_cfg.set(INI_SYS_SECTION, TUBE_IMG_FOLDER, TUBE_IMG_DIR_FP)
            self.sys_cfg.set(INI_SYS_SECTION, DETECT_OUTPUT_FOLDER, DETECT_OUTPUT_DIR_FP)
            with open(CONFIG_FP, 'w', encoding=ENCODING) as cfg_f:
                self.sys_cfg.write(cfg_f)

            # 判断试管图片目录是否存在
            if not os.path.exists(TUBE_IMG_DIR_FP):
                os.makedirs(TUBE_IMG_DIR_FP)
            # 判断分析结果输出目录是否存在
            if not os.path.exists(DETECT_OUTPUT_DIR_FP):
                os.makedirs(DETECT_OUTPUT_DIR_FP)

            # 设置系统配置
            self.scan_interval = SCAN_INTERVAL_DEFAULT_VAL
            self.tube_img_folder = TUBE_IMG_DIR_FP
            self.detect_output_folder = DETECT_OUTPUT_DIR_FP
        else:
            self.sys_cfg.read(CONFIG_FP)
            self.scan_interval = self.sys_cfg.getint(INI_SYS_SECTION, SCAN_INTERVAL)
            self.tube_img_folder = self.sys_cfg.get(INI_SYS_SECTION, TUBE_IMG_FOLDER)
            self.detect_output_folder = self.sys_cfg.get(INI_SYS_SECTION, DETECT_OUTPUT_FOLDER)

        # setup system config dialog
        # 系统配置对话框的初始化依赖于系统配置文件的读取
        # 所以在系统配置对话框初始化之前，需要先确保系统配置文件可以被读取
        self.sys_cfg_dlg = SysCfgDialog.SysCfgDialog(self)
        self.sys_cfg_dlg.config_updated.connect(self.sysCfgUpdated)
        self.main_window_ui.sysCfgAction.triggered.connect(
            self.onSysCfgActionMenuTriggered)

        # setup timer for image scan
        self.img_scan_timer = QTimer(self)
        self.img_scan_timer.setInterval(self.scan_interval * 1000)
        self.img_scan_timer.timeout.connect(self.imgScanTimerTimeout)

        # setup scan state
        self.on_img_scan = False

        # image file extensions
        self.img_file_exts = ['jpg', 'png', 'jpeg', 'JPG', 'bmp']

        # Init HIL Predictor
        self.HIL_predictor = HIL_predictor(
            OD_MODEL_FP, FORECAST_MODEL_FP)
        # self.HIL_predictor = HIL_predictor(
        #     './pytorch_yolov5/checkpoints/best.pt', './pytorch_LogicRegression/checkpoints/LHI-model-use.pt')
        log.info("HIL Predictor initialized.")

        # Init Image folder processor
        self.tube_img_folder_processor = TubeImgFolderProcessor(
            self.HIL_predictor, self.tube_img_folder, self.img_file_exts, self.detect_output_folder)
        self.tube_img_folder_processor.imgProcessed.connect(
            self.showTubeImgAndHIL4CD)
        self.tube_img_folder_processor.allImgProcessed.connect(
            self.allImgProcessed)

        # handle main tab changed
        self.main_window_ui.workModeTab.currentChanged.connect(
            self.mainWorkTabChanged)

        # handle open file dialog
        self.main_window_ui.selectTubeImgBtn.clicked.connect(
            self.openFileNameDialog)

        # resize event
        self.resizeEvent = self.onResize

        # If the 1st Tab is activated, then start image scan timer
        if self.main_window_ui.workModeTab.currentIndex() == 0:
            self.img_scan_timer.start()

        # Result Browser Tab
        # setup detection output folder
        self.main_window_ui.outputFolderPathEdit.setText(
            self.detect_output_folder)
        # fill image file name into list
        if os.path.exists(self.detect_output_folder):
            img_fps = get_files_with_extensions(
                self.detect_output_folder, self.img_file_exts)
            for img_fp in img_fps:
                img_basename = os.path.basename(img_fp)
                self.main_window_ui.outputFileList.addItem(img_basename)

        # set Graphic view for result browse
        self.tube_scene_4rb = QGraphicsScene()
        self.tube_scene_4rb.setBackgroundBrush(Qt.white)
        self.pix_map_item_4rb = None
        self.main_window_ui.tubeImgGView4RB.setScene(self.tube_scene_4rb)
        self.main_window_ui.tubeImgGView4RB.show()
        # connect item selection changed signal
        self.main_window_ui.outputFileList.itemSelectionChanged.connect(
            self.showTubeImgAndHIL4RB)

        # setup status bar
        self.status_bar = self.statusBar()
        self.status_bar.setSizeGripEnabled(True)

        self.work_mode_label = QLabel()
        self.work_mode_label.setFrameStyle(QLabel.StyledPanel | QLabel.Sunken)
        self.status_bar.addPermanentWidget(self.work_mode_label)

        self.status_report_label = QLabel()
        self.status_report_label.setFrameStyle(
            QLabel.StyledPanel | QLabel.Sunken)
        self.status_bar.addPermanentWidget(self.status_report_label, 1)

        self.work_mode_label.setText("工作模式:连续分析")
        self.status_report_label.setText("状态:正常")

        log.info("SerumSage started.")

    def onSysCfgActionMenuTriggered(self):
        """当系统配置菜单被触发时进行的操作
        """

        pub_key_fp = PUBLIC_KEY_FP
        # 判断public key是否存在
        if not os.path.exists(pub_key_fp):
            QMessageBox.critical(self, "公钥文件不存在", "公钥文件不存在")
            return

        admin_pwd_hash_sign_fp = ADMIN_PWD_HASH_SIGN_FP
        # 判断管理员密码hash签名文件是否存在
        if not os.path.exists(admin_pwd_hash_sign_fp):
            QMessageBox.critical(self, "管理员密码hash签名文件不存在", "管理员密码hash签名文件不存在")
            return

        master_pwd_hash_sign_fp = MASTER_PWD_HASH_SIGN_FP
        # 判断主密码hash签名文件是否存在
        if not os.path.exists(master_pwd_hash_sign_fp):
            QMessageBox.critical(self, "主密码hash签名文件不存在", "主密码hash签名文件不存在")
            return

        # 弹出管理员密码输入对话框
        password, ok = QInputDialog.getText(self, "管理员验证", "请输入管理员密码：", QLineEdit.Password)

        passed, return_msg = verify_admin_password(pub_key_fp, admin_pwd_hash_sign_fp, master_pwd_hash_sign_fp, password)

        if ok and passed:
            self.sys_cfg_dlg.show()
            log.info("SysConfig Dialog Showed.")
        elif ok:
            log.info("Password Verification Failed, before enter SysConfig.")
            QMessageBox.critical(self, "密码验证失败", return_msg)

    def sysCfgUpdated(self, updated_cfg):
        """系统配置更新
        """
        self.scan_interval = updated_cfg[0]
        self.tube_img_folder = updated_cfg[1]
        self.detect_output_folder = updated_cfg[2]

        self.img_scan_timer.setInterval(self.scan_interval * 1000)

        # update tube image folder processor
        self.tube_img_folder_processor.setTubeImgAndOutputFolder(
            self.tube_img_folder, self.detect_output_folder)

        # update Result Browser Tab
        # update output folder path in result browser
        self.main_window_ui.outputFolderPathEdit.setText(
            self.detect_output_folder)
        # update file list in result browser
        self.main_window_ui.outputFileList.clear()
        if os.path.exists(self.detect_output_folder):
            img_fps = get_files_with_extensions(
                self.detect_output_folder, self.img_file_exts)
            for img_fp in img_fps:
                img_basename = os.path.basename(img_fp)
                self.main_window_ui.outputFileList.addItem(img_basename)

        log.info("System Config Updated.")


    def showTubeImgAndHIL4RB(self):
        """show tube image and HIL indices for result browser
        """
        selected_item = self.main_window_ui.outputFileList.currentItem()
        if selected_item is not None:
            fn = selected_item.text()
            img_fp = os.path.join(self.detect_output_folder, fn)
            pixmap = QPixmap(img_fp)
            if self.pix_map_item_4rb is None:
                self.pix_map_item_4rb = self.tube_scene_4rb.addPixmap(pixmap)
            else:
                self.pix_map_item_4rb.setPixmap(pixmap)
            # read HIL indices from file
            text_fp = f'{os.path.splitext(img_fp)[0]}.txt'
            if os.path.exists(text_fp):
                self.getHILInfoFromFileAndShow(text_fp)

    def getHILInfoFromFileAndShow(self, text_fp):
        """get HIL indices from file and show them
        """
        with open(text_fp, 'r', encoding=ENCODING) as f:
            lines = f.readlines()
            HIL = {}
            for line in lines:
                if line.startswith('H:'):
                    HIL['H'] = int(line[2:])
                elif line.startswith('I:'):
                    HIL['I'] = int(line[2:])
                elif line.startswith('L:'):
                    HIL['L'] = int(line[2:])
                elif line.startswith('5078:'):
                    H_sqr = line[5:]
                elif line.startswith('5079:'):
                    I_sqr = line[5:]
                elif line.startswith('5080:'):
                    L_sqr = line[5:]
        # show HIL indices
        self.main_window_ui.HIndicesLCD4RB.display(HIL['H'])
        self.main_window_ui.IIndicesLCD4RB.display(HIL['I'])
        self.main_window_ui.LIndicesLCD4RB.display(HIL['L'])
        # show HIL classes
        self.main_window_ui.HClassEdit4RB.setText(H_sqr)
        self.main_window_ui.IClassEdit4RB.setText(I_sqr)
        self.main_window_ui.LClassEdit4RB.setText(L_sqr)

    def showAboutDialog(self):
        """show about dialog
        """
        about = QMessageBox()
        about.setWindowTitle("关于-SerumSage")
        about.setWindowIcon(QIcon(ICON_FP))
        about.setText("血清指数分析软件-SerumSage")
        about.setInformativeText(
            f"授权用户: {self.usr_name}\n使用许可到期时间: {self.expiry_date[:10]}\n\n四川科莫生医疗科技有限公司.\n版本号:1.0.0\nCopyright © 2024 Kemoshen Medical Tech. Co., Ltd. All rights reserved.")
        # about.setInformativeText(
        #     f"授权用户: {self.usr_name}\n使用许可到期时间: {self.expiry_date[:10]}\n\n四川大学华西医院.\n版本号:1.0.0\nCopyright © 2024 WEST CHINA HOSPITAL SICHUAN UNIVERSITY. All rights reserved.")
        kmsIcon = QPixmap(ICON_FP)
        about.setIconPixmap(kmsIcon)
        about.exec_()

    def showTubeImgAndHIL4CD(self, img_fp, H_indices, I_indices, L_indices, H_sqr, I_sqr, L_sqr):
        """show tube image and HIL indices for continue detection
        """
        # show tube image
        pixmap = QPixmap(img_fp)
        if self.pix_map_item_4cd is None:
            self.pix_map_item_4cd = self.tube_scene_4cd.addPixmap(pixmap)
        else:
            self.pix_map_item_4cd.setPixmap(pixmap)
        # show HIL indices
        self.main_window_ui.HIndicesLCD4CD.display(H_indices)
        self.main_window_ui.IIndicesLCD4CD.display(I_indices)
        self.main_window_ui.LIndicesLCD4CD.display(L_indices)
        # show HIL classes
        self.main_window_ui.HClassEdit4CD.setText(H_sqr)
        self.main_window_ui.IClassEdit4CD.setText(I_sqr)
        self.main_window_ui.LClassEdit4CD.setText(L_sqr)
        # add new processed image to file list in result browser
        self.main_window_ui.outputFileList.addItem(os.path.basename(img_fp))
        log.info(
            f"Continue Detection: image_file: {img_fp} H:{H_indices} I:{I_indices} L:{L_indices} H_sqr:{H_sqr} I_sqr:{I_sqr} L_sqr:{L_sqr}")

    def allImgProcessed(self, processed_img_cnt):
        """All tube images processed
        """
        # Image Scan Completed, Set Image Scan State to False
        self.on_img_scan = False
        self.status_report_label.setText("状态:试管图片扫描结束")
        if processed_img_cnt > 0:
            log.info(f"All Tube Images in {self.tube_img_folder} Processed, Total: {processed_img_cnt}")

    def imgScanTimerTimeout(self):
        """Image Scan Timer Timeout
        """
        if self.on_img_scan is True:
            log.info(
                "imgScanTimerTimeout: Last Image Scan is not completed, Wait for next round.")
            return

        # Set Image Scan state
        self.on_img_scan = True

        # setup tube image folder processor
        self.tube_img_folder_processor.start()
        # log.info("Image Scan Timer Timeout, Start Image Scan.")
        self.status_report_label.setText("状态:开始试管图片扫描")

    def mainWorkTabChanged(self, index):
        """Main Window Tab Changed
        """
        if index == 0:
            if self.img_scan_timer.isActive() is False:
                self.img_scan_timer.start()
            self.work_mode_label.setText("工作模式: 连续分析")
            self.status_report_label.setText("状态: 正常")
            log.info("Work Mode Change to Continue Detection.")
        else:
            self.img_scan_timer.stop()
            if index == 1:
                self.work_mode_label.setText("工作模式: 单张分析")
                self.status_report_label.setText("状态: 正常")
                log.info("Work Mode Change to Single Detection.")
            elif index == 2:
                self.work_mode_label.setText("工作模式: 结果浏览")
                self.status_report_label.setText("状态: 正常")
                log.info("Work Mode Change to Result Browser.")

    def onResize(self, event):
        """Main Window Resize
        """
        font_size = self.main_window_ui.HClassEdit4CD.height() // 2
        font = self.main_window_ui.HClassEdit4CD.font()
        font.setPointSize(font_size)

        self.main_window_ui.HClassEdit4CD.setFont(font)
        self.main_window_ui.IClassEdit4CD.setFont(font)
        self.main_window_ui.LClassEdit4CD.setFont(font)

    def openFileNameDialog(self):
        """open file dialog to select tube image
        """
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "选择血清试管图片", "", "血清试管图片文件 (*.jpg);;所有文件 (*)", options=options)
        if fileName:
            self.main_window_ui.tubeImgFullPathEdit.setText(fileName)
            # show tube image
            pixmap = QPixmap(fileName)
            if self.pix_map_item_4sd is None:
                self.pix_map_item_4sd = self.tube_scene_4sd.addPixmap(pixmap)
            else:
                self.pix_map_item_4sd.setPixmap(pixmap)
            # predict HIL indices
            img = cv_imread(fileName)
            HIL = self.HIL_predictor.dealImage(img)
            H_sqr, I_sqr, L_sqr = convert_HIL_indices_to_class(HIL)
            # show HIL indices
            self.main_window_ui.HIndicesLCD4SD.display(HIL['H'])
            self.main_window_ui.IIndicesLCD4SD.display(HIL['I'])
            self.main_window_ui.LIndicesLCD4SD.display(HIL['L'])
            # show HIL classes
            self.main_window_ui.HClassEdit4SD.setText(H_sqr)
            self.main_window_ui.IClassEdit4SD.setText(I_sqr)
            self.main_window_ui.LClassEdit4SD.setText(L_sqr)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     app.setStyle("Fusion")

#     # 显示Splash Screen
#     splash_pix = QPixmap(SPLASH_IMG_FP)
#     splash = QSplashScreen(splash_pix)
#     splash.showMessage("正在启动...", Qt.AlignCenter | Qt.AlignBottom, Qt.white)
#     splash.show()

#     # 允许处理其他事件
#     app.processEvents()

#     # 延时以模拟启动过程
#     QTimer.singleShot(2000, splash.close)

#     # 检查许可证
#     result, msg, usr_name, expiry_date = verify_license(LICENSE_FP, "utf-8", PUBLIC_KEY_FP)
#     if not result:
#         log.error(msg)
#         QMessageBox.critical(None, "许可证验证失败", "\n\n  许可证验证失败:      \n\n" + msg + "    \n")
#         sys.exit(1)
#         # sys.exit(app.exec_())

#     main_window_ui = MainWindow(usr_name=usr_name, expiry_date=expiry_date)
#     # main_window_ui.showMaximized()
#     main_window_ui.show()
#     sys.exit(app.exec_())
