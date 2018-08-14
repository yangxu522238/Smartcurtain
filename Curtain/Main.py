import sys,os
import libs.TimeManager
import libs.IOManager
import libs.WilddogManager
import libs.AppDataManager
import libs.CurtainManager

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTimer
from libs.ElectricCurtainUI import Ui_MainWindow

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Value Properties
        self._missionList = []
        self._tipTimer = QTimer(self)
        self._tipTimer.setSingleShot(True)
        self._isTestMode=True         # If Test Mode

        # Module Properties
        self._timeMgr = libs.TimeManager.TimeMgr()
        self._webCrawler = libs.WilddogManager.WebCrawler(self.WebCrawlerCallBack)
        self._appDataMgr = libs.AppDataManager.DataMsg()
        self._ioMgr = libs.IOManager.IOMgr()

        # Curtain Init
        self.curtain= libs.CurtainManager.Curtain(self,15)
        self.curtain.CommandStopCallBack.append(self.OnCurtainStop)
        self.curtain.CommandStartCallBack.append(self.OnCurtainStart)
        self.curtain.CommandRunningCallBack.append(self.OnCurtainPosUpdate)
        self.curtain.CurtainResetingCallBack.append(self.OnCurtainReseting)

        if(not self._isTestMode):
            self.curtain.ResetCurtain() # 重置初始化

        # Common Logic Init
        self._tipTimer.timeout.connect(lambda: self.Tiplabel.setText(""))
        self._sysDataTime = self._timeMgr.GetSystemDataTime()
        self._webCrawler.StartReadUrlLoop(self._appDataMgr.WilddogLoopTimer, self._appDataMgr.WilddofUrl)
        self._timeMgr.StartUpdateDataTime(self.UpdateDataTimeLabel)

        # UI Init

        self.ControlSlider.setMaximum(self.curtain.CurtainRunTime)
        self.ControlSliderOperationTip.setText(self._appDataMgr.LocalizationMsg.ControlSliderOperationTipStr)

        self.AddMissionBtn.setText(self._appDataMgr.LocalizationMsg.AddMissionBtnStr)
        self.DeleteMissionBtn.setText(self._appDataMgr.LocalizationMsg.DeleteMissionBtnStr)
        self.ComfirmBtn.setText(self._appDataMgr.LocalizationMsg.ComfirmBtnStr)
        self.CancelBtn.setText(self._appDataMgr.LocalizationMsg.CancelBtnStr)

        self.MissionTitle.setText(self._appDataMgr.LocalizationMsg.MissionTitleStr)
        self.MissionSlider.setMaximum(self.curtain.CurtainRunTime)
        self.MissionDataTime.setDisplayFormat(self._appDataMgr.DataTimeFormat)
        self.MissionDataTime.setDateTime(self._sysDataTime)

    # CallBack Function
    def UpdateDataTimeLabel(self,dataTime):
        self._sysDataTime = dataTime
        self.SysDataLabel.setText(dataTime.toString(self._appDataMgr.DataFormat))
        self.SysTimeLabel.setText(dataTime.toString(self._appDataMgr.TimeFormat))

    def WebCrawlerCallBack(self, str):
        print(str)

    # UI Functions
    def OnSliderReleased(self):
        print("OnSliderReleased"+str(self.CurValue.text()))
        selectValue = self.CurValue.text()
        self.curtain.ControlCurtainWithTargetPos(int(selectValue))
    def ShowTip(self,TipStr,waitTime):
        self.Tiplabel.setText(TipStr)
        if(self._tipTimer.isActive()):
            self._tipTimer.stop()
        self._tipTimer.start(waitTime*1000)
    def OnAddMissionClicked(self):
        self._missionOperationType = 0  # 0 is add operation 1 is remove operation

        self.AddMissionBtn.setEnabled(False)
        self.DeleteMissionBtn.setEnabled(False)
        self.ComfirmBtn.setEnabled(True)
        self.CancelBtn.setEnabled(True)
        self.MissionDataTime.setEnabled(True)
        self.MissionSlider.setEnabled(True)
    def OnDeleteMissionClicked(self):
        self._missionOperationType = 1  # 0 is add operation 1 is remove operation

        self.AddMissionBtn.setEnabled(False)
        self.DeleteMissionBtn.setEnabled(False)
        self.ComfirmBtn.setEnabled(True)
        self.CancelBtn.setEnabled(True)
    def OnConfirmBtnClicked(self):
        if(self._missionOperationType==0):
            if(self.AddMission()==False):
                return
        elif(self._missionOperationType==1):
            if(self.RemoveMission()==False):
                return
        print("OnConfirmBtnClicked")
        self.ResetMissionOperationPlane()
    def OnCancelBtnClicked(self):
        print("OnCancelBtnClicked")
        self.ResetMissionOperationPlane()
    def ResetMissionOperationPlane(self):
        self.MissionDataTime.setDateTime(self._sysDataTime)
        self.MissionSlider.setValue(0)
        self.AddMissionBtn.setEnabled(True)
        self.DeleteMissionBtn.setEnabled(True)
        self.ComfirmBtn.setEnabled(False)
        self.CancelBtn.setEnabled(False)
        self.MissionDataTime.setEnabled(False)
        self.MissionSlider.setEnabled(False)

    # Mission Functions
    def AddMission(self):
        print("AddMission")
        selectDataTime = self.MissionDataTime.dateTime()
        selectTimeStamp = selectDataTime.toTime_t()
        if (selectTimeStamp in self._missionList):
            self.ShowTip(self._appDataMgr.LocalizationMsg.AddMissionError, 3)
            return False
        sysTimeStamp = self._sysDataTime.toTime_t()
        waitTime = selectTimeStamp - sysTimeStamp
        if (waitTime < self._appDataMgr.MissionIntervalTime):
            self.ShowTip(self._appDataMgr.LocalizationMsg.AddMissionError, 3)
            return False
        else:
            self._missionList.append(selectTimeStamp)
            listItem = MyListItem(selectDataTime,self.MissionSlider.value())
            self.ListWidget.addItem(listItem)
            self.ListWidget.sortItems()
        return  True

    def RemoveMission(self):
        print("RemoveMission")
        curItem = self.ListWidget.currentRow()
        self.ListWidget.takeItem(curItem)
        return  True

    # Curtain CallBack Function
    def OnCurtainReseting(self):
        print("OnCurtainReseting")
        self.ControlSlider.setEnabled(False)
        self.CurtainState.setText(self._appDataMgr.LocalizationMsg.CurtainResetTipStr)
    def OnCurtainStart(self):
        print("OnCurtainStart")
        self.ControlSlider.setEnabled(False)
    def OnCurtainStop(self):
        print("OnCurtainStop")
        self.CurtainState.setText(self._appDataMgr.LocalizationMsg.CurtaionStopTipStr)
        self.ControlSlider.setEnabled(True)
    def OnCurtainPosUpdate(self,pos):
        # print("OnCurtainPosUpdate"+str(pos))
        self.CurtainState.setText(self._appDataMgr.LocalizationMsg.CurtaionRunningTipStr+str(self.curtain.Position))
        self.ControlSlider.setValue(self.curtain.Position)
        self.CurValue.setText(str(pos))

    # IO functions
    def GetIOPath(self):
        path = ""
        if(self._isTestMode):
            path = self._appDataMgr.TestIOFilePath
        else:
            path = self._appDataMgr.IOFilePath
        return path

class MyListItem(QtGui.QListWidgetItem):
    def __init__(self,targetTime,targetPos):
        self.targetPos=targetPos
        self.targetTimeStamp = targetTime.toTime_t()

        self.timer = QTimer()
        self.timer.timeout.connect(self.TimerCallBack)
        QtGui.QListWidgetItem.__init__(self, targetTime.toString(window._appDataMgr.DataTimeFormat) +"      TargetPos" + str(self.targetPos))
        self.timer.start((self.targetTimeStamp - window._timeMgr.GetSystemDataTimeStamp())*1000)
    def __del__(self):
        print("MyListItem __del__")
        if (self.targetTimeStamp in window._missionList):
            window._missionList.remove(self.targetTimeStamp)
        if (self.timer.isActive()):
            self.timer.stop()
    def TimerCallBack(self):
        self.ControlCurtain()
        window.ListWidget.takeItem(window.ListWidget.row(self))
    def ControlCurtain(self):
        window.curtain.ControlCurtainWithTargetPos(self.targetPos)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())