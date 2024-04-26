# -*- coding: utf-8 -*-
"""The New World Module of SerumSage(Serum Indices Interpretation)

Author: Lei Wang
Date: April 24, 2023
"""
__author__ = "王磊"
__copyright__ = "Copyright 2024 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import os
import sys

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from lic_man.lm_comm_lib import verify_license
from main_window import MainWindow
from utils.constants import PUBLIC_KEY_FP, SPLASH_IMG_FP, LICENSE_FP


def new_world():
    """The Main Function of SerumSage(Serum Indices Interpretation)
    Returns:
        None
    """

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # 显示Splash Screen
    splash_pix = QPixmap(SPLASH_IMG_FP)
    splash = QSplashScreen(splash_pix)
    splash.showMessage("正在启动...", Qt.AlignCenter | Qt.AlignBottom, Qt.white)
    splash.show()

    # 允许处理其他事件
    app.processEvents()

    # 延时以模拟启动过程
    QTimer.singleShot(4000, splash.close)

    # 检查许可证
    license_fp = LICENSE_FP
    # 检查许可证文件是否存在
    if not os.path.exists(license_fp):
        return False, "许可证文件不存在"

    public_key_fp = PUBLIC_KEY_FP
    # 检查公钥文件是否存在
    if not os.path.exists(public_key_fp):
        return False, "公钥文件不存在"

    success, msg, usr_name, expiry_date = verify_license(
        license_fp, "utf-8", public_key_fp)
    if not success:
        return False, msg

    # 初始化应用
    main_window_ui = MainWindow(usr_name=usr_name, expiry_date=expiry_date)
    main_window_ui.show()
    return True, app
