from PyQt5 import QtWidgets, QtGui, QtCore
# uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal

import time
import threading


############################### EXERCISE 2 ################################
class MyThread_sweep(QThread):
    sweepLedsSignal = pyqtSignal(int)

    def run(self):
        self.sweepLedsSignal.emit(1)
        time.sleep(0.5)
        self.sweepLedsSignal.emit(2)
        time.sleep(0.5)
        self.sweepLedsSignal.emit(3)
        time.sleep(0.5)
        self.sweepLedsSignal.emit(4)
        time.sleep(0.5)
        self.sweepLedsSignal.emit(5)


############################### EXERCISE 6 #################################
class MyThread_warning(QThread):
    warningLightsSignal = pyqtSignal(int)

    def run(self):
        while True:
            self.warningLightsSignal.emit(1)
            time.sleep(0.5)
            self.warningLightsSignal.emit(2)
            time.sleep(0.5)


############################### EXERCISE 7 #################################
class MyThread_left(QThread):
    leftLightsSignal = pyqtSignal(int)

    def run(self):
        while True:
            self.leftLightsSignal.emit(1)
            time.sleep(0.5)
            self.leftLightsSignal.emit(2)
            time.sleep(0.5)


############################### EXERCISE 8 #################################
class MyThread_right(QThread):
    rightLightsSignal = pyqtSignal(int)

    def run(self):
        while True:
            self.leftLightsSignal.emit(1)
            time.sleep(0.5)
            self.leftLightsSignal.emit(2)
            time.sleep(0.5)


############################### EXERCISE 10 ################################
class MyThread_unlockCar(QThread):
    unlockCarSignal = pyqtSignal(int)

    def run(self):
        self.unlockCarSignal.emit(3)
        self.unlockCarSignal.emit(1)
        time.sleep(0.5)
        self.unlockCarSignal.emit(0)
        time.sleep(0.5)
        self.unlockCarSignal.emit(1)
        time.sleep(0.5)
        self.unlockCarSignal.emit(0)
        time.sleep(0.1)

        self.unlockCarSignal.emit(2)


