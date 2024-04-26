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

from PyQt5.QtCore import QObject, pyqtSignal, QVariant
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox

import ui_design.Ui_sys_cfg_dialog as SysCfgDialogUI
from utils.constants import CONFIG_FP, ICON_FP, INI_SYS_SECTION, SCAN_INTERVAL, TUBE_IMG_FOLDER, DETECT_OUTPUT_FOLDER, ENCODING, SCAN_INTERVAL_DEFAULT_VAL


class SysCfgDialog(QDialog, QObject):
    """The Class of System Configuration Dialog
    """

    config_updated = pyqtSignal(QVariant)

    def __init__(self, parent=None):
        super(SysCfgDialog, self).__init__(parent)
        QObject.__init__(self)

        self.ui = SysCfgDialogUI.Ui_sysCfgDlg()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(ICON_FP))

        self.ui.sysCfgDlgBtnBox.accepted.connect(self.ok_clicked)
        self.ui.sysCfgDlgBtnBox.rejected.connect(self.cancel_clicked)

        self.cfg_changed = False

        # read config
        self.config = configparser.ConfigParser()
        if os.path.exists(CONFIG_FP) is True:
            self.config.read(CONFIG_FP)
            self.scan_interval = self.config.getint(INI_SYS_SECTION, SCAN_INTERVAL)
            self.tube_img_folder = self.config.get(INI_SYS_SECTION, TUBE_IMG_FOLDER)
            self.detect_output_folder = self.config.get(
                INI_SYS_SECTION, DETECT_OUTPUT_FOLDER)

            self.ui.imgScanIntervalEdit.setText(str(self.scan_interval))
            self.ui.tubeImgFolderEdit.setText(self.tube_img_folder)
            self.ui.detectOutputFolderEdit.setText(self.detect_output_folder)
        else:
            self.scan_interval = SCAN_INTERVAL_DEFAULT_VAL
            self.tube_img_folder = ''
            self.detect_output_folder = ''

    def ok_clicked(self):
        """OK Button Clicked
        """
        scan_interval = self.ui.imgScanIntervalEdit.text()
        # self.scan_interval = self.ui.imgScanIntervalEdit.text()
        try:
            scan_interval = int(scan_interval)

            if scan_interval <= 0 or scan_interval > 12*60*60:
                raise ValueError("The Image Scan Interval input is incorrect")

        except Exception:
            QMessageBox.warning(self, "Warning", "图片文件扫描间隔需要输入正整数值且小于12小时.")
            self.close()
            return
        if scan_interval != self.scan_interval:
            self.scan_interval = scan_interval
            self.cfg_changed = True

        tube_img_folder = self.ui.tubeImgFolderEdit.text()
        if os.path.isdir(tube_img_folder) is False or os.path.exists(tube_img_folder) is False:
            QMessageBox.warning(self, "Warning", "血清试管图片文件夹不存在.")
            self.close()
            return
        if tube_img_folder != self.tube_img_folder:
            self.tube_img_folder = tube_img_folder
            self.cfg_changed = True

        detect_output_folder = self.ui.detectOutputFolderEdit.text()
        if os.path.isdir(detect_output_folder) is False or os.path.exists(detect_output_folder) is False:
            QMessageBox.warning(self, "Warning", "检测结果输出文件夹不存在.")
            self.close()
            return
        if detect_output_folder != self.detect_output_folder:
            self.detect_output_folder = detect_output_folder
            self.cfg_changed = True

        if self.cfg_changed is True:
            self.save_config()
            self.config_updated.emit([self.scan_interval, self.tube_img_folder, self.detect_output_folder])

        self.accept()

    def cancel_clicked(self):
        """Cancel Button Clicked
        """
        self.close()

    def save_config(self):
        """Save Configuration to file
        """
        self.config[INI_SYS_SECTION] = {
            SCAN_INTERVAL: self.scan_interval,
            TUBE_IMG_FOLDER: self.tube_img_folder,
            DETECT_OUTPUT_FOLDER: self.detect_output_folder
        }
        with open(CONFIG_FP, 'w', encoding=ENCODING) as cfg_f:
            self.config.write(cfg_f)
        return
