# coding=utf-8
"""The Main Module of SerumSage System Config parameters setting
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
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox
import ui_design.Ui_sys_cfg_dialog as SysCfgDialogUI


class SysCfgDialog(QDialog, QObject):
    def __init__(self, parent=None):
        super(SysCfgDialog, self).__init__(parent)
        QObject.__init__(self)

        self.ui = SysCfgDialogUI.Ui_sysCfgDlg()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('./ui_img/icon_kemoshen.png'))

        self.ui.sysCfgDlgBtnBox.accepted.connect(self.ok_clicked)
        self.ui.sysCfgDlgBtnBox.rejected.connect(self.cancel_clicked)

        self.cfg_changed = False

        # read config
        self.config = configparser.ConfigParser()
        if os.path.exists('./cfg.ini') is True:
            self.config.read('./cfg.ini')
            self.scan_interval = self.config.getint('SYS', 'scan_interval')
            self.tube_img_folder = self.config.get('SYS', 'tube_img_folder')
            self.detect_output_folder = self.config.get(
                'SYS', 'detect_output_folder')

            self.ui.imgScanIntervalEdit.setText(str(self.scan_interval))
            self.ui.tubeImgFolderEdit.setText(self.tube_img_folder)
            self.ui.detectOutputFolderEdit.setText(self.detect_output_folder)

    def ok_clicked(self):
        self.scan_interval = self.ui.imgScanIntervalEdit.text()
        try:
            self.scan_interval = int(self.scan_interval)

            if self.scan_interval <= 0 or self.scan_interval > 12*60*60:
                raise ValueError("The Image Scan Interval input is incorrect")

        except Exception:
            QMessageBox.warning(self, "Warning", "图片文件扫描间隔需要输入大于零的正整数值.")
            return

        self.tube_img_folder = self.ui.tubeImgFolderEdit.text()
        if os.path.isdir(self.tube_img_folder) is False or os.path.exists(self.tube_img_folder) is False:
            QMessageBox.warning(self, "Warning", "血清试管图片文件夹不存在.")
            return

        self.detect_output_folder = self.ui.detectOutputFolderEdit.text()
        if os.path.isdir(self.detect_output_folder) is False or os.path.exists(self.detect_output_folder) is False:
            QMessageBox.warning(self, "Warning", "检测结果输出文件夹不存在.")
            return

        self.save_config()

        self.cfg_changed = True

        self.close()

    def cancel_clicked(self):
        self.close()

    def save_config(self):
        self.config['SYS'] = {
            'scan_interval': self.scan_interval,
            'tube_img_folder': self.tube_img_folder,
            'detect_output_folder': self.detect_output_folder
        }
        with open('./cfg.ini', 'w', encoding='utf-8') as cfg_f:
            self.config.write(cfg_f)
        return
