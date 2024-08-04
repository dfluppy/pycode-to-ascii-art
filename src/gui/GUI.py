# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QCursor, QFont, QIntValidator)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.select_image_button = QPushButton(self.centralwidget)
        self.select_image_button.setObjectName(u"select_image_button")

        self.verticalLayout.addWidget(self.select_image_button)

        self.onlyInt = QIntValidator()  # маска только на числа


        self.scale_lineedit = QLineEdit(self.centralwidget)
        self.scale_lineedit.setObjectName(u"scale_lineedit")
        self.scale_lineedit.setValidator(QIntValidator(1, 100, self.scale_lineedit))
        self.scale_lineedit.setMaxLength(3)

        self.verticalLayout.addWidget(self.scale_lineedit)

        self.width_lineedit = QLineEdit(self.centralwidget)
        self.width_lineedit.setObjectName(u"width_lineedit")
        self.width_lineedit.setValidator(self.onlyInt)
        self.width_lineedit.setMaxLength(3)

        self.verticalLayout.addWidget(self.width_lineedit)

        self.height_lineedit = QLineEdit(self.centralwidget)
        self.height_lineedit.setObjectName(u"height_lineedit")
        self.height_lineedit.setValidator(self.onlyInt)
        self.height_lineedit.setMaxLength(3)

        self.verticalLayout.addWidget(self.height_lineedit)

        self.ascii_chars_lineedit = QLineEdit(self.centralwidget)
        self.ascii_chars_lineedit.setObjectName(u"ascii_chars_lineedit")

        self.verticalLayout.addWidget(self.ascii_chars_lineedit)

        self.convert_4bit_checkbox = QCheckBox(self.centralwidget)
        self.convert_4bit_checkbox.setObjectName(u"convert_4bit_checkbox")
        self.convert_4bit_checkbox.setEnabled(False)

        self.verticalLayout.addWidget(self.convert_4bit_checkbox)

        self.invert_checkbox = QCheckBox(self.centralwidget)
        self.invert_checkbox.setObjectName(u"invert_checkbox")

        self.verticalLayout.addWidget(self.invert_checkbox)

        self.add_exec_checkbox = QCheckBox(self.centralwidget)
        self.add_exec_checkbox.setObjectName(u"add_exec_checkbox")

        self.verticalLayout.addWidget(self.add_exec_checkbox)

        self.generate_art_button = QPushButton(self.centralwidget)
        self.generate_art_button.setObjectName(u"generate_art_button")

        self.verticalLayout.addWidget(self.generate_art_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.help_label = QLabel(self.centralwidget)
        self.help_label.setObjectName(u"help_label")
        self.help_label.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.help_label.setMouseTracking(False)

        self.verticalLayout.addWidget(self.help_label)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.pycode_edit = QTextEdit(self.splitter)
        self.pycode_edit.setObjectName(u"pycode_edit")
        self.pycode_edit.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pycode_edit.sizePolicy().hasHeightForWidth())
        self.pycode_edit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.pycode_edit.setFont(font)
        self.splitter.addWidget(self.pycode_edit)
        self.textEdit = QTextEdit(self.splitter)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Courier"])
        self.textEdit.setFont(font1)
        self.textEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.textEdit.setReadOnly(True)
        self.splitter.addWidget(self.textEdit)

        self.verticalLayout_2.addWidget(self.splitter)

        self.copy_art_button = QPushButton(self.centralwidget)
        self.copy_art_button.setObjectName(u"copy_art_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.copy_art_button.sizePolicy().hasHeightForWidth())
        self.copy_art_button.setSizePolicy(sizePolicy2)
        self.copy_art_button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.verticalLayout_2.addWidget(self.copy_art_button, 0, Qt.AlignmentFlag.AlignRight)

        self.notification_label = QLabel(self.centralwidget)
        self.notification_label.setFont(QFont("Arial", 10))
        self.notification_label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 128); padding: 10px; border-radius: 10px;")
        self.notification_label.hide()


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.formLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ASCII art", None))
        self.select_image_button.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.scale_lineedit.setText("")
        self.scale_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scale (optional)", None))
        self.width_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Width (optional)", None))
        self.height_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Height (optional)", None))
        self.ascii_chars_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ASCII chars (optional)", None))
        self.convert_4bit_checkbox.setText(QCoreApplication.translate("MainWindow", u"Convert 4 bit (soon)", None))
        self.invert_checkbox.setText(QCoreApplication.translate("MainWindow", u"Invert", None))
        self.add_exec_checkbox.setText(QCoreApplication.translate("MainWindow", u"Add exec", None))
        self.generate_art_button.setText(QCoreApplication.translate("MainWindow", u"Generate Art", None))
#if QT_CONFIG(tooltip)
        self.help_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">[1] Select Image</span>:   Click the button and specify the path to the image.</p><p><span style=\" font-weight:700;\">[2] Scale:</span>   Specify the size of the ASCII art <span style=\" font-style:italic;\">(optional).</span></p><p><span style=\" font-weight:700;\">[3] Width:</span>   Specify image width <span style=\" font-style:italic;\">(optional).</span></p><p><span style=\" font-weight:700;\">[4] Height:   </span>Specify the image height (optional).</p><p><span style=\" font-weight:700;\">[5] ASCII chars: </span>  You can specify your own acceptable characters.</p><p><span style=\" font-style:italic;\">Note:</span> specify characters in ascending or descending order of their brightness factor (example: `@#%/,.` where `@` is 255 and `.` is 5)</p><p><span style=\" font-weight:700;\">[6] Convert 4 bit:</span>   You can convert the color depth of your image up to 4 bits.</p><p><span style=\" font-weight:700;\">[7] Invert: </span>  Inverting ASCII chars"
                        " for art.</p><p><span style=\" font-weight:700;\">[8] Add exec: </span>  You can write your python code in a special text field and add it to your art.</p><p><span style=\" font-weight:700;\">[9] Generate: </span>  Button to generate your ASCII art</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.help_label.setText(QCoreApplication.translate("MainWindow", u"(?) Help ", None))
        self.pycode_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write your python code", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"To display the result, generate ASCII art", None))
        self.copy_art_button.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.ascii_chars_lineedit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body>ASCII chars (optional)</body></html>", None))
    # retranslateUi

