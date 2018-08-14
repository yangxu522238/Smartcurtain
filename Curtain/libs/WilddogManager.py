# -*- coding: utf-8 -*-
import urllib.request
import threading
from PyQt4.QtCore import QTimer
from PyQt4 import QtGui

class WebCrawler(QtGui.QMainWindow):
    def __init__(self,func):
        QtGui.QMainWindow.__init__(self)
        self._func=func

    def StartReadUrlLoop(self,loopTime,url):
        self._url=url
        self._delayTime=0
        self._listenWebTimer = QTimer(self)
        self._listenWebTimer.setInterval(loopTime*1000)
        self._listenWebTimer.timeout.connect(self.ReadUrl)
        self._listenWebTimer.start()
    def StopReadUrlLoop(self):
        if(self._listenWebTimer.isActive()):
            self._listenWebTimer.stop()
    def ReadUrl(self):
        timer = threading.Timer(self._delayTime, self.ReadUrlInfo)
        timer.start()
    def ReadUrlInfo(self):
        content = urllib.request.urlopen(self._url).read()
        if(self._func):
            self._func(content)