############################### EXERCISE 11 ################################
class MyThread_lockCar(QThread):
    lockCarSignal = pyqtSignal(int)

    def run(self):
        self.lockCarSignal.emit(1)
        time.sleep(0.5)
        self.lockCarSignal.emit(2)
        self.lockCarSignal.emit(0)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 500)
        MainWindow.setWindowTitle("Laboratory 1 - Interior Lights")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)

        # Set background application color
        self.centralwidget.setStyleSheet("background-color: white;")

        # Continental image
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 350, 350, 120))
        pixmap = QPixmap("conti.png")
        pixmap = pixmap.scaled(350, 120, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

        # Car image
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(300, 170, 331, 161))
        pixmap1 = QPixmap("car.jpg")
        pixmap1 = pixmap1.scaled(331, 161, QtCore.Qt.KeepAspectRatio)
        self.label_1.setPixmap(pixmap1)

        # Left door button
        self.left_door = QtWidgets.QPushButton(MainWindow)
        self.left_door.setText("Left Door")
        self.left_door.setStyleSheet("font: bold;")
        self.left_door.setGeometry(QtCore.QRect(380, 50, 211, 41))
        self.left_door.clicked.connect(self.open_door_left)

        # Left door slider
        self.left_door_slider = QtWidgets.QSlider(self.centralwidget)
        self.left_door_slider.setGeometry(QtCore.QRect(410, 100, 160, 26))
        self.left_door_slider.setOrientation(QtCore.Qt.Horizontal)
        self.left_door_slider.setRange(0, 100)
        self.left_door_slider.setValue(0)
        self.left_door_slider.valueChanged.connect(self.valuechange_left_slider)

        # Left door spinbox
        self.spinBox_left = QtWidgets.QSpinBox(MainWindow)
        self.spinBox_left.setGeometry(QtCore.QRect(300, 50, 75, 41))
        self.spinBox_left.setKeyboardTracking(False)
        self.spinBox_left.setRange(0, 100)
        self.spinBox_left.valueChanged.connect(self.valuechange)

        # Right door
        self.right_door = QtWidgets.QPushButton(MainWindow)
        self.right_door.setText("Right door")
        self.right_door.setStyleSheet("font: bold;")
        self.right_door.setGeometry(QtCore.QRect(380, 400, 211, 41))
        self.right_door.clicked.connect(self.open_door_right)

        # Right door slider
        self.right_door_slider = QtWidgets.QSlider(self.centralwidget)
        self.right_door_slider.setGeometry(QtCore.QRect(410, 360, 160, 26))
        self.right_door_slider.setOrientation(QtCore.Qt.Horizontal)
        self.right_door_slider.setRange(0, 100)
        self.right_door_slider.setValue(0)
        self.right_door_slider.valueChanged.connect(self.valuechange_right_slider)

        # Right door spinbox
        self.spinBox_right = QtWidgets.QSpinBox(MainWindow)
        self.spinBox_right.setGeometry(QtCore.QRect(300, 400, 75, 41))
        self.spinBox_right.setKeyboardTracking(False)
        self.spinBox_right.setRange(0, 100)
        self.spinBox_right.valueChanged.connect(self.valuechange)

        # Current kl label
        self.current_kl_label = QtWidgets.QLabel(self.centralwidget)
        self.current_kl_label.setGeometry(QtCore.QRect(685, 80, 151, 31))
        self.current_kl_label.setStyleSheet("font: bold;")
        self.current_kl_label.setText("Current KL: no_KL")

        # Previous kl button
        self.prev_kl = QtWidgets.QPushButton(MainWindow)
        self.prev_kl.setText("Previous KL")
        self.prev_kl.setStyleSheet("font: bold;")
        self.prev_kl.setGeometry(QtCore.QRect(680, 40, 101, 31))
        self.prev_kl.clicked.connect(self.prev_kl_function)
        self.prev_kl.setEnabled(False)

        # Prev kl label
        self.prev_kl_label = QtWidgets.QLabel(self.centralwidget)
        self.prev_kl_label.setGeometry(QtCore.QRect(790, 40, 92, 31))
        self.prev_kl_label.setStyleSheet("font: bold;")

        # Next kl button
        self.next_kl = QtWidgets.QPushButton(MainWindow)
        self.next_kl.setText("Next KL")
        self.next_kl.setStyleSheet("font: bold;")
        self.next_kl.setGeometry(QtCore.QRect(680, 120, 101, 31))
        self.next_kl.clicked.connect(self.next_kl_function)

        # Next kl label
        self.next_kl_label = QtWidgets.QLabel(self.centralwidget)
        self.next_kl_label.setGeometry(QtCore.QRect(790, 120, 81, 31))
        self.next_kl_label.setStyleSheet("font: bold;")
        self.next_kl_label.setText("KL_s")

        # green led for interior lights
        self.interiorLightsLabel = QtWidgets.QLabel(self.centralwidget)
        self.interiorLightsLabel.setGeometry(QtCore.QRect(220, 160, 20, 20))

        # inside carLight Button
        self.carLight1 = QtWidgets.QPushButton(MainWindow)
        self.carLight1.setText("Car Light")
        self.carLight1.setStyleSheet("font: bold;")
        self.carLight1.setGeometry(QtCore.QRect(680, 280, 120, 30))
        self.carLight1.clicked.connect(self.carLightSet)

        # inside carLight
        self.carLight = QtWidgets.QLabel(self.centralwidget)
        self.carLight.setGeometry(QtCore.QRect(450, 240, 20, 20))

        # warning Lights Button
        self.warning = QtWidgets.QPushButton(MainWindow)
        self.warning.setText("Warning Lights")
        self.warning.setStyleSheet("font: bold;")
        self.warning.setGeometry(QtCore.QRect(50, 100, 160, 41))
        self.warning.clicked.connect(self.warningLightsButton)

        # left signaling Button
        self.warningLeft = QtWidgets.QPushButton(MainWindow)
        self.warningLeft.setText("Left Signaling")
        self.warningLeft.setStyleSheet("font:bold;")
        self.warningLeft.setGeometry(QtCore.QRect(680, 370, 120, 30))
        self.warningLeft.clicked.connect(self.leftSignaling)

        # right signaling Button
        self.warningRight = QtWidgets.QPushButton(MainWindow)
        self.warningRight.setText("Right Signaling")
        self.warningRight.setStyleSheet("font:bold;")
        self.warningRight.setGeometry(QtCore.QRect(680, 400, 120, 30))
        self.warningRight.clicked.connect(self.rightSignaling)

        # Warning Lights
        self.warningLightLeftRear = QtWidgets.QLabel(self.centralwidget)
        self.warningLightLeftRear.setGeometry(QtCore.QRect(260, 190, 20, 20))

        self.warningLightRightRear = QtWidgets.QLabel(self.centralwidget)
        self.warningLightRightRear.setGeometry(QtCore.QRect(260, 293, 20, 20))

        self.warningLightLeftFront = QtWidgets.QLabel(self.centralwidget)
        self.warningLightLeftFront.setGeometry(QtCore.QRect(650, 190, 20, 20))

        self.warningLightRightFront = QtWidgets.QLabel(self.centralwidget)
        self.warningLightRightFront.setGeometry(QtCore.QRect(650, 293, 20, 20))

        # Lock Car
        self.lockCar1 = QtWidgets.QPushButton(MainWindow)
        self.lockCar1.setText("Lock car")
        self.lockCar1.setStyleSheet("font: bold;")
        self.lockCar1.setGeometry(QtCore.QRect(680, 340, 120, 30))
        self.lockCar1.clicked.connect(self.LockCar)

        # Unlock Car
        self.unlockCar1 = QtWidgets.QPushButton(MainWindow)
        self.unlockCar1.setText("Unlock car")
        self.unlockCar1.setStyleSheet("font: bold;")
        self.unlockCar1.setGeometry(QtCore.QRect(680, 310, 120, 30))
        self.unlockCar1.clicked.connect(self.unlockCar)

        # 4 leds for sweep
        self.led1_sweep = QtWidgets.QLabel(self.centralwidget)
        self.led1_sweep.setGeometry(QtCore.QRect(220, 210, 20, 20))

        self.led2_sweep = QtWidgets.QLabel(self.centralwidget)
        self.led2_sweep.setGeometry(QtCore.QRect(240, 210, 20, 20))

        self.led3_sweep = QtWidgets.QLabel(self.centralwidget)
        self.led3_sweep.setGeometry(QtCore.QRect(260, 210, 20, 20))

        self.led4_sweep = QtWidgets.QLabel(self.centralwidget)
        self.led4_sweep.setGeometry(QtCore.QRect(280, 210, 20, 20))

        # KL_s led
        self.KL_S = QtWidgets.QLabel(self.centralwidget)
        self.KL_S.setGeometry(QtCore.QRect(750, 165, 20, 20))
        # KL_s label
        self.KL_S_label = QtWidgets.QLabel(self.centralwidget)
        self.KL_S_label.setGeometry(QtCore.QRect(700, 165, 40, 20))
        self.KL_S_label.setStyleSheet("font: bold;")
        self.KL_S_label.setText("KL_s")

        # KL_15 led
        self.KL_15 = QtWidgets.QLabel(self.centralwidget)
        self.KL_15.setGeometry(QtCore.QRect(750, 190, 20, 20))
        # KL_15 label
        self.KL_15_label = QtWidgets.QLabel(self.centralwidget)
        self.KL_15_label.setGeometry(QtCore.QRect(700, 190, 40, 20))
        self.KL_15_label.setStyleSheet("font: bold;")
        self.KL_15_label.setText("KL_15")

        # KL_50 led
        self.KL_50 = QtWidgets.QLabel(self.centralwidget)
        self.KL_50.setGeometry(QtCore.QRect(750, 215, 20, 20))
        # KL_50 label
        self.KL_50_label = QtWidgets.QLabel(self.centralwidget)
        self.KL_50_label.setGeometry(QtCore.QRect(700, 215, 40, 20))
        self.KL_50_label.setStyleSheet("font: bold;")
        self.KL_50_label.setText("KL_50")

        # KL_75 led
        self.KL_75 = QtWidgets.QLabel(self.centralwidget)
        self.KL_75.setGeometry(QtCore.QRect(750, 240, 20, 20))
        # KL_75 label
        self.KL_75_label = QtWidgets.QLabel(self.centralwidget)
        self.KL_75_label.setGeometry(QtCore.QRect(700, 240, 40, 20))
        self.KL_75_label.setStyleSheet("font: bold;")
        self.KL_75_label.setText("KL_75")

        # Close all leds button
        self.close_all = QtWidgets.QPushButton(MainWindow)
        self.close_all.setText("Close all leds")
        self.close_all.setStyleSheet("font: bold;color: red")
        self.close_all.setGeometry(QtCore.QRect(50, 50, 120, 35))
        self.close_all.clicked.connect(self.close_all_leds)

        # 1 Led inside
        self.interior_lights = QtWidgets.QPushButton(MainWindow)
        self.interior_lights.setText("Interior lights")
        self.interior_lights.setStyleSheet("font: bold;")
        self.interior_lights.setGeometry(QtCore.QRect(50, 150, 160, 41))
        self.interior_lights.clicked.connect(self.set_interior_lights)

        # Led brightness percentage label
        self.percentage_label = QtWidgets.QLabel(self.centralwidget)
        self.percentage_label.setGeometry(QtCore.QRect(50, 260, 90, 40))
        self.percentage_label.setStyleSheet("font: bold;")
        self.percentage_label.setText("Percentage")

        # Led brightness progress bar
        self.progress_bar = QtWidgets.QProgressBar(MainWindow)
        self.progress_bar.setGeometry(50, 310, 200, 21)
        self.progress_bar.setRange(0, 100)

        # Led brightness spinbox
        self.spinBox = QtWidgets.QSpinBox(MainWindow)
        self.spinBox.setGeometry(QtCore.QRect(150, 260, 75, 41))
        self.spinBox.setKeyboardTracking(False)
        self.spinBox.setRange(0, 100)
        self.spinBox.valueChanged.connect(self.valuechange)

        # Sweep button
        self.sweep = QtWidgets.QPushButton(MainWindow)
        self.sweep.setText("Sweep")
        self.sweep.setStyleSheet("font: bold;")
        self.sweep.setGeometry(QtCore.QRect(50, 200, 160, 41))
        self.sweep.clicked.connect(self.sweep_threads)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        # 6
        self.thread_warning = None

        # 7
        self.thread_warning = None
        self.warning_lights_were_running = False
        self.signal_left_were_running = False
        self.signal_right_were_running = False
        self.thread_left = None
        self.thread_right = None

        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()

    ############################### EXERCISE 1 ###############################
    # Clear all leds and widgtets when the Close all leds is pressed
    def close_all_leds(self):
        self.interior_light_led("#ffffff")
        self.setcarLight("#ffffff")

        self.set_bg_colors("#ffffff", "#ffffff", "#ffffff", "#ffffff")
        self.prev_kl_label.setText("")
        self.current_kl_label.setText("Current KL: no_KL")
        self.next_kl_label.setText("KL_s")
        self.prev_kl.setEnabled(False)
        self.next_kl.setEnabled(True)

        if self.thread_warning is not None:
            self.thread_warning.terminate()
            self.thread_warning = None
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")
        if self.thread_right is not None:
            self.thread_right.terminate()
            self.thread_right = None
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")
        if self.thread_left is not None:
            self.thread_left.terminate()
            self.thread_left = None
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")

    # Open one led when interior lights is pressed
    def interior_light_led(self, b1):
        self.interior_lights_b1 = b1
        self.interiorLightsLabel.setStyleSheet("background-color:" + str(b1) + ";border-radius:5px;")

    # Function called from button handler
    def set_interior_lights(self):
        if (str(self.interiorLightsLabel.palette().window().color().name()) == "#ffffff"):
            self.interior_light_led("green")
        else:
            self.interior_light_led("")

    ############################### EXERCISE 2 ###############################
    # Sweep Leds thread
    def sweep_threads(self):
        self.thread = MyThread_sweep()
        self.thread.sweepLedsSignal.connect(self.sweep_leds)
        self.thread.start()

    # Sweep Leds function
    def sweep_leds(self, val):
        if val == 1:
            self.set4leds("grey", "#ffffff", "#ffffff", "#ffffff")
        elif val == 2:
            self.set4leds("#ffffff", "green", "#ffffff", "#ffffff")
        elif val == 3:
            self.set4leds("#ffffff", "#ffffff", "red", "#ffffff")
        elif val == 4:
            self.set4leds("#ffffff", "#ffffff", "#ffffff", "blue")
        elif val == 5:
            self.set4leds("#ffffff", "#ffffff", "#ffffff", "#ffffff")

    # Sweep Leds
    def set4leds(self, led1, led2, led3, led4):
        self.led1_sweep.setStyleSheet("background-color:" + str(led1) + ";border-radius:5px;")
        self.led2_sweep.setStyleSheet("background-color:" + str(led2) + ";border-radius:5px;")
        self.led3_sweep.setStyleSheet("background-color:" + str(led3) + ";border-radius:5px;")
        self.led4_sweep.setStyleSheet("background-color:" + str(led4) + ";border-radius:5px;")

    ############################### EXERCISE 3 ###############################
    # Change progress bar value when spinbox value is changed
    def valuechange(self):
        if self.progress_bar.value() > self.spinBox.value():
            self.change_pb_down_value(self.spinBox.value())
        else:
            self.change_pb_up_value(self.spinBox.value())

    # Change led brightness down when the spinbox value (representing led brightness percentage) is less than progress bar value
    def change_pb_down_value(self, value):
        for i in range(self.progress_bar.value(), value - 1, -1):
            self.progress_bar.setValue(i)
            time.sleep(0.15)

    # Change led brightness up when the spinbox value (representing led brightness percentage) is bigger than progress bar value
    def change_pb_up_value(self, value):
        for i in range(self.progress_bar.value(), value + 1):
            self.progress_bar.setValue(i)
            time.sleep(0.15)

    ############################### EXERCISE 4 ###############################
    # Succesive KL led turn
    def KL_lights(self, KL):
        if KL == "":
            self.set_bg_colors("grey", "green", "red", "blue")
        elif KL == "KL_s":
            self.set_bg_colors("#ffffff", "#ffffff", "#ffffff", "#ffffff")
        elif KL == "KL_15":
            self.set_bg_colors("grey", "#ffffff", "#ffffff", "#ffffff")
        elif KL == "KL_50":
            self.set_bg_colors("grey", "green", "#ffffff", "#ffffff")
        elif KL == "KL_75":
            self.set_bg_colors("grey", "green", "red", "#ffffff")
        else:
            self.set_bg_colors("grey", "green", "red", "blue")

    # Set previous value for KL when previous KL button is pressed
    def prev_kl_function(self):
        if self.next_kl_label.text() == "KL_s":
            self.KL_lights(self.next_kl_label.text())
        if self.next_kl_label.text() == "KL_15":
            self.current_kl_label.setText("Current KL: no_KL")
            self.next_kl_label.setText("KL_s")
            self.prev_kl_label.setText("")
            self.KL_lights(self.next_kl_label.text())
        elif self.next_kl_label.text() == "KL_50":
            self.current_kl_label.setText("Current KL: KL_s")
            self.next_kl_label.setText("KL_15")
            self.prev_kl_label.setText("no_KL")
            self.KL_lights(self.next_kl_label.text())
        elif self.next_kl_label.text() == "KL_75":
            self.current_kl_label.setText("Current KL: KL_15")
            self.next_kl_label.setText("KL_50")
            self.prev_kl_label.setText("KL_s")
            self.KL_lights(self.next_kl_label.text())
        elif self.next_kl_label.text() == "":
            self.current_kl_label.setText("Current KL: KL_50")
            self.next_kl_label.setText("KL_75")
            self.prev_kl_label.setText("KL_15")
            self.KL_lights(self.next_kl_label.text())

        self.set_enable()

    # Set next value for KL when next KL button is pressed
    def next_kl_function(self):
        if self.next_kl_label.text() == "KL_s":
            self.current_kl_label.setText("Current KL: KL_s")
            self.next_kl_label.setText("KL_15")
            self.prev_kl_label.setText("no_KL")
            self.KL_lights(self.next_kl_label.text())
        elif self.next_kl_label.text() == "KL_15":
            self.current_kl_label.setText("Current KL: KL_15")
            self.next_kl_label.setText("KL_50")
            self.prev_kl_label.setText("KL_s")
            self.KL_lights(self.next_kl_label.text())
        elif self.next_kl_label.text() == "KL_50":
            self.current_kl_label.setText("Current KL: KL_50")
            self.next_kl_label.setText("KL_75")
            self.prev_kl_label.setText("KL_15")
            self.KL_lights(self.next_kl_label.text())
        elif self.next_kl_label.text() == "KL_75":
            self.current_kl_label.setText("Current KL: KL_75")
            self.next_kl_label.setText("")
            self.prev_kl_label.setText("KL_50")
            self.KL_lights(self.next_kl_label.text())

        self.set_enable()

    # Set enable KL buttons
    def set_enable(self):
        if self.next_kl_label.text() == "KL_s":
            self.prev_kl.setEnabled(False)
            self.next_kl.setEnabled(True)
        elif self.next_kl_label.text() != "KL_s" and self.next_kl_label.text() != "":
            self.prev_kl.setEnabled(True)
            self.next_kl.setEnabled(True)
        else:
            self.prev_kl.setEnabled(True)
            self.next_kl.setEnabled(False)

    # Set KL leds colors
    def set_bg_colors(self, l1, l2, l3, l4):
        self.KL_S.setStyleSheet("background-color:" + str(l1) + ";border-radius:5px;")
        self.KL_15.setStyleSheet("background-color:" + str(l2) + ";border-radius:5px;")
        self.KL_50.setStyleSheet("background-color:" + str(l3) + ";border-radius:5px;")
        self.KL_75.setStyleSheet("background-color:" + str(l4) + ";border-radius:5px;")

    ############################### EXERCISE 5 ##############################
    ################################ BONUS ################################
    # Open left door untill the obstacle is detected
    def open_door_left(self):
        self.left_door_slider.setValue(self.spinBox_left.value())

    # This function will stop the slider to go to values bigger than the obstacle
    def valuechange_left_slider(self):
        if self.left_door_slider.value() > self.spinBox_left.value():
            self.left_door_slider.setValue(self.spinBox_left.value())
            self.left_door_slider.setStyleSheet("background-color:red")
        else:
            self.left_door_slider.setStyleSheet("background-color:#ffffff")

    # Open right door untill the obstacle is detected
    def open_door_right(self):
        self.right_door_slider.setValue(self.spinBox_right.value())

    # This function will stop the slider to go to values bigger than the obstacle
    def valuechange_right_slider(self):
        if self.right_door_slider.value() > self.spinBox_right.value():
            self.right_door_slider.setValue(self.spinBox_right.value())
            self.right_door_slider.setStyleSheet("background-color:red")
        else:
            self.right_door_slider.setStyleSheet("background-color:#ffffff")

    #########################################################################
    ############################### USED FUNCTION ###########################
    def setWarningLights(self, warningLightLeftRear, warningLightRightRear, warningLightLeftFront,
                         warningLightRightFront):
        self.warningLightLeftRear.setStyleSheet("background-color:" + str(warningLightLeftRear) + ";border-radius:5px;")
        self.warningLightRightRear.setStyleSheet(
            "background-color:" + str(warningLightRightRear) + ";border-radius:5px;")
        self.warningLightLeftFront.setStyleSheet(
            "background-color:" + str(warningLightLeftFront) + ";border-radius:5px;")
        self.warningLightRightFront.setStyleSheet(
            "background-color:" + str(warningLightRightFront) + ";border-radius:5px;")

    #########################################################################

    ############################### EXERCISE 6 ##############################
    # Warning lights thread
    def warningLightsButton(self):
        if self.thread_warning is None:
            self.thread_warning = MyThread_warning()
            self.thread_warning.warningLightsSignal.connect(self.warningLighs)
            self.thread_warning.start()

            if self.thread_left is not None:
                self.signal_left_were_running = True
                self.thread_left.terminate()
                self.thread_left = None
            if self.thread_right is not None:
                self.signal_right_were_running = True
                self.thread_right.terminate()
                self.thread_right = None
        else:
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")

            if self.signal_left_were_running == True:
                self.thread_left = MyThread_left()
                self.thread_left.leftLightsSignal.connect(self.whileLeft)
                self.thread_left.start()
            if self.signal_right_were_running == True:
                self.thread_right = MyThread_left()
                self.thread_right.leftLightsSignal.connect(self.whileRight)
                self.thread_right.start()

            self.thread_warning.terminate()
            self.thread_warning = None

    # Warning Lights function
    def warningLighs(self, val):
        if val == 1:
            self.setWarningLights("orange", "orange", "orange", "orange")
        elif val == 2:
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")

    ############################### EXERCISE 7 ##############################
    # Left Signaling Lights
    def leftSignaling(self):
        if self.thread_left is None:
            self.thread_left = MyThread_left()
            self.thread_left.leftLightsSignal.connect(self.whileLeft)
            self.thread_left.start()

            self.signal_left_were_running = True
            self.signal_right_were_running = False

            if self.thread_warning is not None:
                self.warning_lights_were_running = True
                self.thread_warning.terminate()
                self.thread_warning = None
            if self.thread_right is not None:
                self.thread_right.terminate()
                self.thread_right = None
        else:
            self.thread_left.terminate()
            self.thread_left = None
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")
            self.signal_left_were_running = False
            if self.warning_lights_were_running == True:
                self.thread_warning = MyThread_warning()
                self.thread_warning.warningLightsSignal.connect(self.warningLighs)
                self.thread_warning.start()

    def whileLeft(self, val):
        if val == 1:
            self.setWarningLights("orange", "#ffffff", "orange", "#ffffff")
        else:
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")

    ############################### EXERCISE 8 ##############################
    # Right Signaling Lights
    def rightSignaling(self):
        if self.thread_right is None:
            self.thread_right = MyThread_left()
            self.thread_right.leftLightsSignal.connect(self.whileRight)
            self.thread_right.start()

            self.signal_right_were_running = True
            self.signal_left_were_running = False

            if self.thread_warning is not None:
                self.warning_lights_were_running = True
                self.thread_warning.terminate()
                self.thread_warning = None
            if self.thread_left is not None:
                self.thread_left.terminate()
                self.thread_left = None

        else:
            self.thread_right.terminate()
            self.thread_right = None
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")
            self.signal_right_were_running = False
            if self.warning_lights_were_running == True:
                self.thread_warning = MyThread_warning()
                self.thread_warning.warningLightsSignal.connect(self.warningLighs)
                self.thread_warning.start()

    def whileRight(self, val):
        if val == 1:
            self.setWarningLights("#ffffff", "orange", "#ffffff", "orange")
        else:
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")

    ######################### Car Light - usefull for next ex ################
    def setcarLight(self, color):
        self.carLight.setStyleSheet("background-color:" + str(color) + ";border-radius:5px;")

    # Open and close the interior light
    def carLightSet(self):
        if (str(self.carLight.palette().window().color().name()) == "#ffffff"):
            self.setcarLight("green")
        else:
            self.setcarLight("")

    ############################### EXERCISE 9 ##############################
    # Unlock car
    def unlockCar(self):
        self.thread_unlockCar = MyThread_unlockCar()
        self.thread_unlockCar.unlockCarSignal.connect(self.UnlockCarThread)
        self.thread_unlockCar.start()

    def UnlockCarThread(self, val):
        if val == 0:
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")
        elif val == 1:
            self.setWarningLights("orange", "orange", "orange", "orange")
        elif val == 2:
            self.setcarLight("")
        elif val == 3:
            self.setcarLight("green")

    ############################### EXERCISE 10 ##############################
    # Lock the car
    def LockCar(self):
        self.thread_lockCar = MyThread_lockCar()
        self.thread_lockCar.lockCarSignal.connect(self.LockCarThread)
        self.thread_lockCar.start()

    def LockCarThread(self, val):
        if val == 0:
            self.setWarningLights("#ffffff", "#ffffff", "#ffffff", "#ffffff")
        elif val == 1:
            self.setWarningLights("orange", "orange", "orange", "orange")
        elif val == 2:
            self.setcarLight("")
        elif val == 3:
            self.setcarLight("green")


class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self,
                                                "Confirm Exit",
                                                "Are you sure you want to exit ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()

        elif result == QtWidgets.QMessageBox.No:
            event.ignore()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.center()
    sys.exit(app.exec_())
