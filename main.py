from src.gui_finctions import UI
from PySide6.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication([])
    win = UI()


    win.show()
    app.exec()


