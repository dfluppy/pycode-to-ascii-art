from src.pycode_to_ascii import PyCodeTOAscii
from src.GUI import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.img: str = ''
        self.handlersButton()


    def handlersButton(self) -> None:
        """
        Обработчик для кнопок
        :return: None
        """
        self.ui.select_image_button.clicked.connect(self.showFileDialog)
        self.ui.generate_art_button.clicked.connect(self.generateArtButton)
        self.ui.add_exec_checkbox.stateChanged.connect(self.pyCodeState)
        self.ui.copy_art_button.clicked.connect(self.copyClipBoard)


    def pyCodeState(self, state):
        if state == 2:
            self.ui.pycode_edit.setEnabled(True)
        else:
            self.ui.pycode_edit.setEnabled(False)


    def showFileDialog(self) -> None:
        img_path, _ = QFileDialog.getOpenFileNames(self, 'Проводник', '', 'Images (*.jpg *.png)')

        if len(img_path) > 0:
            self.img = img_path[0]


    def getAllParametrsForm(self) -> tuple:
        return (
                self.ui.ascii_chars_lineedit.text() or None,
                self.ui.scale_lineedit.text().strip() or None,
                self.ui.width_lineedit.text().strip() or None,
                self.ui.height_lineedit.text().strip() or None,
                self.ui.invert_checkbox.isChecked(),
                self.ui.add_exec_checkbox.isChecked(),
                self.ui.pycode_edit.toPlainText().strip() or None,
        )


    def generateArtButton(self):
        if self.img:
            pycodetoascii = PyCodeTOAscii(self.img, *self.getAllParametrsForm())
            res = pycodetoascii.generate_ascii_art()
            self.ui.textEdit.setText(res)
        else:
            error_msg = QMessageBox()
            error_msg.setText('Выберите путь к изображению')
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.exec()
            self.showFileDialog()

    def copyClipBoard(self):
        copy_clipboard = QApplication.clipboard()
        copy_clipboard.setText(self.ui.textEdit.toPlainText())



