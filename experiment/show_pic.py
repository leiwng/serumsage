"""The Main GUI of SerumSage(Serum Indices Interpretation)
"""
__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import os
import sys
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from experiment.Ui_show_pic import Ui_MainWindow


def get_files_with_extensions(folder_path, extensions):
    """Get file paths with specific extensions in a folder

    Args:
        folder_path (String): File folder path, e.g. TUBE_IMG_DIR_FP, the folder must be exist
        extensions (List of String): List of File extensions, e.g. ['jpg', 'png', 'jpeg', 'JPG','bmp']

    Returns:
        List of String: List of file paths, e.g. ['./test/tube_img/1.jpg', './test/tube_img/2.jpg']
    """
    files = []
    for fn in os.listdir(folder_path):
        files.extend(os.path.join(folder_path, fn) for ext in extensions if fn.endswith(ext))
    return files


class MainWindow(QMainWindow, QObject):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QObject.__init__(self)

        # setup main window ui
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

        # setup pic view
        self.tubeImgScene = QGraphicsScene()
        self.tubeImgScene.setBackgroundBrush(Qt.white)
        self.main_window.tubeImgGView.setScene(self.tubeImgScene)
        self.main_window.tubeImgGView.show()

    def show_tube_img(self, img_folder, img_exts):
        img_fps = get_files_with_extensions(img_folder, img_exts)
        for img_fp in img_fps:
            img = QPixmap(img_fp)
            self.tubeImgScene.addPixmap(img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = MainWindow()
    # main_window.showMaximized()
    main_window.show()
    main_window.show_tube_img('../test/tube_img', ['jpg', 'png', 'jpeg', 'JPG', 'bmp'])
    sys.exit(app.exec_())
