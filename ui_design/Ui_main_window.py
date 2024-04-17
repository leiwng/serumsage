# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Prj\voyager\serumsage\ui_design\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(3840, 2160))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.workModeTab = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.workModeTab.sizePolicy().hasHeightForWidth())
        self.workModeTab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.workModeTab.setFont(font)
        self.workModeTab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.workModeTab.setObjectName("workModeTab")
        self.tab4CD = QtWidgets.QWidget()
        self.tab4CD.setObjectName("tab4CD")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab4CD)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab4CD)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_8 = QtWidgets.QWidget(self.groupBox)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tubeImgGView4CD = QtWidgets.QGraphicsView(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tubeImgGView4CD.sizePolicy().hasHeightForWidth())
        self.tubeImgGView4CD.setSizePolicy(sizePolicy)
        self.tubeImgGView4CD.setObjectName("tubeImgGView4CD")
        self.gridLayout_4.addWidget(self.tubeImgGView4CD, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_8, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.widget = QtWidgets.QWidget(self.tab4CD)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.HIndicesLCD4CD = QtWidgets.QLCDNumber(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HIndicesLCD4CD.sizePolicy().hasHeightForWidth())
        self.HIndicesLCD4CD.setSizePolicy(sizePolicy)
        self.HIndicesLCD4CD.setObjectName("HIndicesLCD4CD")
        self.horizontalLayout_2.addWidget(self.HIndicesLCD4CD)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.IIndicesLCD4CD = QtWidgets.QLCDNumber(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IIndicesLCD4CD.sizePolicy().hasHeightForWidth())
        self.IIndicesLCD4CD.setSizePolicy(sizePolicy)
        self.IIndicesLCD4CD.setObjectName("IIndicesLCD4CD")
        self.horizontalLayout_3.addWidget(self.IIndicesLCD4CD)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.LIndicesLCD4CD = QtWidgets.QLCDNumber(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LIndicesLCD4CD.sizePolicy().hasHeightForWidth())
        self.LIndicesLCD4CD.setSizePolicy(sizePolicy)
        self.LIndicesLCD4CD.setObjectName("LIndicesLCD4CD")
        self.horizontalLayout_4.addWidget(self.LIndicesLCD4CD)
        self.verticalLayout.addWidget(self.widget_4)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.HClassEdit4CD = QtWidgets.QLineEdit(self.widget_5)
        self.HClassEdit4CD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HClassEdit4CD.sizePolicy().hasHeightForWidth())
        self.HClassEdit4CD.setSizePolicy(sizePolicy)
        self.HClassEdit4CD.setReadOnly(True)
        self.HClassEdit4CD.setObjectName("HClassEdit4CD")
        self.horizontalLayout_5.addWidget(self.HClassEdit4CD)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.IClassEdit4CD = QtWidgets.QLineEdit(self.widget_6)
        self.IClassEdit4CD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IClassEdit4CD.sizePolicy().hasHeightForWidth())
        self.IClassEdit4CD.setSizePolicy(sizePolicy)
        self.IClassEdit4CD.setReadOnly(True)
        self.IClassEdit4CD.setObjectName("IClassEdit4CD")
        self.horizontalLayout_6.addWidget(self.IClassEdit4CD)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.LClassEdit4CD = QtWidgets.QLineEdit(self.widget_7)
        self.LClassEdit4CD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LClassEdit4CD.sizePolicy().hasHeightForWidth())
        self.LClassEdit4CD.setSizePolicy(sizePolicy)
        self.LClassEdit4CD.setReadOnly(True)
        self.LClassEdit4CD.setObjectName("LClassEdit4CD")
        self.horizontalLayout_7.addWidget(self.LClassEdit4CD)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout.addWidget(self.widget)
        self.workModeTab.addTab(self.tab4CD, "")
        self.tab4CD1 = QtWidgets.QWidget()
        self.tab4CD1.setObjectName("tab4CD1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab4CD1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_9 = QtWidgets.QWidget(self.tab4CD1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.selectTubeImgBtn = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(18)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectTubeImgBtn.sizePolicy().hasHeightForWidth())
        self.selectTubeImgBtn.setSizePolicy(sizePolicy)
        self.selectTubeImgBtn.setObjectName("selectTubeImgBtn")
        self.horizontalLayout_16.addWidget(self.selectTubeImgBtn)
        self.label_7 = QtWidgets.QLabel(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_16.addWidget(self.label_7)
        self.tubeImgFullPathEdit = QtWidgets.QLineEdit(self.widget_9)
        self.tubeImgFullPathEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tubeImgFullPathEdit.sizePolicy().hasHeightForWidth())
        self.tubeImgFullPathEdit.setSizePolicy(sizePolicy)
        self.tubeImgFullPathEdit.setText("")
        self.tubeImgFullPathEdit.setPlaceholderText("")
        self.tubeImgFullPathEdit.setObjectName("tubeImgFullPathEdit")
        self.horizontalLayout_16.addWidget(self.tubeImgFullPathEdit)
        self.verticalLayout_6.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.tab4CD1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tubeImgGView4SD = QtWidgets.QGraphicsView(self.groupBox_4)
        self.tubeImgGView4SD.setObjectName("tubeImgGView4SD")
        self.gridLayout_2.addWidget(self.tubeImgGView4SD, 0, 0, 1, 1)
        self.horizontalLayout_14.addWidget(self.groupBox_4)
        self.widget_11 = QtWidgets.QWidget(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setObjectName("widget_11")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_11)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget_11)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_12 = QtWidgets.QWidget(self.groupBox_5)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget_12)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.HIndicesLCD4SD = QtWidgets.QLCDNumber(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HIndicesLCD4SD.sizePolicy().hasHeightForWidth())
        self.HIndicesLCD4SD.setSizePolicy(sizePolicy)
        self.HIndicesLCD4SD.setObjectName("HIndicesLCD4SD")
        self.horizontalLayout_8.addWidget(self.HIndicesLCD4SD)
        self.verticalLayout_4.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.groupBox_5)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.widget_13)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.IIndicesLCD4SD = QtWidgets.QLCDNumber(self.widget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IIndicesLCD4SD.sizePolicy().hasHeightForWidth())
        self.IIndicesLCD4SD.setSizePolicy(sizePolicy)
        self.IIndicesLCD4SD.setObjectName("IIndicesLCD4SD")
        self.horizontalLayout_9.addWidget(self.IIndicesLCD4SD)
        self.verticalLayout_4.addWidget(self.widget_13)
        self.widget_14 = QtWidgets.QWidget(self.groupBox_5)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.widget_14)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.LIndicesLCD4SD = QtWidgets.QLCDNumber(self.widget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LIndicesLCD4SD.sizePolicy().hasHeightForWidth())
        self.LIndicesLCD4SD.setSizePolicy(sizePolicy)
        self.LIndicesLCD4SD.setObjectName("LIndicesLCD4SD")
        self.horizontalLayout_10.addWidget(self.LIndicesLCD4SD)
        self.verticalLayout_4.addWidget(self.widget_14)
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget_11)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_15 = QtWidgets.QWidget(self.groupBox_6)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.widget_15)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.HClassEdit4SD = QtWidgets.QLineEdit(self.widget_15)
        self.HClassEdit4SD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HClassEdit4SD.sizePolicy().hasHeightForWidth())
        self.HClassEdit4SD.setSizePolicy(sizePolicy)
        self.HClassEdit4SD.setReadOnly(True)
        self.HClassEdit4SD.setObjectName("HClassEdit4SD")
        self.horizontalLayout_11.addWidget(self.HClassEdit4SD)
        self.verticalLayout_5.addWidget(self.widget_15)
        self.widget_16 = QtWidgets.QWidget(self.groupBox_6)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.widget_16)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.IClassEdit4SD = QtWidgets.QLineEdit(self.widget_16)
        self.IClassEdit4SD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IClassEdit4SD.sizePolicy().hasHeightForWidth())
        self.IClassEdit4SD.setSizePolicy(sizePolicy)
        self.IClassEdit4SD.setReadOnly(True)
        self.IClassEdit4SD.setObjectName("IClassEdit4SD")
        self.horizontalLayout_12.addWidget(self.IClassEdit4SD)
        self.verticalLayout_5.addWidget(self.widget_16)
        self.widget_17 = QtWidgets.QWidget(self.groupBox_6)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.widget_17)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.LClassEdit4SD = QtWidgets.QLineEdit(self.widget_17)
        self.LClassEdit4SD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LClassEdit4SD.sizePolicy().hasHeightForWidth())
        self.LClassEdit4SD.setSizePolicy(sizePolicy)
        self.LClassEdit4SD.setReadOnly(True)
        self.LClassEdit4SD.setObjectName("LClassEdit4SD")
        self.horizontalLayout_13.addWidget(self.LClassEdit4SD)
        self.verticalLayout_5.addWidget(self.widget_17)
        self.gridLayout_5.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.horizontalLayout_14.addWidget(self.widget_11)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)
        self.verticalLayout_6.addWidget(self.widget_10)
        self.workModeTab.addTab(self.tab4CD1, "")
        self.tab4RB = QtWidgets.QWidget()
        self.tab4RB.setObjectName("tab4RB")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab4RB)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_18 = QtWidgets.QWidget(self.tab4RB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.widget_18)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_14 = QtWidgets.QLabel(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_23.addWidget(self.label_14)
        self.outputFolderPathEdit = QtWidgets.QLineEdit(self.widget_18)
        self.outputFolderPathEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(55)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputFolderPathEdit.sizePolicy().hasHeightForWidth())
        self.outputFolderPathEdit.setSizePolicy(sizePolicy)
        self.outputFolderPathEdit.setObjectName("outputFolderPathEdit")
        self.horizontalLayout_23.addWidget(self.outputFolderPathEdit)
        self.verticalLayout_9.addWidget(self.widget_18)
        self.widget_19 = QtWidgets.QWidget(self.tab4RB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(55)
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.groupBox_10 = QtWidgets.QGroupBox(self.widget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.outputFileList = QtWidgets.QListWidget(self.groupBox_10)
        self.outputFileList.setObjectName("outputFileList")
        self.gridLayout_8.addWidget(self.outputFileList, 0, 0, 1, 1)
        self.horizontalLayout_24.addWidget(self.groupBox_10)
        self.groupBox_7 = QtWidgets.QGroupBox(self.widget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tubeImgGView4RB = QtWidgets.QGraphicsView(self.groupBox_7)
        self.tubeImgGView4RB.setObjectName("tubeImgGView4RB")
        self.gridLayout_6.addWidget(self.tubeImgGView4RB, 0, 0, 1, 1)
        self.horizontalLayout_24.addWidget(self.groupBox_7)
        self.widget_20 = QtWidgets.QWidget(self.widget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.widget_20.setFont(font)
        self.widget_20.setObjectName("widget_20")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_20)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox_8 = QtWidgets.QGroupBox(self.widget_20)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_21 = QtWidgets.QWidget(self.groupBox_8)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.widget_21)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.HIndicesLCD4RB = QtWidgets.QLCDNumber(self.widget_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HIndicesLCD4RB.sizePolicy().hasHeightForWidth())
        self.HIndicesLCD4RB.setSizePolicy(sizePolicy)
        self.HIndicesLCD4RB.setObjectName("HIndicesLCD4RB")
        self.horizontalLayout_17.addWidget(self.HIndicesLCD4RB)
        self.verticalLayout_7.addWidget(self.widget_21)
        self.widget_22 = QtWidgets.QWidget(self.groupBox_8)
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_22)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_16 = QtWidgets.QLabel(self.widget_22)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_18.addWidget(self.label_16)
        self.IIndicesLCD4RB = QtWidgets.QLCDNumber(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IIndicesLCD4RB.sizePolicy().hasHeightForWidth())
        self.IIndicesLCD4RB.setSizePolicy(sizePolicy)
        self.IIndicesLCD4RB.setObjectName("IIndicesLCD4RB")
        self.horizontalLayout_18.addWidget(self.IIndicesLCD4RB)
        self.verticalLayout_7.addWidget(self.widget_22)
        self.widget_23 = QtWidgets.QWidget(self.groupBox_8)
        self.widget_23.setObjectName("widget_23")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_23)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_17 = QtWidgets.QLabel(self.widget_23)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_19.addWidget(self.label_17)
        self.LIndicesLCD4RB = QtWidgets.QLCDNumber(self.widget_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LIndicesLCD4RB.sizePolicy().hasHeightForWidth())
        self.LIndicesLCD4RB.setSizePolicy(sizePolicy)
        self.LIndicesLCD4RB.setObjectName("LIndicesLCD4RB")
        self.horizontalLayout_19.addWidget(self.LIndicesLCD4RB)
        self.verticalLayout_7.addWidget(self.widget_23)
        self.verticalLayout_10.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.widget_20)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_24 = QtWidgets.QWidget(self.groupBox_9)
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_24)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_18 = QtWidgets.QLabel(self.widget_24)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_20.addWidget(self.label_18)
        self.HClassEdit4RB = QtWidgets.QLineEdit(self.widget_24)
        self.HClassEdit4RB.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HClassEdit4RB.sizePolicy().hasHeightForWidth())
        self.HClassEdit4RB.setSizePolicy(sizePolicy)
        self.HClassEdit4RB.setReadOnly(True)
        self.HClassEdit4RB.setObjectName("HClassEdit4RB")
        self.horizontalLayout_20.addWidget(self.HClassEdit4RB)
        self.verticalLayout_8.addWidget(self.widget_24)
        self.widget_25 = QtWidgets.QWidget(self.groupBox_9)
        self.widget_25.setObjectName("widget_25")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_25)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_19 = QtWidgets.QLabel(self.widget_25)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_21.addWidget(self.label_19)
        self.IClassEdit4RB = QtWidgets.QLineEdit(self.widget_25)
        self.IClassEdit4RB.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IClassEdit4RB.sizePolicy().hasHeightForWidth())
        self.IClassEdit4RB.setSizePolicy(sizePolicy)
        self.IClassEdit4RB.setReadOnly(True)
        self.IClassEdit4RB.setObjectName("IClassEdit4RB")
        self.horizontalLayout_21.addWidget(self.IClassEdit4RB)
        self.verticalLayout_8.addWidget(self.widget_25)
        self.widget_26 = QtWidgets.QWidget(self.groupBox_9)
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_26)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_20 = QtWidgets.QLabel(self.widget_26)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_22.addWidget(self.label_20)
        self.LClassEdit4RB = QtWidgets.QLineEdit(self.widget_26)
        self.LClassEdit4RB.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LClassEdit4RB.sizePolicy().hasHeightForWidth())
        self.LClassEdit4RB.setSizePolicy(sizePolicy)
        self.LClassEdit4RB.setReadOnly(True)
        self.LClassEdit4RB.setObjectName("LClassEdit4RB")
        self.horizontalLayout_22.addWidget(self.LClassEdit4RB)
        self.verticalLayout_8.addWidget(self.widget_26)
        self.verticalLayout_10.addWidget(self.groupBox_9)
        self.horizontalLayout_24.addWidget(self.widget_20)
        self.verticalLayout_9.addWidget(self.widget_19)
        self.workModeTab.addTab(self.tab4RB, "")
        self.gridLayout.addWidget(self.workModeTab, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.action.setFont(font)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.serumSegaAboutAction = QtWidgets.QAction(MainWindow)
        self.serumSegaAboutAction.setObjectName("serumSegaAboutAction")
        self.sysCfgAction = QtWidgets.QAction(MainWindow)
        self.sysCfgAction.setObjectName("sysCfgAction")
        self.config_user_action = QtWidgets.QAction(MainWindow)
        self.config_user_action.setObjectName("config_user_action")
        self.menu.addAction(self.sysCfgAction)
        self.menu_2.addAction(self.serumSegaAboutAction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.workModeTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "血清指数智能判读-SerumSage"))
        self.groupBox.setTitle(_translate("MainWindow", "试管图片"))
        self.groupBox_2.setTitle(_translate("MainWindow", "血清指数检测结果"))
        self.label.setText(_translate("MainWindow", "H (血红蛋白指数):"))
        self.label_2.setText(_translate("MainWindow", "I (黄疸指数):        "))
        self.label_3.setText(_translate("MainWindow", "L (乳糜指数):       "))
        self.groupBox_3.setTitle(_translate("MainWindow", "血清指数分类结果"))
        self.label_4.setText(_translate("MainWindow", "H (血红蛋白指数分类):"))
        self.label_6.setText(_translate("MainWindow", "I (黄疸指数分类):        "))
        self.label_5.setText(_translate("MainWindow", "L (乳糜指数分类):       "))
        self.workModeTab.setTabText(self.workModeTab.indexOf(self.tab4CD), _translate("MainWindow", "连续检测"))
        self.selectTubeImgBtn.setText(_translate("MainWindow", "选择血液试管图片"))
        self.label_7.setText(_translate("MainWindow", "图片路径:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "试管图片"))
        self.groupBox_5.setTitle(_translate("MainWindow", "血清指数检测结果"))
        self.label_8.setText(_translate("MainWindow", "H (血红蛋白指数):"))
        self.label_9.setText(_translate("MainWindow", "I (黄疸指数):        "))
        self.label_10.setText(_translate("MainWindow", "L (乳糜指数):       "))
        self.groupBox_6.setTitle(_translate("MainWindow", "血清指数分类结果"))
        self.label_11.setText(_translate("MainWindow", "H (血红蛋白指数分类):"))
        self.label_12.setText(_translate("MainWindow", "I (黄疸指数分类):        "))
        self.label_13.setText(_translate("MainWindow", "L (乳糜指数分类):       "))
        self.workModeTab.setTabText(self.workModeTab.indexOf(self.tab4CD1), _translate("MainWindow", "单次检测"))
        self.label_14.setText(_translate("MainWindow", "检测结果目录:"))
        self.groupBox_10.setTitle(_translate("MainWindow", "文件列表"))
        self.groupBox_7.setTitle(_translate("MainWindow", "图片预览"))
        self.groupBox_8.setTitle(_translate("MainWindow", "血清指数检测结果"))
        self.label_15.setText(_translate("MainWindow", "H (血红蛋白指数):"))
        self.label_16.setText(_translate("MainWindow", "I (黄疸指数):        "))
        self.label_17.setText(_translate("MainWindow", "L (乳糜指数):       "))
        self.groupBox_9.setTitle(_translate("MainWindow", "血清指数分类结果"))
        self.label_18.setText(_translate("MainWindow", "H (血红蛋白指数分类):"))
        self.label_19.setText(_translate("MainWindow", "I (黄疸指数分类):        "))
        self.label_20.setText(_translate("MainWindow", "L (乳糜指数分类):       "))
        self.workModeTab.setTabText(self.workModeTab.indexOf(self.tab4RB), _translate("MainWindow", "结果浏览"))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.action.setText(_translate("MainWindow", "工作目录设置"))
        self.action_2.setText(_translate("MainWindow", "用户设置"))
        self.serumSegaAboutAction.setText(_translate("MainWindow", "血清指数智能检测软件(SerumSega)"))
        self.sysCfgAction.setText(_translate("MainWindow", "系统设置"))
        self.config_user_action.setText(_translate("MainWindow", "用户设置"))
