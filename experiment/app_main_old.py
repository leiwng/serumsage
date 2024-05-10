"""The Main GUI of SerumSage(Serum Indices Interpretation)
"""
__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTabWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QTextEdit, QListView, QWidget, QMessageBox, QDialog, QFormLayout, QLineEdit, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGroupBox
from PyQt5.QtGui import QIcon, QPixmap, QImage
from AnimatedToggle import AnimatedToggle
from utils.constants import ICON_FP


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = '血清指数分析软件-SerumSage'
        self.initUI()

    def initUI(self):
        ###
        ### Main Window
        ###
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('./ui_img/icon_MainWindow.png'))
        self.resize(1024, 768)

        ###
        ### Menu bar
        ###
        menubar = self.menuBar()

        configAction = QAction(QIcon('./ui_img/icon_config.png'), '系统设置', self)
        configAction.triggered.connect(self.showConfigDialog)

        aboutAction = QAction(QIcon('./ui_img/icon_about.png'), '关于系统', self)
        aboutAction.triggered.connect(self.showAboutDialog)

        menubar.addAction(configAction)
        menubar.addAction(aboutAction)

        ###
        ### Status bar
        ###
        self.statusBar().showMessage(' 连续分析 | 就绪 ')

        ###
        ### Central widget
        ###

        # Tab widget
        self.tab_widget = QTabWidget(self)
        # 将MainWindow的中心部件设置为tab_widget
        self.setCentralWidget(self.tab_widget)

        # Tabs
        self.tab4CW = QWidget()
        self.tab4CW = QWidget()
        self.tab4RB = QWidget()

        # Add tabs
        self.tab_widget.addTab(self.tab4CW, "连续分析")
        self.tab_widget.addTab(self.tab4CW, "单次分析")
        self.tab_widget.addTab(self.tab4RB, "结果浏览")

        # Add widgets to tabs


        # Tab 1
        gLayout = QGridLayout(self)

        # start switch
        self.startSwitch = AnimatedToggle()

        # serum picture zone
        scene = QGraphicsScene()
        self.continue_pic_viewer = QGraphicsView(scene)
        image = QImage("./ui_img/blood_test_tube.jpg")
        pixmap = QPixmap.fromImage(image)
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.continue_pic_viewer.show()

        # serum Indices result zone
        self.result_from = QFormLayout()
        self.result_from.addRow("", )

        gLayout.addWidget(self.startSwitch)
        self.tab4CW.setLayout(gLayout)

        # Tab 2
        vLayout2 = QVBoxLayout(self)
        selectFileButton = QPushButton("选择血清试管图片")
        selectFileButton.clicked.connect(self.openFileNameDialog)
        vLayout2.addWidget(selectFileButton)
        self.fileNameTextEdit = QTextEdit()
        vLayout2.addWidget(self.fileNameTextEdit)
        self.tab4CW.setLayout(vLayout2)

        # Tab 3
        vLayout3 = QVBoxLayout(self)
        self.fileListView = QListView()
        vLayout3.addWidget(self.fileListView)
        self.tab4RB.setLayout(vLayout3)

    def showAboutDialog(self):
        # TODO: Implement the function to show About dialog
        about = QMessageBox()
        about.setWindowTitle("About")
        about.setText("血清指数分析软件-SerumSage")
        about.setInformativeText("四川科莫生医疗科技有限公司.\nCopyright © 2024 Kemoshen Medical Tech. Co., Ltd. All rights reserved.")
        # about.setInformativeText("四川大学华西医院.\nCopyright © 2024 WEST CHINA HOSPITAL SICHUAN UNIVERSITY. All rights reserved.")
        kmsIcon = QPixmap(ICON_FP)
        about.setIconPixmap(kmsIcon)
        about.exec_()

    def showConfigDialog(self):
        # TODO: Implement the function to show Config dialog
        configDialog = ConfigDialog(self)
        if configDialog.exec_() == QDialog.Accepted:
            self.inputFolderPath = configDialog.inputFolderLineEdit.text()
            self.outputFolderPath = configDialog.outputFolderLineEdit.text()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"选择血清试管图片", "","血清试管图片文件 (*.jpg);;所有文件 (*)", options=options)
        if fileName:
            self.fileNameTextEdit.setText(fileName)

class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("系统配置")
        self.initUI()

    def initUI(self):
        layout = QFormLayout(self)

        # Input folder selection button
        inputFolderButton = QPushButton("选择血清试管图片文件夹")
        inputFolderButton.clicked.connect(self.selectInputFolder)
        self.inputFolderLineEdit = QLineEdit()
        layout.addRow("血清试管图片文件夹:", self.inputFolderLineEdit)
        layout.addWidget(inputFolderButton)

        # Output folder selection button
        outputFolderButton = QPushButton("选择分析结果输出文件夹")
        outputFolderButton.clicked.connect(self.selectOutputFolder)
        self.outputFolderLineEdit = QLineEdit()
        layout.addRow("分析结果输出文件夹:", self.outputFolderLineEdit)
        layout.addWidget(outputFolderButton)

        # OK and Cancel buttons
        buttonsLayout = QHBoxLayout()
        okButton = QPushButton("确定")
        okButton.clicked.connect(self.accept)
        cancelButton = QPushButton("取消")
        cancelButton.clicked.connect(self.reject)
        buttonsLayout.addWidget(okButton)
        buttonsLayout.addWidget(cancelButton)
        layout.addRow(buttonsLayout)

    def selectInputFolder(self):
        options = QFileDialog.Options()
        if folderName := QFileDialog.getExistingDirectory(
            self, "选择血清试管图片文件夹", options=options
        ):
            self.inputFolderLineEdit.setText(folderName)

    def selectOutputFolder(self):
        options = QFileDialog.Options()
        if folderName := QFileDialog.getExistingDirectory(
            self, "选择分析结果输出文件夹", options=options
        ):
            self.outputFolderLineEdit.setText(folderName)


class ContinueWorkTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # start switch
        self.startSwitch = AnimatedToggle()

        # serum picture zone
        scene = QGraphicsScene()
        self.continue_pic_viewer = QGraphicsView(scene)
        image = QImage("./ui_img/blood_test_tube.jpg")
        pixmap = QPixmap.fromImage(image)
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.continue_pic_viewer.show()

        # serum Indices result zone
        self.result_from = QFormLayout()
        self.result_from.addRow("", )

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.startSwitch)
        self.layout.addWidget(self.continue_pic_viewer)
        self.layout.addLayout(self.result_from)
        self.setLayout(self.layout)


class BloodTestTubeViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scene = QGraphicsScene()
        self.continue_pic_viewer = QGraphicsView(self.scene)
        self.show("./ui_img/blood_test_tube.jpg")

    def show(self, img_path):
        self.image = QImage(img_path)
        self.pixmap = QPixmap.fromImage(self.image)
        self.item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(self.item)
        self.continue_pic_viewer.show()


class SerumIndicesResultForm(QFormLayout):
    def __init__(self):
        super().__init__()
        self.initProperty()
        self.initUI()

    def initProperty(self):
        self.H_indices = None # hemoglobin indices 血红蛋白
        self.L_indices = None # lipaemia indices 乳糜
        self.I_indices = None # icterus indices 黄疸

        self.H_sqr = None
        self.L_sqr = None
        self.I_sqr = None

    def initUI(self):
        self.addRow("", )


class SerumIndicesGroup(QGroupBox):
    def __init__(self):
        super().__init__()
        self.initProperty()
        self.initUI()

    def initProperty(self):
        self.H_indices = None # hemoglobin indices 血红蛋白
        self.I_indices = None # icterus indices 黄疸
        self.L_indices = None # lipaemia indices 乳糜

    def initUI(self):
        self.setTitle("血清指数参考值")

        self.H_indices_edit = QLineEdit()
        self.H_indices_edit.setReadOnly(True)
        self.H_indices_edit.setText(str(self.H_indices))

        self.I_indices_edit = QLineEdit()
        self.I_indices_edit.setReadOnly(True)
        self.I_indices_edit.setText(str(self.I_indices))

        self.L_indices_edit = QLineEdit()
        self.L_indices_edit.setReadOnly(True)
        self.L_indices_edit.setText(str(self.L_indices))

        self.addRow("H (血红蛋白):", self.H_indices_edit)
        self.addRow("I (黄疸)   :", self.I_indices_edit)
        self.addRow("L (乳糜)   :", self.L_indices_edit)

    def setIndices(self, H_indices, I_indices, L_indices):
        self.H_indices = H_indices
        self.I_indices = I_indices
        self.L_indices = L_indices

        self.H_indices_edit.setText(str(self.H_indices))
        self.I_indices_edit.setText(str(self.I_indices))
        self.L_indices_edit.setText(str(self.L_indices))

    def getIndices(self):
        return self.H_indices, self.I_indices, self.L_indices


class SerumClassGroup(QGroupBox):
    def __init__(self):
        super().__init__()
        self.initProperty()
        self.initUI()

    def initProperty(self):
        self.H_sqr = None
        self.L_sqr = None
        self.I_sqr = None

    def initUI(self):
        self.setTitle("血清指数分析结果")

        self.H_class_edit = QLineEdit()
        self.H_class_edit.setReadOnly(True)
        self.H_class_edit.setText(str(self.H_sqr))

        self.I_class_edit = QLineEdit()
        self.I_class_edit.setReadOnly(True)
        self.I_class_edit.setText(str(self.I_sqr))

        self.L_class_edit = QLineEdit()
        self.L_class_edit.setReadOnly(True)
        self.L_class_edit.setText(str(self.L_sqr))

        self.addRow("H (血红蛋白):", self.H_class_edit)
        self.addRow("I (黄疸)   :", self.I_class_edit)
        self.addRow("L (乳糜)   :", self.L_class_edit)

    def setClass(self, H_sqr, I_sqr, L_sqr):
        self.H_sqr = H_sqr
        self.I_sqr = I_sqr
        self.L_sqr = L_sqr

        self.H_class_edit.setText(str(self.H_sqr))
        self.I_class_edit.setText(str(self.I_sqr))
        self.L_class_edit.setText(str(self.L_sqr))

    def getClass(self):
        return self.H_sqr, self.I_sqr, self.L_sqr

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
