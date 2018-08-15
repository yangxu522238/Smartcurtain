This is a smart curtain project based on qualcomm 410c。 The app controls the state of the curtains, such as closing or closing the curtains to a certain degree when there is sunlight. For example, if your home is wet recently, but you are at work, you can control the opening and closing of the curtains through the mobile app.

Geting start
-------
These instruction will get you a copy of the project up and running on your 410c board

1.HardWare Requirement Dragonboard 410c Voltage conversion module Motor drive module Breadboard Line connection

2softwate requirement ubuntu development. linux 410c source code. Python3 PyQt4 & Qt designer PyCharm

Reference materials Python：https://www.python.org/ PyQt：https://doc.qt.io/archives/qt-4.8/index.html

instruction hardwareSetup: 
Dragonboard 410c
Figure 1: Development board
-----
According to the hardware schematic, GPIO_13 is selected to determine the state of the limit switch; Selecting GPIO_12 and GPI0_69 to control the forward and reverse rotation of the DC motor. When GPIO_12 is high and GPIO_69 is low, the DC motor rotates forward and the curtain opens; When GPIO_12 is low and GPIO69 is high, the DC motor reverses and the curtain closes. When GPIO_13 is low, the shade has been completely opened or closed.
（2）Voltage conversion module The output voltage of the Dragonboard 410c pin is 1.8V. However, the motor drive module requires a supply voltage of 3.3V-5V. In order to improve the stability of the system and prevent the voltage difference from causing reverse current damage to the chip, the PCA9306 voltage conversion module was chosen for bridging. As shown in Figure 3:

Figure 3: Voltage Conversion Module
-------
（3）Motor drive module The motor drive module is used to provide voltage and current to the motor and control the positive and negative rotation of the motor. （4）Breadboard Using breadboards saves wires and simplifies wiring. As shown in Figure 5:

Line connection The physical connection is shown in Figure 6:
------
Figure 6: Physical connection (1)The 24 pins (GPIO_12) and 26 pins (GPIO_690) of the J8 of the Dragonboard 410c board are connected to SCL1 and SDA1 of the voltage conversion module, respectively. (2)SCL2 and SDA2 of the voltage conversion module are connected to IN3 and IN4 of the motor drive module, respectively. (3)O3 and O4 of the motor drive block are connected to both motor pins. (4)VREF1 and VREF2 of the voltage conversion module are respectively connected to 35 pins (1.8V) and 37 pins (5V) of the Dragonboard 410c board J8. (5)The motor drive modules VIN and GND are connected to 37 pins and 2 pins (GND) of the Dragonboard 410c board J8, respectively. (6)One end of the limit switch (two springs) is grounded, and the other end is connected to a pull-up resistor. One end of the resistor is connected to the 37 pin of J8, and the other end is connected to pin 25 (GPIO_13) of J8

SoftwareSetup:
-----
1.Python3 download and install First download the Python 3.4.2 version of the Window7 64-bit installation package from Python's official website, the specific download link is https://www.python.org/downloads/release/python-342/

After the Python3.4.2 installation package is downloaded, double-click the package and follow the prompts to install. The default installation path is C:\Python34. At this point, the PC-side window7 64-bit Python 3.4.2 development environment has been configured. To verify Python 3.4.2 is installed successfully, you can use the CMD command: Start -> Run -> type cmd or command, enter Python, as shown in the following figure is Python3.4.2 environment configuration is successful. On the development board of Qualcomm 410c, Debian system system has built-in development environment of Python2 and Python3. Open the terminal and input Python3. You can see the code similar to the above figure appears, that is, Python3 is installed.

2.PyQt4 download and install In the PC's Window7 64-bit environment, PyQt uses version 4.11. This version of the exe installation file can be downloaded from the link https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11/

After the installation file is downloaded successfully, double-click it to install it. The installation path is the default path. After the installation is successful, you can find the PyQt4 related files in the path of C:\Python34\Lib\site-packages\PyQt4. In this path, the designer.exe file is the Qt GUI design software, and the user can design the UI style of the GUI software in the software.

At this point, the PyQt4 environment on the Windows 7 64-bit PC has been configured. 3.PyCharm download and install First, download the installation package from PyCharm official website. The official website link is https://www.jetbrains.com/pycharm/. The version selected here is pycharm-community-2018.1.1. After the download is successful, install it.

Next configure QtDesigner, open Pycharm, select File->Settings, select Tools->External Tools in the pop-up panel, click the Add button to edit the information as follows: The Name tag is set to QtDesigner, Program is the designer.exe file in the PyQt4 installation directory, and the Working Directory is PyQt4's installation directory. Click OK to add it successfully. Configure PyUIC, also click the Add button, the configuration information is as follows: Name is set to PyUIC, Program is a Python file in the Python installation directory, Arguments is set to -m PyQt4.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py, Working Directory is $FileDir$, click OK to add success.

Configure PYRCC and the configuration information is as follows: Name is set to PYRCC, Program is the pyrcc4.exe file in the PyQt4 installation directory, Arguments is set to -py3 $FileName$ -o $FileNameWithoutExtension$_rc.py, Working Directory is $FileDir$, click OK to add it successfully. The final environment configuration information is as follows: Three、Qualcomm 410c operating environment 1.Update system Open the terminal, enter sudo apt-get update and press Enter Key 2.Pip download and install Open the terminal, enter sudo apt-get install python3-pip. If you see the following prompt: ble to fetch some archives, maybe run apt-get update or try with --fix-missing Please enter sudo apt-get update and reenter sudo apt-get install python3-pip 3.PyQt4 download and install Open the terminal and entersudo apt-get install python3-pyqt4 to install PyQt4 until the installation success flag appears.

about "how to Build application" , "how to start the application","how to use the application" and "how to stop application" you can check the file that's name is Bottom design of smart curtain based on Dragonboard 410c.doc Demo-Electric curtain.docx PyQt development environment.docx
