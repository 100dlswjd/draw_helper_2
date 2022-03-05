import sys
import time
import keyboard_tool
import win32api
import win32con

from threading import Thread, Event
from PySide6.QtWidgets import QApplication, QMainWindow
from main_form import Ui_MainWindow

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self._width = "0"
        self._height = "0"
        self._range = "0"
        self.btn_ok.clicked.connect(self.btn_ok_handler)
        self.lineEdit_width.textChanged.connect(self.lineEdit_width_handler)
        self.lineEdit_height.textChanged.connect(self.lineEdit_height_handler)
        self.lineEdit_range.textChanged.connect(self.lineEdit_range_handler)
        self.main_thread = Thread(target = self.thread_proc)
        self.exit_event = Event()
        self.main_thread.start()
    """
    반복문 (높이/ 간격)
        반복문 (너비/ 간격)
            알트 누르고 찍고
            알트 떼고
            찍고
            간격만큼 + 이동
        간격 만큼 + 이동
    """
    def thread_proc(self):
        while self.exit_event.is_set() == False:
            if win32api.GetAsyncKeyState(win32con.VK_F10) & 0x8000:
                time.sleep(.25)
                print("F10 눌름 ! 쓰레드시작 !")
                Pos = win32api.GetCursorPos()
                temPos = [Pos[0], Pos[1]]
                for height in range(int(int(self._height)/int(self._range))):
                    for width in range(int(int(self._width)/int(self._range))):
                        keyboard_tool.pressAndHold("alt")
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, temPos[0], temPos[1], 0, 0)
                        time.sleep(.1)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, temPos[0], temPos[1], 0, 0)
                        keyboard_tool.release("alt")
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, temPos[0], temPos[1], 0, 0)
                        time.sleep(.05)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, temPos[0], temPos[1], 0, 0)
                        temPos[0] = temPos[0] + int(self._range)
                        movePos = (temPos[0], temPos[1])
                        win32api.SetCursorPos(movePos)
                    temPos[0] = Pos[0]
                    temPos[1] = temPos[1] + int(self._range)
                    movePos = (temPos[0], temPos[1])
                    win32api.SetCursorPos(movePos)
                win32api.SetCursorPos(Pos)
                

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
        
        if self._range.isdigit():
            text += "간격 : " + self._range + "\n"
            self._range = int(self._range)
        else:
            text += "간격을 잘못 입력 했습니다.\n"

        self.label_set_info.setText(text)
        
    def lineEdit_range_handler(self, text):
        self._range = text

    def lineEdit_width_handler(self, text):
        self._width = text

    def lineEdit_height_handler(self, text):
        self._height = text
    
    def closeEvent(self, event) -> None:
        self.exit_event.set()
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()
