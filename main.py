from datetime import timedelta, datetime, timezone

import pytz
from PySide6.QtWidgets import QApplication, QLayout, QButtonGroup, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox, QTableWidgetItem, QGridLayout, QWidget, QVBoxLayout, QFrame
from PySide6 import QtUiTools
from PySide6.QtCore import QFile, Qt, QRect, QTimer
from pyasn1_modules.rfc2985 import pkcs_9_sx_signingTime
from suspend import Ui_suspend_form

from login import Ui_login_dialog
#from window import Ui_MainWindow
from window1 import Ui_MainWindow
from db import DataBase
from crypt import Cryptor

server = DataBase()
cryptor = Cryptor()
class MyWindow(QMainWindow, Ui_login_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login_check)
        self.setFixedSize(400,600)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.drag_position = None

        self.id_find.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.exit_btn.clicked.connect(self.exit_btn_clicked)

    def login_check(self):
        user_id = self.id_input.text()
        user_pw = self.pw_input.text()
        user_pw.encode()
        server_pw = server.get_pw_by_id(user_id)
        if cryptor.check_pw(user_pw, server_pw):
            self.user_data = server.get_user_data(user_id)
            if self.user_data['auth'] == "임시 차단":
                if datetime.now(timezone.utc) >= self.user_data['until']:
                    server.profile_change(user_id, {'auth' : '유저', 'suspend_reason' : '', 'until' : ''})
                    server.login_log(user_id)
                    self.user_data = server.get_user_data(user_id)
                    self.open_main_window()
                else:
                    QMessageBox.warning(self, "계정 정지됨", f"계정이 일시적으로 정지되어 {self.user_data['until'].strftime("%Y-%m-%d %H:%M")}까지 이용하실 수 없습니다. \n사유 : {self.user_data['suspend_reason']}")
            elif self.user_data['auth'] == "영구 정지":
                QMessageBox.warning(self, "계정 정지됨",
                                    f"계정이 영구 정지되어 이용하실 수 없습니다. \n사유 : {self.user_data['suspend_reason']}")
            else:
                server.login_log(user_id)
                self.open_main_window()
        else:
            QMessageBox.warning(self, "오류", "아이디 혹은 비밀번호가 올바르지 않습니다.")
            print("로그인 실패!")

    def exit_btn_clicked(self):
        exit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos()  # 마우스 클릭 위치 저장
            event.accept()

    def mouseMoveEvent(self, event):
        if self.drag_position:
            delta = event.globalPos() - self.drag_position
            self.move(self.pos() + delta)  # 창 이동
            self.drag_position = event.globalPos()
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_position = None  # 마우스 버튼을 놓으면 이동을 멈춤

    def open_main_window(self):
        self.close()
        self.main_window = MainWindow(self.user_data)
        self.main_window.show()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_data):
        super().__init__()
        self.setupUi(self)

        self.last_sender = None
        self.user_parent_widget.setCurrentIndex(2)
        self.select_menu_widget.setCurrentIndex(0)
        self.profile_apply_frame.hide()

        self.user_id = user_data['user_id']
        self.username = user_data['username']
        self.intro = user_data['intro']
        self.username_title_ps.setText(user_data['username'] + "의 프로필")
        self.username_title_va.setText(user_data['username'] + "의 권한 열람")
        self.username_title_up.setText(user_data['username'])
        self.user_id_title_vl.setText(user_data['user_id'] + " 계정의 로그인 기록")

        self.cp_user_id = None
        self.timer = QTimer(self)
        self.sel_user_data = None

        # 프로필 설정
        self.username_input.setText(user_data['username'])
        self.intro_input.setPlainText(user_data['intro'])

        # 프로필 설정 프리뷰
        def check_changed():
            if self.username_input.text() == user_data['username'] and self.intro_input.toPlainText() == user_data['intro'] and self.profile_apply_frame.isVisible():
                self.profile_apply_frame.hide()
            elif self.profile_apply_frame.isVisible():
                pass
            else:
                self.profile_apply_frame.show()

        def username_update(): self.username_preview.setText(self.username_input.text()); check_changed()
        def intro_update(): self.intro_preview.setText(self.intro_input.toPlainText()); check_changed()

        self.profile_apply_btn.clicked.connect(self.profile_change_apply)
        self.reset_btn.clicked.connect(self.profile_reset)

        self.username_input.textChanged.connect(username_update)
        self.intro_input.textChanged.connect(intro_update)

        self.username_preview.setText(user_data['username'])
        self.user_id_preview.setText(user_data['user_id'])
        self.auth_preview.setText(user_data['auth'])
        self.intro_preview.setText(user_data['intro'])
        #self.cp_username_title.

        self.profile_bar_btn_group = QButtonGroup(self)
        self.profile_bar_btn_group.addButton(self.profile_set_btn)
        self.profile_bar_btn_group.addButton(self.view_auth_btn)
        self.profile_bar_btn_group.addButton(self.data_priv_btn)
        self.profile_bar_btn_group.addButton(self.login_log_btn)
        self.profile_bar_btn_group.buttonClicked.connect(self.bar_btn_pressed)

        self.menu_bar_btn_group = QButtonGroup(self)
        self.menu_bar_btn_group.addButton(self.profile_btn)
        self.menu_bar_btn_group.addButton(self.chat_btn)
        self.menu_bar_btn_group.addButton(self.admin_btn)
        self.menu_bar_btn_group.buttonClicked.connect(self.menu_bar_btn_pressed)

        # 어드민 프로필 뷰어
        self.user_list_ad.cellClicked.connect(self.set_user)
        self.apply_frame_ad.hide()
        self.profile_apply_btn_ad.clicked.connect(self.apply_force_change)
        self.reset_btn_ad.clicked.connect(self.change_reset)
        self.acc_sus_btn_ad.clicked.connect(self.suspend_account)

        # 채팅
        #self.chat_user_layout.addStretch()
        self.chat_user_layout.setAlignment(Qt.AlignTop)
        self.chat_user_layout.setAlignment(Qt.AlignTop)
        self.chat_input.returnPressed.connect(self.send_chat)
        self.chat_scroll_bar = self.chat_scroll.verticalScrollBar()

        # 실행시 함수 로드
        self.load_chat_user()
        self.load_users()

    def bar_btn_pressed(self, button):
        if button.text() == "프로필 설정":
            self.user_parent_widget.setCurrentIndex(2)
        elif button.text() == "권한 보기":
            self.user_parent_widget.setCurrentIndex(0)
        elif button.text() == "데이터 및 개인정보":
            self.user_parent_widget.setCurrentIndex(3)
        elif button.text() == "로그인 기록":
            self.user_parent_widget.setCurrentIndex(1)
            self.call_login_log(self.user_id)

    def menu_bar_btn_pressed(self, button):
        if button.objectName() == "chat_btn":
            self.select_menu_widget.setCurrentIndex(1)
        elif button.objectName() == "profile_btn":
            self.select_menu_widget.setCurrentIndex(0)
        elif button.objectName() == "admin_btn":
            self.select_menu_widget.setCurrentIndex(2)

    def chat_btn_pressed(self):
        self.select_menu_widget.setCurrentIndex(1)

    def call_login_log(self, user_id):
        for data in server.get_login_log(user_id):
            row = self.login_log_widget.rowCount()
            self.login_log_widget.insertRow(row)
            for col, key in enumerate(["time", "os", "country", "ip"]):
                item = QTableWidgetItem(str(data.get(key)))
                item.setTextAlignment(Qt.AlignCenter)
                self.login_log_widget.setItem(row, col, item)


