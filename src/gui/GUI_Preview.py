# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)


class Ui_MainWindow_Preview(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.preview_image = QGraphicsView(self.centralwidget)
        self.preview_image.setObjectName(u"preview_image")

        self.verticalLayout.addWidget(self.preview_image)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_slider = QLabel(self.centralwidget)
        self.label_slider.setObjectName(u"label_slider")
        font = QFont()
        font.setPointSize(12)
        self.label_slider.setFont(font)

        self.verticalLayout.addWidget(self.label_slider)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.threshold_slider = QSlider(self.centralwidget)
        self.threshold_slider.setObjectName(u"threshold_slider")
        self.threshold_slider.setMaximum(255)
        self.threshold_slider.setTracking(True)
        self.threshold_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.threshold_slider)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.value_label = QLabel(self.centralwidget)
        self.value_label.setObjectName(u"value_label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.value_label.setFont(font1)

        self.verticalLayout.addWidget(self.value_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.width_label = QLabel(self.centralwidget)
        self.width_label.setObjectName(u"width_label")
        self.width_label.setFont(font)

        self.verticalLayout.addWidget(self.width_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.height_label = QLabel(self.centralwidget)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setFont(font)

        self.verticalLayout.addWidget(self.height_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")

        self.verticalLayout.addWidget(self.save_button, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Prepare Image", None))
        self.label_slider.setText(QCoreApplication.translate("MainWindow", u"Choose a suitable threshold value for the image", None))
        self.value_label.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.width_label.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

