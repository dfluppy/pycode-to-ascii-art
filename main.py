from src.pycode_to_ascii import PyCodeTOAscii
from src.GUI import Ui_MainWindow
from src.gui_finctions import UI
from PySide6.QtWidgets import QApplication, QMainWindow

# main = PyCodeTOAscii()
#
# print(main.generate_ascii_art(img='ciri.jpg', scale=70))



if __name__ == '__main__':
    app = QApplication([])
    win = UI()


    win.show()
    app.exec()


