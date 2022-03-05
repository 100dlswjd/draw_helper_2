import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from main_form import Ui_MainWindow

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self._width = 0
        self._height = 0
        self.btn_ok.clicked.connect(self.btn_ok_handler)
        self.lineEdit_width.textChanged.connect(self.lineEdit_width_handler)
        self.lineEdit_height.textChanged.connect(self.lineEdit_height_handler)

    def btn_ok_handler(self):
        self.label_set_info.setText("")
        text = ""        
        if self._width.isdigit():
            text += "너비 : " + self._width + "\n"
            self._width = int(self._width)
        else:
            text += "너비를 잘못 입력 했습니다.\n"

        if self._height.isdigit():
            text += "높이 : " + self._height + "\n"
            self._height = int(self._height)
        else:
            text += "높이를 잘못 입력 했습니다.\n"

        self.label_set_info.setText(text)
        

    def lineEdit_width_handler(self, text):
        self._width = text

    def lineEdit_height_handler(self, text):
        self._height = text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()
