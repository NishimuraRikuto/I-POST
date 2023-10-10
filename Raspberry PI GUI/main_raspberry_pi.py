import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QGridLayout,
)
from msg_manager import get_message, send_message
import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = InboxWindow()
        self.window2 = OutboxWindow()

        l = QVBoxLayout()
        pixmap = QPixmap("I-POST_logo.png")
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        l.addWidget(image_label)

        w = QWidget()
        self.setWindowFlag(Qt.FramelessWindowHint)
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window1, window2):
        if window1.isVisible():
            window1.hide()
        else:
            window1.showMaximized()
            window2.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_I:
            if self.window1.isVisible():
                self.window1.hide()
            else:
                self.window1.showMaximized()
                self.window2.hide()
#Qt.Key_O には紙センサー
        elif event.key() == Qt.Key_O:
            self.toggle_window(window1=self.window2, window2=self.window1)
class OutboxWindow(QWidget):
    I_POST_SERVER = "https://ipost-server-eh2trxntfa-an.a.run.app/"
    def __init__(self):
        super().__init__()
        self.id = "Tulgaa"
        palette = QPalette()
        nav_font = QFont("Times", 40, QFont.Bold)
        msg_font = QFont("Times", 15)

        outbox_text = QLabel()
        outbox_text.setText("Outbox")
        outbox_text.setFixedHeight(100)
        outbox_text.adjustSize()
        outbox_text.setFont(nav_font)
        outbox_text.setStyleSheet("border-radius: 25px; ")
        outbox_text.setAlignment(Qt.AlignCenter)

        self.direction = QLabel()
        self.direction.setText("宛先を選択してください")
        self.direction.setFixedHeight(100)
        self.direction.adjustSize()
        self.direction.setFont(nav_font)
        self.direction.setStyleSheet("background-color: white; border-radius: 25px; ")
        self.direction.setAlignment(Qt.AlignCenter)

        id_1 = QLabel()
        id_1.setText("一郎")
        id_1.setFixedSize(100, 70)
        id_1.adjustSize()
        id_1.setFont(msg_font)
        id_1.setStyleSheet("background-color: white; border-radius: 25px; ")
        id_1.setAlignment(Qt.AlignCenter)

        id_2 = QLabel()
        id_2.setText("二郎")
        id_2.setFixedSize(100, 70)
        id_2.adjustSize()
        id_2.setFont(msg_font)
        id_2.setStyleSheet("background-color: white; border-radius: 25px; ")
        id_2.setAlignment(Qt.AlignCenter)

        id_3 = QLabel()
        id_3.setText("三郎")
        id_3.setFixedSize(100, 70)
        id_3.adjustSize()
        id_3.setFont(msg_font)
        id_3.setStyleSheet("background-color: white; border-radius: 25px; ")
        id_3.setAlignment(Qt.AlignCenter)

        layout = QGridLayout()
        layout.addWidget(outbox_text, 0,0,1,3)
        layout.addWidget(self.direction,1,0,1,3)
        layout.addWidget(id_1,2,0)
        layout.addWidget(id_2,2,1)
        layout.addWidget(id_3,2,2)

        self.setWindowTitle("I-POST")
        self.setAutoFillBackground(True)
        self.setLayout(layout)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setFixedSize(1024, 600)
        palette.setColor(QPalette.Window, QColor("#f2635f"))
        self.setPalette(palette)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.id = "id_1"
            send_message(self.id)
            self.direction.setText(f"{self.id}へ送りました。")
            time.sleep(5)
            self.hide()
        elif event.key() == Qt.Key_2:
            self.id = "id_2"
            send_message(self.id)
            self.direction.setText(f"{self.id}へ送りました。")
            time.sleep(5)
            self.hide()
        elif event.key() == Qt.Key_3:
            self.id = "id_3"
            send_message(self.id)
            self.direction.setText( self.id + "へ送りました。")
            time.sleep(5)
            self.hide()


class InboxWindow(QWidget):
    I_POST_SERVER = "https://ipost-server-eh2trxntfa-an.a.run.app/"
    def __init__(self):
        super().__init__()

        self.data = get_message()
        self.msg_number = 2
        palette = QPalette()
        nav_font = QFont("Times", 40, QFont.Bold)
        time_font = QFont("Times", 10, QFont.Bold)
        name_font = QFont("Times", 30)
        msg_font = QFont("Times", 15)
        # Inbox
        nav = QLabel("Inbox", self)
        self.name = QLabel("Tulgaa", self)
        self.msg = QLabel("A Message", self)
        self.received_time = QLabel("2023:12:00", self)

        nav.setFixedHeight(100)
        nav.adjustSize()
        nav.setFont(nav_font)
        nav.setStyleSheet("border-radius: 25px; ")
        nav.setAlignment(Qt.AlignCenter)

        self.received_time.setFixedWidth(120)
        self.received_time.setFixedHeight(100)
        self.received_time.setFont(time_font)
        self.received_time.setStyleSheet("background-color: white; border-radius: 25px;")
        self.received_time.setWordWrap(True)
        self.received_time.setAlignment(Qt.AlignCenter)

        self.name.setFixedHeight(90)
        self.name.setFont(name_font)
        self.name.setStyleSheet("background-color: white; border-radius: 25px; padding: 0, 5, 0, 10")
        self.name.setAlignment(Qt.AlignLeft)

        self.msg.setFixedHeight(300)
        self.msg.setFont(msg_font)
        self.msg.setStyleSheet("background-color: white; border-radius: 25px; padding: 10, 20, 20, 20")
        self.msg.setWordWrap(True)
        self.msg.setAlignment(Qt.AlignLeft)

        layout = QGridLayout()
        layout.addWidget(nav, 0, 0, 1, 5)
        layout.addWidget(self.name, 1, 1, 1, 1)
        layout.addWidget(self.received_time, 1, 3)
        layout.addWidget(self.msg, 2, 1, 1, 3)
        self.setWindowTitle("I-POST")
        self.setAutoFillBackground(True)
        self.setLayout(layout)
        palette.setColor(QPalette.Window, QColor("#f2635f"))
        self.setPalette(palette)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.update_message()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_B:  # スペースキーが押されたら
            self.prev_msg_button()
        elif event.key() == Qt.Key_N:
            self.next_msg_button()
        elif event.key() == Qt.Key_I:
            if self.isVisible():
                self.hide()
            else:
                self.showMaximized()
                self.hide()

    def update_message(self):
        try:
            data = get_message()
            self.msg.setText(data[self.msg_number]["text"])
            self.name.setText(data[self.msg_number]["senderName"])
            ts = data[self.msg_number]["sendsAt"]["_seconds"]
            dt = datetime.datetime.fromtimestamp(ts)
            self.received_time.setText(str(dt))
        except IndexError:
            print("Reached first/last message.")
        except  KeyError:
            print("Reached first/last message.")
    def next_msg_button(self):
        if self.msg_number < len(self.data):
            self.msg_number += 3
            self.update_message()
        else:
            self.msg_number = 2
            self.next_msg_button()

    def prev_msg_button(self):
        if self.msg_number > 2:
            self.msg_number -= 3
            self.update_message()

app = QApplication(sys.argv)
w = MainWindow()
w.showMaximized()
sys.exit(app.exec())