# 유저 설정 프로필 변경 함수
    def profile_change_apply(self):
        data = {
            "username" : self.username_input.text(),
            "intro" : self.intro_input.toPlainText(),
        }
        server.profile_change(self.user_id, data)
        self.profile_apply_frame.hide()
        self.username = self.username_input.text()
        self.intro = self.intro_input.toPlainText()

    def profile_reset(self):
        self.username_input.setText(self.username)
        self.intro_input.setPlainText(self.intro)
        self.profile_apply_frame.hide()

# 어드민 유저 관리창 함수
    def load_users(self):
        users = server.get_user_list()
        for user in users:
            row = self.user_list_ad.rowCount()
            self.user_list_ad.insertRow(row)
            item1 = QTableWidgetItem(str(user.id))
            item2 = QTableWidgetItem(str(user.get('username')))
            self.user_list_ad.setItem(row, 0, item1)
            self.user_list_ad.setItem(row, 1, item2)

    def set_user(self, row, col):
        item = self.user_list_ad.item(row, col)
        data = server.get_user_data(item.text())
        self.sel_user_data = data
        self.username_edit_ad.setText(data['username'])
        self.cp_username_title_ad.setText(data['username'] + "의 프로필 열람")
        self.user_id_edit_ad.setText(data['user_id'])
        self.intro_edit_ad.setPlainText(data['intro'])
        self.auth_sel_box.setCurrentText(data['auth'])

        def check_changed_admin():
            if self.sel_user_data:
                if self.username_edit_ad.text() == self.sel_user_data[
                    'username'] and self.intro_edit_ad.toPlainText() == self.sel_user_data[
                    'intro'] and self.auth_sel_box.currentText() == self.sel_user_data[
                    'auth'] and self.apply_frame_ad.isVisible():
                    self.apply_frame_ad.hide()
                elif self.apply_frame_ad.isVisible():
                    pass
                else:
                    self.apply_frame_ad.show()

        self.username_edit_ad.textChanged.connect(check_changed_admin)
        self.auth_sel_box.currentTextChanged.connect(check_changed_admin)
        self.intro_edit_ad.textChanged.connect(check_changed_admin)

    def apply_force_change(self):
        data = {
            "username" : self.username_edit_ad.text(),
            "intro" : self.intro_edit_ad.toPlainText(),
            "auth" : self.auth_sel_box.currentText(),
        }
        server.profile_change(self.sel_user_data['user_id'], data)
        self.apply_frame_ad.hide()
        self.sel_user_data = server.get_user_data(self.sel_user_data['user_id'])

    def change_reset(self):
        self.username_edit_ad.setText(self.sel_user_data['username'])
        self.intro_edit_ad.setPlainText(self.sel_user_data['intro'])
        self.auth_sel_box.setCurrentText(self.sel_user_data['auth'])
        self.apply_frame_ad.hide()

    def suspend_account(self):
        self.suspend_window = SuspendWindow(self.sel_user_data, self.user_id)
        self.suspend_window.show()
