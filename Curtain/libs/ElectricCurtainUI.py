# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoUI.ui'
#
# Created: Fri Apr 27 10:24:57 2018
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(14)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Bg = QtGui.QLabel(self.centralwidget)
        self.Bg.setEnabled(True)
        self.Bg.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.Bg.setAutoFillBackground(False)
        self.Bg.setStyleSheet(_fromUtf8("image: url(:/images/main_bg.png);"))
        self.Bg.setText(_fromUtf8(""))
        self.Bg.setObjectName(_fromUtf8("Bg"))
        self.ControlSlider = QtGui.QSlider(self.centralwidget)
        self.ControlSlider.setEnabled(True)
        self.ControlSlider.setGeometry(QtCore.QRect(179, 150, 421, 20))
        self.ControlSlider.setMaximum(100)
        self.ControlSlider.setPageStep(1)
        self.ControlSlider.setTracking(False)
        self.ControlSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ControlSlider.setObjectName(_fromUtf8("ControlSlider"))
        self.CurValue = QtGui.QLabel(self.centralwidget)
        self.CurValue.setGeometry(QtCore.QRect(620, 150, 41, 20))
        self.CurValue.setObjectName(_fromUtf8("CurValue"))
        self.SysDataLabel = QtGui.QLabel(self.centralwidget)
        self.SysDataLabel.setGeometry(QtCore.QRect(20, 20, 200, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SysDataLabel.sizePolicy().hasHeightForWidth())
        self.SysDataLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SysDataLabel.setFont(font)
        self.SysDataLabel.setObjectName(_fromUtf8("SysDataLabel"))
        self.SysTimeLabel = QtGui.QLabel(self.centralwidget)
        self.SysTimeLabel.setGeometry(QtCore.QRect(580, 20, 200, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SysTimeLabel.sizePolicy().hasHeightForWidth())
        self.SysTimeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SysTimeLabel.setFont(font)
        self.SysTimeLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.SysTimeLabel.setScaledContents(False)
        self.SysTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SysTimeLabel.setObjectName(_fromUtf8("SysTimeLabel"))
        self.Tiplabel = QtGui.QLabel(self.centralwidget)
        self.Tiplabel.setGeometry(QtCore.QRect(0, 560, 800, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Tiplabel.setFont(font)
        self.Tiplabel.setStyleSheet(_fromUtf8("color: rgb(255, 64, 58);"))
        self.Tiplabel.setText(_fromUtf8(""))
        self.Tiplabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Tiplabel.setObjectName(_fromUtf8("Tiplabel"))
        self.ListWidget = QtGui.QListWidget(self.centralwidget)
        self.ListWidget.setGeometry(QtCore.QRect(200, 240, 400, 211))
        self.ListWidget.setObjectName(_fromUtf8("ListWidget"))
        self.DeleteMissionBtn = QtGui.QPushButton(self.centralwidget)
        self.DeleteMissionBtn.setGeometry(QtCore.QRect(290, 470, 75, 23))
        self.DeleteMissionBtn.setObjectName(_fromUtf8("DeleteMissionBtn"))
        self.AddMissionBtn = QtGui.QPushButton(self.centralwidget)
        self.AddMissionBtn.setGeometry(QtCore.QRect(200, 470, 75, 23))
        self.AddMissionBtn.setObjectName(_fromUtf8("AddMissionBtn"))
        self.MissionTitle = QtGui.QLabel(self.centralwidget)
        self.MissionTitle.setGeometry(QtCore.QRect(0, 210, 800, 16))
        self.MissionTitle.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.MissionTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.MissionTitle.setObjectName(_fromUtf8("MissionTitle"))
        self.CurtainState = QtGui.QLabel(self.centralwidget)
        self.CurtainState.setGeometry(QtCore.QRect(0, 0, 800, 16))
        self.CurtainState.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.CurtainState.setAlignment(QtCore.Qt.AlignCenter)
        self.CurtainState.setObjectName(_fromUtf8("CurtainState"))
        self.ControlSliderOperationTip = QtGui.QLabel(self.centralwidget)
        self.ControlSliderOperationTip.setGeometry(QtCore.QRect(0, 110, 800, 16))
        self.ControlSliderOperationTip.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.ControlSliderOperationTip.setAlignment(QtCore.Qt.AlignCenter)
        self.ControlSliderOperationTip.setObjectName(_fromUtf8("ControlSliderOperationTip"))
        self.ComfirmBtn = QtGui.QPushButton(self.centralwidget)
        self.ComfirmBtn.setEnabled(False)
        self.ComfirmBtn.setGeometry(QtCore.QRect(450, 470, 75, 23))
        self.ComfirmBtn.setObjectName(_fromUtf8("ComfirmBtn"))
        self.MissionDataTime = QtGui.QDateTimeEdit(self.centralwidget)
        self.MissionDataTime.setGeometry(QtCore.QRect(200, 510, 171, 22))
        self.MissionDataTime.setAutoFillBackground(False)
        self.MissionDataTime.setCalendarPopup(True)
        self.MissionDataTime.setEnabled(False)
        self.MissionDataTime.setObjectName(_fromUtf8("MissionDataTime"))
        self.MissionValue = QtGui.QLabel(self.centralwidget)
        self.MissionValue.setGeometry(QtCore.QRect(570, 510, 54, 12))
        self.MissionValue.setObjectName(_fromUtf8("MissionValue"))
        self.MissionSlider = QtGui.QSlider(self.centralwidget)
        self.MissionSlider.setGeometry(QtCore.QRect(390, 510, 160, 19))
        self.MissionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MissionSlider.setObjectName(_fromUtf8("MissionSlider"))
        self.MissionSlider.setEnabled(False)
        self.CancelBtn = QtGui.QPushButton(self.centralwidget)
        self.CancelBtn.setEnabled(False)
        self.CancelBtn.setGeometry(QtCore.QRect(530, 470, 75, 23))
        self.CancelBtn.setObjectName(_fromUtf8("CancelBtn"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.ControlSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), MainWindow.OnSliderReleased)
        QtCore.QObject.connect(self.ControlSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.CurValue.setNum)
        QtCore.QObject.connect(self.DeleteMissionBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.OnDeleteMissionClicked)
        QtCore.QObject.connect(self.AddMissionBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.OnAddMissionClicked)
        QtCore.QObject.connect(self.MissionSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.MissionValue.setNum)
        QtCore.QObject.connect(self.ComfirmBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.OnConfirmBtnClicked)
        QtCore.QObject.connect(self.CancelBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.OnCancelBtnClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.MissionDataTime, self.ControlSlider)
        MainWindow.setTabOrder(self.ControlSlider, self.ListWidget)
        MainWindow.setTabOrder(self.ListWidget, self.AddMissionBtn)
        MainWindow.setTabOrder(self.AddMissionBtn, self.DeleteMissionBtn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Electric curtain", None))
        self.CurValue.setText(_translate("MainWindow", "0", None))
        self.SysDataLabel.setText(_translate("MainWindow", "", None))
        self.SysTimeLabel.setText(_translate("MainWindow", "", None))
        self.DeleteMissionBtn.setText(_translate("MainWindow", "", None))
        self.AddMissionBtn.setText(_translate("MainWindow", "", None))
        self.MissionTitle.setText(_translate("MainWindow", "：", None))
        self.CurtainState.setText(_translate("MainWindow", "：", None))
        self.ControlSliderOperationTip.setText(_translate("MainWindow", "", None))
        self.ComfirmBtn.setText(_translate("MainWindow", "", None))
        self.MissionValue.setText(_translate("MainWindow", "0", None))
        self.CancelBtn.setText(_translate("MainWindow", "", None))

import libs.APPResources_rc
