from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap

from src.pycode_to_ascii import PyCodeTOAscii
from src.gui.GUI import Ui_MainWindow
from src.gui.GUI_Preview import Ui_MainWindow_Preview
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication, QGraphicsScene, QGraphicsPixmapItem
import cv2


class UI(QMainWindow):
    BINARY_DATA = None

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


    def pyCodeState(self, state: int) -> None:
        """
        Вкл/выкл редактор кода
        :param state: состояние [0 - False / 2 - True]
        :return: None
        """
        if state == 2:
            self.ui.pycode_edit.setEnabled(True)
        else:
            self.ui.pycode_edit.setEnabled(False)


    def showFileDialog(self) -> None:
        """
        Метод для открытия проводника, выбора файла
        :return:
        """
        img_path, _ = QFileDialog.getOpenFileNames(self, 'Проводник', '', 'Images (*.jpg *.png)')

        if len(img_path) > 0:
            self.img = img_path[0]

            img_info = cv2.imread(self.img)
            height, width, _ = img_info.shape

            self.win_preview = UIPreview()
            self.win_preview.show()
            UIPreview.IMG_PATH = self.img
            self.win_preview.setSceneImage(value_treshold=0)

            self.ui.width_lineedit.setPlaceholderText(f'Width ({width})')
            self.ui.height_lineedit.setPlaceholderText(f'Height ({height})')


    def getAllParametrsForm(self) -> tuple:
        """
        Метод для возврата всех указанных параметров юзера
        :return: кортеж значений
        """
        return (
                self.ui.ascii_chars_lineedit.text() or None,
                self.ui.scale_lineedit.text().strip() or None,
                self.ui.width_lineedit.text().strip() or None,
                self.ui.height_lineedit.text().strip() or None,
                self.ui.invert_checkbox.isChecked(),
                self.ui.add_exec_checkbox.isChecked(),
                self.ui.pycode_edit.toPlainText().strip() or None,
        )

    def generateArtButton(self) -> None:
        """
        Вызов функции генерации ASCII арта, получение результата и отображения в текстовом поле
        :return:
        """
        if self.img:
            pycodetoascii = PyCodeTOAscii(self.img, *self.getAllParametrsForm(), threshold=0)

            res = pycodetoascii.generate_ascii_art(self.BINARY_DATA)
            self.ui.textEdit.setText(res)
        else:
            error_msg = QMessageBox()
            error_msg.setText('Выберите путь к изображению')
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.exec()
            self.showFileDialog()

    def copyClipBoard(self) -> None:
        """
        Метод для копирования арта в буфер обмена
        :return:
        """
        copy_clipboard = QApplication.clipboard()
        copy_clipboard.setText(self.ui.textEdit.toPlainText())
        self.showNotificationCopy()

    def showNotificationCopy(self) -> None:
        """
        Уведомление об успешном копировании в буфер обмена
        :return:
        """
        self.ui.notification_label.setText('Copied!')
        self.ui.notification_label.adjustSize()
        self.ui.notification_label.move(
            (self.width() - self.ui.notification_label.width()) // 2,
            (self.height() - self.ui.notification_label.height()) // 2
        )
        self.ui.notification_label.show()

        QTimer.singleShot(1250, self.ui.notification_label.hide)


class UIPreview(QMainWindow):
    """
    Отображение окна предобработки изображения
    """
    IMG_PATH = None

    def __init__(self):
        super().__init__()
        self.ui_preview = Ui_MainWindow_Preview()
        self.ui_preview.setupUi(self)

        self.handlersButtonPreview()
        self.ui_preview.threshold_slider.valueChanged.connect(self.sliderEvent)

    def handlersButtonPreview(self) -> None:
        """
        Обработчик вызова методов для кнопок
        :return:
        """
        self.ui_preview.save_button.clicked.connect(self.saveButton)

    def sliderEvent(self, value: int) -> None:
        """
        Метод для регулировки значения слайдера
        :param value: значение слайдера
        :return:
        """
        self.setSceneImage(value)
        self.ui_preview.value_label.setText(str(value))

    def setSceneImage(self, value_treshold: int) -> None:
        """
        Рендеринг изображения в окне
        :param value_treshold: значение слайдера
        :return:
        """
        image = cv2.imread(self.IMG_PATH)

        width, height, _ = image.shape
        self.ui_preview.width_label.setText(f'Width: {width}')
        self.ui_preview.height_label.setText(f'Height: {height}')

        graphics_scene = QGraphicsScene(self)
        prepare_image = self.convertCVtoQImageTreshold(image, value_treshold)
        pixmap = QPixmap(prepare_image)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        graphics_scene.addItem(pixmap_item)
        self.ui_preview.preview_image.setScene(graphics_scene)

    def convertCVtoQImageTreshold(self, cv_image, value_treshold: int, save=False) -> QImage:
        """
        Конвертация изображения cv2 -> QImage, получение массива данных о пороговой настройке
        :param cv_image: изображение
        :param value_treshold: значение слайдера
        :param save: булевое значение (при сохранение возвращается только массив со значениями пикселей)
        :return: объект QImage или массив пикселей
        """
        height, width, _ = cv_image.shape
        gray_img = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        ret, binary_image = cv2.threshold(gray_img, value_treshold, 255, cv2.THRESH_BINARY)

        q_image = QImage(binary_image.data, width, height, width, QImage.Format_Grayscale8)

        return binary_image if save else q_image

    def saveButton(self) -> None:
        """
        Сохранение настроек подготовленного изображения
        :return:
        """
        image = cv2.imread(self.IMG_PATH)
        value = self.ui_preview.value_label.text()
        UI.BINARY_DATA = self.convertCVtoQImageTreshold(image, int(value), save=True)
        self.close()