# 채팅 함수
    def load_chat_user(self):
        users = server.get_user_list()
        self.chat_user_btn_group = QButtonGroup(self)
        self.chat_user_btn_group.buttonClicked.connect(self.sel_chat_user)
        for user in users:
            if user.id == self.user_id:  # 본인 id 넘기기
                continue
            button = QPushButton(f"{user.get("username")}")
            button.setObjectName(f"{user.id}")
            button.setFlat(True)
            button.setCheckable(True)
            button.setFixedWidth(171)
            button.setFixedHeight(36)
            self.chat_user_btn_group.addButton(button)
            button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0);
                color: #949ba4;
                font: 500 12pt "프리젠테이션";
                text-align: left;
            }
            QPushButton:checked, QPushButton:hover {
                background-color: #404249;
                color: #ffffff;
            }""")
            self.chat_user_layout.addWidget(button)

    def sel_chat_user(self, button): # 채팅 로딩
        if self.last_sender == None:
            self.last_sender = button.objectName()
            self.timer.timeout.connect(self.sel_chat_user(button))
            self.timer.start(2000)
            return
        self.last_sender = None
        self.last_notice_time = datetime(1900 , 1, 1, 1, 1, tzinfo=pytz.UTC)
        self.remove_chat_layout()
        self.cp_user_id = button.objectName()
        self.cp_username_title.setText(button.objectName())
        chattings = server.load_chat(self.user_id, button.objectName())
        for chat in chattings:
            text = QLabel(chat.get('msg'))
            text.setStyleSheet("""
            border: 1px solid rgba(255, 255, 255, 0);
            font: 400 11pt "프리젠테이션";
            text-align: left;
            color: #ffffff;
            """)
            if self.last_sender == chat.get('sender') or (chat.get('time') - self.last_notice_time) > timedelta(minutes=5):
                chat_time = QLabel()
                chat_time.setText(chat.get('time').strftime("%H:%M"))
                chat_time.setFixedWidth(41)
                chat_time.setFixedHeight(16)
                spacer = QWidget()
                grid_layout = QGridLayout()
                grid_layout.addWidget(chat_time, 0, 0)
                grid_layout.addWidget(text, 0, 1)
                grid_layout.addWidget(spacer, 0, 2)
                self.chat_layout.addLayout(grid_layout)
                self.last_sender = chat.get('sender')
                self.last_notice_time = chat.get('time')

            else:
                #profile_img = QLabel(pixmap=QPixmap("test.png")
                profile_img = QLabel()
                profile_img.setFixedWidth(41)
                profile_img.setFixedHeight(41)

                username = QLabel()
                username.setText(server.get_name_by_id(chat.get('sender')))

                chat_time = QLabel()
                chat_time.setText(chat.get('time').strftime("%Y-%m-%d %H:%M"))

                chat_frame = QFrame()
                chat_frame.setFixedHeight(51)


                grid_layout = QGridLayout(chat_frame)
                grid_layout.addWidget(profile_img, 0, 0)
                grid_layout.addWidget(username, 0, 1)
                grid_layout.addWidget(chat_time, 0, 2)
                grid_layout.setAlignment(chat_time, Qt.AlignRight)
                grid_layout.addWidget(text, 1, 1)
                grid_layout.setAlignment(Qt.AlignTop)

                self.chat_layout.addWidget(chat_frame)
                self.last_sender = chat.get('sender')
                self.last_notice_time = chat.get('time')

    def send_chat(self):
        server.send_chat(self.user_id, self.cp_user_id, self.chat_input.text())
        self.chat_input.clear()
        self.found_btn = self.findChild(QPushButton, self.cp_user_id)
        self.sel_chat_user(self.found_btn)

    def remove_chat_layout(self):
        self.remove_widgets_and_layout(self.chat_layout)

    def remove_widgets_and_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.remove_widgets_and_layout(item.layout())

class SuspendWindow(QWidget, Ui_suspend_form):
    def __init__(self, data, manager):
        super().__init__()
        self.setupUi(self)
        self.manager = manager
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.username.setText(data['username'])
        self.user_id.setText(data['user_id'])
        self.suspend_btn.clicked.connect(self.suspend_account)
        self.raise_()

    def suspend_account(self):
        if self.comboBox.currentText() == "영구 정지":
            data = {
                'auth' : "영구 정지",
                'suspend_reason' : self.reason_edit.toPlainText(),
                'until' : datetime(9999, 12, 31)
            }
            until = datetime(9999, 12, 31)
        else:
            period = int(self.comboBox.currentText().replace("일", ""))
            until = datetime.now() + timedelta(days=period)
            data = {
                'auth': "임시 차단",
                'suspend_reason': self.reason_edit.toPlainText(),
                'until': until
            }
        log = {
            'reason' : self.reason_edit.toPlainText(),
            'manager': self.manager,
            'period': self.comboBox.currentText(),
            'until' : until,
        }
        server.profile_change(self.user_id.text(), data)
        server.add_sus_log(self.user_id.text(), log)
        self.close()

if __name__ == "__main__":
    app = QApplication([])

    window = MyWindow()
    window.show()

    app.exec()
