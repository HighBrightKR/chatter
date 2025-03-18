# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 601)
        MainWindow.setStyleSheet(u"#left_menubar {\n"
"	background-color: #1e1f22;\n"
"}\n"
"\n"
"#center_frame_ch, #center_top_frame_ch, #center_frame_up, #center_top_frame_up, #center_frame_ad, #center_top_frame_ad{\n"
"	background-color: #2b2d31;\n"
"}\n"
"\n"
"#main_frame, #main_top_frame {\n"
"	background-color: #313338;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #949ba4;\n"
"}\n"
"\n"
"#chat_scroll {\n"
"	color: #2b2d31;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.left_menubar = QFrame(self.centralwidget)
        self.left_menubar.setObjectName(u"left_menubar")
        self.left_menubar.setGeometry(QRect(0, 0, 71, 601))
        self.left_menubar.setStyleSheet(u"QPushButton {\n"
"	background-color: #313338;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:checked, QPushButton:hover {\n"
"	background-color: #5865f2;\n"
"	border-radius: 10px;\n"
"}")
        self.left_menubar.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_menubar.setFrameShadow(QFrame.Shadow.Raised)
        self.profile_btn = QPushButton(self.left_menubar)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setGeometry(QRect(10, 10, 51, 51))
        icon = QIcon()
        icon.addFile(u":/user_icon/user (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profile_btn.setIcon(icon)
        self.profile_btn.setIconSize(QSize(32, 32))
        self.profile_btn.setCheckable(True)
        self.profile_btn.setChecked(True)
        self.profile_btn.setAutoRepeatDelay(299)
        self.profile_btn.setFlat(True)
        self.chat_btn = QPushButton(self.left_menubar)
        self.chat_btn.setObjectName(u"chat_btn")
        self.chat_btn.setGeometry(QRect(10, 80, 51, 51))
        icon1 = QIcon()
        icon1.addFile(u":/user_icon/messages (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chat_btn.setIcon(icon1)
        self.chat_btn.setIconSize(QSize(30, 30))
        self.chat_btn.setCheckable(True)
        self.chat_btn.setChecked(False)
        self.chat_btn.setAutoRepeatDelay(299)
        self.chat_btn.setFlat(True)
        self.line = QFrame(self.left_menubar)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 60, 51, 16))
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.admin_btn = QPushButton(self.left_menubar)
        self.admin_btn.setObjectName(u"admin_btn")
        self.admin_btn.setGeometry(QRect(10, 540, 51, 51))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLockScreen))
        self.admin_btn.setIcon(icon2)
        self.admin_btn.setIconSize(QSize(30, 30))
        self.admin_btn.setCheckable(True)
        self.admin_btn.setChecked(False)
        self.admin_btn.setAutoRepeatDelay(299)
        self.admin_btn.setFlat(True)
        self.select_menu_widget = QStackedWidget(self.centralwidget)
        self.select_menu_widget.setObjectName(u"select_menu_widget")
        self.select_menu_widget.setGeometry(QRect(70, 0, 931, 601))
        self.user_profile = QWidget()
        self.user_profile.setObjectName(u"user_profile")
        self.user_profile.setEnabled(True)
        self.user_parent_frame = QFrame(self.user_profile)
        self.user_parent_frame.setObjectName(u"user_parent_frame")
        self.user_parent_frame.setEnabled(True)
        self.user_parent_frame.setGeometry(QRect(0, 0, 931, 601))
        self.user_parent_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.user_parent_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.center_frame_up = QFrame(self.user_parent_frame)
        self.center_frame_up.setObjectName(u"center_frame_up")
        self.center_frame_up.setGeometry(QRect(0, 50, 191, 551))
        self.center_frame_up.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #949ba4;\n"
"}\n"
"\n"
"QPushButton:checked, QPushButton:hover {\n"
"	background-color: #404249;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#acc_del_btn {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #da373c;\n"
"	border: 1px solid #da373c;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#acc_del_btn:hover, #acc_del_btn:pressed {\n"
"	background-color: #da373c;\n"
"	color: #ffffff;\n"
"}")
        self.center_frame_up.setFrameShape(QFrame.Shape.StyledPanel)
        self.center_frame_up.setFrameShadow(QFrame.Shadow.Raised)
        self.profile_set_btn = QPushButton(self.center_frame_up)
        self.profile_set_btn.setObjectName(u"profile_set_btn")
        self.profile_set_btn.setGeometry(QRect(10, 10, 171, 41))
        palette = QPalette()
        brush = QBrush(QColor(148, 155, 164, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(148, 155, 164, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush3 = QBrush(QColor(0, 0, 0, 92))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.profile_set_btn.setPalette(palette)
        font = QFont()
        font.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font.setPointSize(14)
        self.profile_set_btn.setFont(font)
        self.profile_set_btn.setToolTipDuration(-1)
        self.profile_set_btn.setCheckable(True)
        self.profile_set_btn.setChecked(True)
        self.profile_set_btn.setFlat(True)
        self.view_auth_btn = QPushButton(self.center_frame_up)
        self.view_auth_btn.setObjectName(u"view_auth_btn")
        self.view_auth_btn.setGeometry(QRect(10, 60, 171, 41))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.view_auth_btn.setPalette(palette1)
        self.view_auth_btn.setFont(font)
        self.view_auth_btn.setCheckable(True)
        self.view_auth_btn.setFlat(True)
        self.data_priv_btn = QPushButton(self.center_frame_up)
        self.data_priv_btn.setObjectName(u"data_priv_btn")
        self.data_priv_btn.setGeometry(QRect(10, 110, 171, 41))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.data_priv_btn.setPalette(palette2)
        self.data_priv_btn.setFont(font)
        self.data_priv_btn.setCheckable(True)
        self.data_priv_btn.setFlat(True)
        self.login_log_btn = QPushButton(self.center_frame_up)
        self.login_log_btn.setObjectName(u"login_log_btn")
        self.login_log_btn.setGeometry(QRect(10, 160, 171, 41))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.login_log_btn.setPalette(palette3)
        self.login_log_btn.setFont(font)
        self.login_log_btn.setCheckable(True)
        self.login_log_btn.setFlat(True)
        self.acc_del_btn = QPushButton(self.center_frame_up)
        self.acc_del_btn.setObjectName(u"acc_del_btn")
        self.acc_del_btn.setGeometry(QRect(10, 500, 171, 41))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.acc_del_btn.setPalette(palette4)
        self.acc_del_btn.setFont(font)
        self.acc_del_btn.setFlat(True)
        self.logout_btn = QPushButton(self.center_frame_up)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(10, 450, 171, 41))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.logout_btn.setPalette(palette5)
        self.logout_btn.setFont(font)
        self.logout_btn.setFlat(True)
        self.center_top_frame_up = QFrame(self.user_parent_frame)
        self.center_top_frame_up.setObjectName(u"center_top_frame_up")
        self.center_top_frame_up.setGeometry(QRect(0, 0, 191, 51))
        self.center_top_frame_up.setFrameShape(QFrame.Shape.StyledPanel)
        self.center_top_frame_up.setFrameShadow(QFrame.Shadow.Raised)
        self.center_top_frame_up.setLineWidth(1)
        self.username_title_up = QLabel(self.center_top_frame_up)
        self.username_title_up.setObjectName(u"username_title_up")
        self.username_title_up.setGeometry(QRect(7, 5, 181, 41))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.username_title_up.setPalette(palette6)
        font1 = QFont()
        font1.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.username_title_up.setFont(font1)
        self.username_title_up.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_parent_widget = QStackedWidget(self.user_parent_frame)
        self.user_parent_widget.setObjectName(u"user_parent_widget")
        self.user_parent_widget.setEnabled(True)
        self.user_parent_widget.setGeometry(QRect(190, 0, 741, 621))
        self.view_auth_widget = QWidget()
        self.view_auth_widget.setObjectName(u"view_auth_widget")
        self.view_auth_widget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.view_auth_frame = QFrame(self.view_auth_widget)
        self.view_auth_frame.setObjectName(u"view_auth_frame")
        self.view_auth_frame.setEnabled(True)
        self.view_auth_frame.setGeometry(QRect(0, 0, 741, 601))
        self.view_auth_frame.setStyleSheet(u"QLineEdit, QPlainTextEdit {\n"
"	background-color: #1e1f22;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"	color: #ffffff;\n"
"}\n"
"QFrame {\n"
"	background-color: #313338;\n"
"}\n"
"#intro_input{\n"
"	background-color: #1e1f22;\n"
"	color: #ffffff;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#profile_pic_change_btn{\n"
"	background-color: #5865f2;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#profile_pic_del_btn{\n"
"	background-color: #da373c;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#preview_frame {\n"
"	background-color: #111214;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#profile_pic_preview {\n"
"	background-color: rgba(255, 255, 255, 111);\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #2b2d31;\n"
"	color:#ffffff;\n"
"	font: 450 11pt \"\ud504\ub9ac\uc820\ud14c\uc774\uc158\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"	text-align: center;\n"
"	color: rgb(148, 155, 164);\n"
"}\n"
""
                        "\n"
"")
        self.view_auth_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.view_auth_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.main_frame_va = QFrame(self.view_auth_frame)
        self.main_frame_va.setObjectName(u"main_frame_va")
        self.main_frame_va.setGeometry(QRect(0, 50, 741, 551))
        self.main_frame_va.setStyleSheet(u"")
        self.main_frame_va.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_va.setFrameShadow(QFrame.Shadow.Raised)
        self.perm_1 = QTableWidget(self.main_frame_va)
        if (self.perm_1.columnCount() < 1):
            self.perm_1.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.perm_1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.perm_1.rowCount() < 16):
            self.perm_1.setRowCount(16)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.perm_1.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.perm_1.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.perm_1.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.perm_1.setItem(1, 0, __qtablewidgetitem4)
        self.perm_1.setObjectName(u"perm_1")
        self.perm_1.setGeometry(QRect(10, 20, 171, 531))
        font2 = QFont()
        font2.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font2.setPointSize(12)
        font2.setKerning(True)
        self.perm_1.setFont(font2)
        self.perm_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.perm_1.setAutoFillBackground(False)
        self.perm_1.setFrameShape(QFrame.Shape.NoFrame)
        self.perm_1.setAutoScroll(False)
        self.perm_1.setTabKeyNavigation(True)
        self.perm_1.setRowCount(16)
        self.perm_1.setColumnCount(1)
        self.perm_1.horizontalHeader().setVisible(False)
        self.perm_1.horizontalHeader().setHighlightSections(True)
        self.perm_1.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.perm_1.horizontalHeader().setStretchLastSection(False)
        self.perm_1.verticalHeader().setProperty(u"showSortIndicator", False)
        self.perm_1.verticalHeader().setStretchLastSection(False)
        self.perm_2 = QTableWidget(self.main_frame_va)
        if (self.perm_2.columnCount() < 1):
            self.perm_2.setColumnCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.perm_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        if (self.perm_2.rowCount() < 16):
            self.perm_2.setRowCount(16)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.perm_2.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.perm_2.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.perm_2.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.perm_2.setItem(1, 0, __qtablewidgetitem9)
        self.perm_2.setObjectName(u"perm_2")
        self.perm_2.setGeometry(QRect(190, 20, 171, 531))
        self.perm_2.setFont(font2)
        self.perm_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.perm_2.setAutoFillBackground(False)
        self.perm_2.setFrameShape(QFrame.Shape.NoFrame)
        self.perm_2.setAutoScroll(False)
        self.perm_2.setTabKeyNavigation(True)
        self.perm_2.setRowCount(16)
        self.perm_2.setColumnCount(1)
        self.perm_2.horizontalHeader().setVisible(False)
        self.perm_2.horizontalHeader().setHighlightSections(True)
        self.perm_2.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.perm_2.horizontalHeader().setStretchLastSection(False)
        self.perm_2.verticalHeader().setProperty(u"showSortIndicator", False)
        self.perm_2.verticalHeader().setStretchLastSection(False)
        self.perm_3 = QTableWidget(self.main_frame_va)
        if (self.perm_3.columnCount() < 1):
            self.perm_3.setColumnCount(1)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.perm_3.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        if (self.perm_3.rowCount() < 16):
            self.perm_3.setRowCount(16)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.perm_3.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.perm_3.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.perm_3.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.perm_3.setItem(1, 0, __qtablewidgetitem14)
        self.perm_3.setObjectName(u"perm_3")
        self.perm_3.setGeometry(QRect(370, 20, 171, 531))
        self.perm_3.setFont(font2)
        self.perm_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.perm_3.setAutoFillBackground(False)
        self.perm_3.setFrameShape(QFrame.Shape.NoFrame)
        self.perm_3.setAutoScroll(False)
        self.perm_3.setTabKeyNavigation(True)
        self.perm_3.setRowCount(16)
        self.perm_3.setColumnCount(1)
        self.perm_3.horizontalHeader().setVisible(False)
        self.perm_3.horizontalHeader().setHighlightSections(True)
        self.perm_3.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.perm_3.horizontalHeader().setStretchLastSection(False)
        self.perm_3.verticalHeader().setProperty(u"showSortIndicator", False)
        self.perm_3.verticalHeader().setStretchLastSection(False)
        self.perm_4 = QTableWidget(self.main_frame_va)
        if (self.perm_4.columnCount() < 1):
            self.perm_4.setColumnCount(1)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.perm_4.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        if (self.perm_4.rowCount() < 16):
            self.perm_4.setRowCount(16)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.perm_4.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.perm_4.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.perm_4.setItem(0, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.perm_4.setItem(1, 0, __qtablewidgetitem19)
        self.perm_4.setObjectName(u"perm_4")
        self.perm_4.setGeometry(QRect(550, 20, 171, 531))
        self.perm_4.setFont(font2)
        self.perm_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.perm_4.setAutoFillBackground(False)
        self.perm_4.setFrameShape(QFrame.Shape.NoFrame)
        self.perm_4.setAutoScroll(False)
        self.perm_4.setTabKeyNavigation(True)
        self.perm_4.setRowCount(16)
        self.perm_4.setColumnCount(1)
        self.perm_4.horizontalHeader().setVisible(False)
        self.perm_4.horizontalHeader().setHighlightSections(True)
        self.perm_4.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.perm_4.horizontalHeader().setStretchLastSection(False)
        self.perm_4.verticalHeader().setProperty(u"showSortIndicator", False)
        self.perm_4.verticalHeader().setStretchLastSection(False)
        self.main_top_frame_va = QFrame(self.view_auth_frame)
        self.main_top_frame_va.setObjectName(u"main_top_frame_va")
        self.main_top_frame_va.setEnabled(True)
        self.main_top_frame_va.setGeometry(QRect(0, 0, 741, 51))
        self.main_top_frame_va.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_top_frame_va.setFrameShadow(QFrame.Shadow.Raised)
        self.username_title_va = QLabel(self.main_top_frame_va)
        self.username_title_va.setObjectName(u"username_title_va")
        self.username_title_va.setGeometry(QRect(20, 10, 511, 31))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush4 = QBrush(QColor(49, 51, 56, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.username_title_va.setPalette(palette7)
        font3 = QFont()
        font3.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.username_title_va.setFont(font3)
        self.username_title_va.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ip_label_va = QLabel(self.main_top_frame_va)
        self.ip_label_va.setObjectName(u"ip_label_va")
        self.ip_label_va.setGeometry(QRect(530, 10, 191, 31))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.ip_label_va.setPalette(palette8)
        self.ip_label_va.setFont(font3)
        self.ip_label_va.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.user_parent_widget.addWidget(self.view_auth_widget)
        self.view_login_log = QWidget()
        self.view_login_log.setObjectName(u"view_login_log")
        self.view_login_frame = QFrame(self.view_login_log)
        self.view_login_frame.setObjectName(u"view_login_frame")
        self.view_login_frame.setEnabled(True)
        self.view_login_frame.setGeometry(QRect(0, 0, 741, 601))
        self.view_login_frame.setStyleSheet(u"QLineEdit, QPlainTextEdit {\n"
"	background-color: #1e1f22;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"	color: #ffffff;\n"
"}\n"
"QFrame {\n"
"	background-color: #313338;\n"
"}\n"
"#intro_input{\n"
"	background-color: #1e1f22;\n"
"	color: #ffffff;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#profile_pic_change_btn{\n"
"	background-color: #5865f2;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#profile_pic_del_btn{\n"
"	background-color: #da373c;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#preview_frame {\n"
"	background-color: #111214;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#profile_pic_preview {\n"
"	background-color: rgba(255, 255, 255, 111);\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #2b2d31;\n"
"	color:#ffffff;\n"
"	font: 450 11pt \"\ud504\ub9ac\uc820\ud14c\uc774\uc158\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"	text-align: center;\n"
"	color: rgb(148, 155, 164);\n"
"}")
        self.view_login_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.view_login_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.main_frame_vl = QFrame(self.view_login_frame)
        self.main_frame_vl.setObjectName(u"main_frame_vl")
        self.main_frame_vl.setGeometry(QRect(0, 50, 741, 551))
        self.main_frame_vl.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_vl.setFrameShadow(QFrame.Shadow.Raised)
        self.login_log_widget = QTableWidget(self.main_frame_vl)
        if (self.login_log_widget.columnCount() < 4):
            self.login_log_widget.setColumnCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.login_log_widget.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.login_log_widget.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.login_log_widget.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.login_log_widget.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        self.login_log_widget.setObjectName(u"login_log_widget")
        self.login_log_widget.setGeometry(QRect(10, 10, 721, 531))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_log_widget.sizePolicy().hasHeightForWidth())
        self.login_log_widget.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font4.setPointSize(10)
        self.login_log_widget.setFont(font4)
        self.login_log_widget.setFrameShape(QFrame.Shape.NoFrame)
        self.login_log_widget.setFrameShadow(QFrame.Shadow.Sunken)
        self.login_log_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.login_log_widget.setShowGrid(False)
        self.login_log_widget.setSortingEnabled(False)
        self.login_log_widget.setWordWrap(True)
        self.login_log_widget.setCornerButtonEnabled(True)
        self.login_log_widget.setColumnCount(4)
        self.login_log_widget.horizontalHeader().setVisible(True)
        self.login_log_widget.horizontalHeader().setDefaultSectionSize(181)
        self.login_log_widget.horizontalHeader().setHighlightSections(True)
        self.login_log_widget.verticalHeader().setVisible(False)
        self.main_top_frame_vl = QFrame(self.view_login_frame)
        self.main_top_frame_vl.setObjectName(u"main_top_frame_vl")
        self.main_top_frame_vl.setEnabled(True)
        self.main_top_frame_vl.setGeometry(QRect(0, 0, 741, 51))
        self.main_top_frame_vl.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_top_frame_vl.setFrameShadow(QFrame.Shadow.Raised)
        self.user_id_title_vl = QLabel(self.main_top_frame_vl)
        self.user_id_title_vl.setObjectName(u"user_id_title_vl")
        self.user_id_title_vl.setGeometry(QRect(20, 10, 511, 31))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.user_id_title_vl.setPalette(palette9)
        self.user_id_title_vl.setFont(font3)
        self.user_id_title_vl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ip_label_vl = QLabel(self.main_top_frame_vl)
        self.ip_label_vl.setObjectName(u"ip_label_vl")
        self.ip_label_vl.setGeometry(QRect(530, 10, 191, 31))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.ip_label_vl.setPalette(palette10)
        self.ip_label_vl.setFont(font3)
        self.ip_label_vl.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.user_parent_widget.addWidget(self.view_login_log)
        self.profile_set_widget = QWidget()
        self.profile_set_widget.setObjectName(u"profile_set_widget")
        self.profile_set_frame = QFrame(self.profile_set_widget)
        self.profile_set_frame.setObjectName(u"profile_set_frame")
        self.profile_set_frame.setEnabled(True)
        self.profile_set_frame.setGeometry(QRect(0, 0, 741, 601))
        font5 = QFont()
        font5.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font5.setPointSize(12)
        self.profile_set_frame.setFont(font5)
        self.profile_set_frame.setStyleSheet(u"QLineEdit, QPlainTextEdit {\n"
"	background-color: #1e1f22;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"	color: #ffffff;\n"
"}\n"
"QFrame {\n"
"	background-color: #313338;\n"
"}\n"
"#intro_input{\n"
"	background-color: #1e1f22;\n"
"	color: #ffffff;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#profile_pic_change_btn{\n"
"	background-color: #5865f2;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#profile_pic_del_btn{\n"
"	background-color: #da373c;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#preview_frame {\n"
"	background-color: #111214;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#profile_pic_preview {\n"
"	background-color: rgba(255, 255, 255, 111);\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"#profile_apply_frame {\n"
"	background-color: #111214;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#apply_inform_label {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#reset_btn {\n"
"	background-colo"
                        "r: rgba(255, 255, 255, 0);\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#profile_apply_btn {\n"
"	background-color: #248045;\n"
"	color: #ffffff;\n"
"}")
        self.profile_set_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.profile_set_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.profile_main_frame = QFrame(self.profile_set_frame)
        self.profile_main_frame.setObjectName(u"profile_main_frame")
        self.profile_main_frame.setGeometry(QRect(0, 50, 741, 551))
        self.profile_main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.profile_main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.username_label = QLabel(self.profile_main_frame)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(10, 10, 291, 31))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.username_label.setPalette(palette11)
        font6 = QFont()
        font6.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font6.setPointSize(11)
        font6.setBold(False)
        self.username_label.setFont(font6)
        self.username_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.username_input = QLineEdit(self.profile_main_frame)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(10, 40, 291, 41))
        font7 = QFont()
        font7.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font7.setPointSize(11)
        self.username_input.setFont(font7)
        self.username_input.setClearButtonEnabled(False)
        self.intro_label = QLabel(self.profile_main_frame)
        self.intro_label.setObjectName(u"intro_label")
        self.intro_label.setGeometry(QRect(10, 90, 291, 31))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.intro_label.setPalette(palette12)
        self.intro_label.setFont(font6)
        self.intro_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.intro_input = QPlainTextEdit(self.profile_main_frame)
        self.intro_input.setObjectName(u"intro_input")
        self.intro_input.setGeometry(QRect(10, 120, 291, 121))
        self.intro_input.setFont(font7)
        self.intro_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.intro_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.intro_input.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.intro_input.setMaximumBlockCount(4)
        self.profile_pic_label = QLabel(self.profile_main_frame)
        self.profile_pic_label.setObjectName(u"profile_pic_label")
        self.profile_pic_label.setGeometry(QRect(10, 250, 291, 31))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.profile_pic_label.setPalette(palette13)
        self.profile_pic_label.setFont(font6)
        self.profile_pic_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.profile_pic_change_btn = QPushButton(self.profile_main_frame)
        self.profile_pic_change_btn.setObjectName(u"profile_pic_change_btn")
        self.profile_pic_change_btn.setGeometry(QRect(10, 280, 131, 31))
        self.profile_pic_del_btn = QPushButton(self.profile_main_frame)
        self.profile_pic_del_btn.setObjectName(u"profile_pic_del_btn")
        self.profile_pic_del_btn.setGeometry(QRect(150, 280, 131, 31))
        self.preview_label = QLabel(self.profile_main_frame)
        self.preview_label.setObjectName(u"preview_label")
        self.preview_label.setGeometry(QRect(350, 10, 371, 31))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.preview_label.setPalette(palette14)
        self.preview_label.setFont(font6)
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.preview_frame = QFrame(self.profile_main_frame)
        self.preview_frame.setObjectName(u"preview_frame")
        self.preview_frame.setGeometry(QRect(350, 40, 341, 231))
        self.preview_frame.setStyleSheet(u"QPushButton {\n"
"	background-color: #313338;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #ffffff;\n"
"}")
        self.preview_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.preview_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.profile_pic_preview = QPushButton(self.preview_frame)
        self.profile_pic_preview.setObjectName(u"profile_pic_preview")
        self.profile_pic_preview.setGeometry(QRect(10, 10, 71, 71))
        self.profile_pic_preview.setIcon(icon)
        self.profile_pic_preview.setIconSize(QSize(32, 32))
        self.profile_pic_preview.setAutoRepeatDelay(299)
        self.profile_pic_preview.setFlat(True)
        self.username_preview = QLabel(self.preview_frame)
        self.username_preview.setObjectName(u"username_preview")
        self.username_preview.setGeometry(QRect(100, 20, 221, 21))
        self.username_preview.setFont(font1)
        self.user_id_preview = QLabel(self.preview_frame)
        self.user_id_preview.setObjectName(u"user_id_preview")
        self.user_id_preview.setGeometry(QRect(100, 50, 221, 21))
        self.user_id_preview.setFont(font5)
        self.intro_preview = QLabel(self.preview_frame)
        self.intro_preview.setObjectName(u"intro_preview")
        self.intro_preview.setGeometry(QRect(10, 100, 301, 91))
        self.intro_preview.setFont(font5)
        self.intro_preview.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.intro_preview.setMargin(5)
        self.auth_preview = QLabel(self.preview_frame)
        self.auth_preview.setObjectName(u"auth_preview")
        self.auth_preview.setGeometry(QRect(10, 200, 151, 21))
        self.auth_preview.setFont(font4)
        self.auth_preview.setMargin(5)
        self.ip_preview = QLabel(self.preview_frame)
        self.ip_preview.setObjectName(u"ip_preview")
        self.ip_preview.setGeometry(QRect(180, 200, 151, 21))
        self.ip_preview.setFont(font4)
        self.ip_preview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ip_preview.setMargin(5)
        self.logo_preview = QLabel(self.preview_frame)
        self.logo_preview.setObjectName(u"logo_preview")
        self.logo_preview.setGeometry(QRect(260, 20, 61, 61))
        self.logo_preview.setPixmap(QPixmap(u"../../Users/59613/Downloads/CAB (2).png"))
        self.logo_preview.setScaledContents(True)
        self.logo_preview.raise_()
        self.profile_pic_preview.raise_()
        self.username_preview.raise_()
        self.user_id_preview.raise_()
        self.intro_preview.raise_()
        self.auth_preview.raise_()
        self.ip_preview.raise_()
        self.profile_apply_frame = QFrame(self.profile_main_frame)
        self.profile_apply_frame.setObjectName(u"profile_apply_frame")
        self.profile_apply_frame.setEnabled(True)
        self.profile_apply_frame.setGeometry(QRect(19, 479, 701, 51))
        self.profile_apply_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.profile_apply_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.apply_inform_label = QLabel(self.profile_apply_frame)
        self.apply_inform_label.setObjectName(u"apply_inform_label")
        self.apply_inform_label.setGeometry(QRect(10, 10, 441, 31))
        self.apply_inform_label.setFont(font5)
        self.reset_btn = QPushButton(self.profile_apply_frame)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(460, 10, 81, 31))
        self.reset_btn.setFont(font5)
        self.profile_apply_btn = QPushButton(self.profile_apply_frame)
        self.profile_apply_btn.setObjectName(u"profile_apply_btn")
        self.profile_apply_btn.setGeometry(QRect(550, 10, 141, 31))
        self.profile_apply_btn.setFont(font5)
        self.profile_main_top_frame = QFrame(self.profile_set_frame)
        self.profile_main_top_frame.setObjectName(u"profile_main_top_frame")
        self.profile_main_top_frame.setEnabled(True)
        self.profile_main_top_frame.setGeometry(QRect(0, 0, 741, 51))
        self.profile_main_top_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.profile_main_top_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.username_title_ps = QLabel(self.profile_main_top_frame)
        self.username_title_ps.setObjectName(u"username_title_ps")
        self.username_title_ps.setGeometry(QRect(20, 10, 511, 31))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.username_title_ps.setPalette(palette15)
        self.username_title_ps.setFont(font3)
        self.username_title_ps.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ip_label_ps = QLabel(self.profile_main_top_frame)
        self.ip_label_ps.setObjectName(u"ip_label_ps")
        self.ip_label_ps.setGeometry(QRect(530, 10, 191, 31))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.ip_label_ps.setPalette(palette16)
        self.ip_label_ps.setFont(font3)
        self.ip_label_ps.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.user_parent_widget.addWidget(self.profile_set_widget)
        self.select_menu_widget.addWidget(self.user_profile)
        self.chat = QWidget()
        self.chat.setObjectName(u"chat")
        self.chat.setStyleSheet(u"#chat_search_input {\n"
"	color: #898f98;\n"
"	background-color: rgb(30, 31, 34);\n"
"	border: 1px solid rgba(255, 255, 255, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #949ba4;\n"
"}\n"
"\n"
"QPushButton:checked, QPushButton:hover {\n"
"	background-color: #404249;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#main_frame_ch, #main_top_frame_ch {\n"
"	background-color: #313338;\n"
"}\n"
"\n"
"#chat_scroll,#chat_scroll_bg, #msg_scroll, #msg_scroll_bg, #chat_input_frame {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"#chat_input {\n"
"	background-color: #383a40;\n"
"	border: 1px solid rgba(255, 255, 255, 0);\n"
"	border-radius: 5px;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#cp_username_title {color: #ffffff;}")
        self.chat_parent_frame = QFrame(self.chat)
        self.chat_parent_frame.setObjectName(u"chat_parent_frame")
        self.chat_parent_frame.setEnabled(True)
        self.chat_parent_frame.setGeometry(QRect(0, 0, 931, 601))
        self.chat_parent_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chat_parent_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.center_frame_ch = QFrame(self.chat_parent_frame)
        self.center_frame_ch.setObjectName(u"center_frame_ch")
        self.center_frame_ch.setGeometry(QRect(0, 50, 191, 551))
        self.center_frame_ch.setStyleSheet(u"")
        self.center_frame_ch.setFrameShape(QFrame.Shape.StyledPanel)
        self.center_frame_ch.setFrameShadow(QFrame.Shadow.Raised)
        self.chat_scroll = QScrollArea(self.center_frame_ch)
        self.chat_scroll.setObjectName(u"chat_scroll")
        self.chat_scroll.setGeometry(QRect(0, 0, 191, 551))
        self.chat_scroll.setWidgetResizable(True)
        self.chat_scroll_bg = QWidget()
        self.chat_scroll_bg.setObjectName(u"chat_scroll_bg")
        self.chat_scroll_bg.setGeometry(QRect(0, 0, 189, 549))
        self.verticalLayoutWidget = QWidget(self.chat_scroll_bg)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 171, 531))
        self.chat_user_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.chat_user_layout.setObjectName(u"chat_user_layout")
        self.chat_user_layout.setContentsMargins(0, 0, 0, 0)
        self.chat_scroll.setWidget(self.chat_scroll_bg)
        self.center_top_frame_ch = QFrame(self.chat_parent_frame)
        self.center_top_frame_ch.setObjectName(u"center_top_frame_ch")
        self.center_top_frame_ch.setGeometry(QRect(0, 0, 191, 51))
        self.center_top_frame_ch.setFrameShape(QFrame.Shape.StyledPanel)
        self.center_top_frame_ch.setFrameShadow(QFrame.Shadow.Raised)
        self.center_top_frame_ch.setLineWidth(1)
        self.chat_search_input = QLineEdit(self.center_top_frame_ch)
        self.chat_search_input.setObjectName(u"chat_search_input")
        self.chat_search_input.setGeometry(QRect(10, 10, 171, 31))
        self.chat_search_input.setFont(font5)
        self.main_frame_ch = QFrame(self.chat_parent_frame)
        self.main_frame_ch.setObjectName(u"main_frame_ch")
        self.main_frame_ch.setGeometry(QRect(190, 50, 741, 551))
        self.main_frame_ch.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_ch.setFrameShadow(QFrame.Shadow.Raised)
        self.chat_input_frame = QFrame(self.main_frame_ch)
        self.chat_input_frame.setObjectName(u"chat_input_frame")
        self.chat_input_frame.setGeometry(QRect(0, 470, 741, 81))
        self.chat_input_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chat_input_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.chat_input = QLineEdit(self.chat_input_frame)
        self.chat_input.setObjectName(u"chat_input")
        self.chat_input.setGeometry(QRect(10, 10, 721, 41))
        self.chat_input.setFont(font5)
        self.msg_scroll = QScrollArea(self.main_frame_ch)
        self.msg_scroll.setObjectName(u"msg_scroll")
        self.msg_scroll.setGeometry(QRect(0, 0, 741, 471))
        self.msg_scroll.setWidgetResizable(True)
        self.msg_scroll_bg = QWidget()
        self.msg_scroll_bg.setObjectName(u"msg_scroll_bg")
        self.msg_scroll_bg.setGeometry(QRect(0, 0, 739, 469))
        self.verticalLayoutWidget_2 = QWidget(self.msg_scroll_bg)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 721, 451))
        self.chat_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.chat_layout.setObjectName(u"chat_layout")
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.msg_scroll.setWidget(self.msg_scroll_bg)
        self.main_top_frame_ch = QFrame(self.chat_parent_frame)
        self.main_top_frame_ch.setObjectName(u"main_top_frame_ch")
        self.main_top_frame_ch.setGeometry(QRect(190, 0, 741, 51))
        self.main_top_frame_ch.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_top_frame_ch.setFrameShadow(QFrame.Shadow.Raised)
        self.chat_profile_img = QLabel(self.main_top_frame_ch)
        self.chat_profile_img.setObjectName(u"chat_profile_img")
        self.chat_profile_img.setGeometry(QRect(10, 10, 31, 31))
        self.chat_profile_img.setPixmap(QPixmap(u":/user_icon/user (2).png"))
        self.chat_profile_img.setScaledContents(True)
        self.cp_username_title = QLabel(self.main_top_frame_ch)
        self.cp_username_title.setObjectName(u"cp_username_title")
        self.cp_username_title.setGeometry(QRect(50, 10, 91, 31))
        self.cp_username_title.setFont(font1)
        self.cp_username_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.select_menu_widget.addWidget(self.chat)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"")
        self.user_parent_frame_2 = QFrame(self.page)
        self.user_parent_frame_2.setObjectName(u"user_parent_frame_2")
        self.user_parent_frame_2.setEnabled(True)
        self.user_parent_frame_2.setGeometry(QRect(0, 0, 931, 601))
        self.user_parent_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.user_parent_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.center_frame_ad = QFrame(self.user_parent_frame_2)
        self.center_frame_ad.setObjectName(u"center_frame_ad")
        self.center_frame_ad.setGeometry(QRect(0, 50, 191, 551))
        self.center_frame_ad.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #949ba4;\n"
"}\n"
"\n"
"QPushButton:checked, QPushButton:hover {\n"
"	background-color: #404249;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#acc_del_btn {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #da373c;\n"
"	border: 1px solid #da373c;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#acc_del_btn:hover, #acc_del_btn:pressed {\n"
"	background-color: #da373c;\n"
"	color: #ffffff;\n"
"}")
        self.center_frame_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.center_frame_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.profile_view_btn_ad = QPushButton(self.center_frame_ad)
        self.profile_view_btn_ad.setObjectName(u"profile_view_btn_ad")
        self.profile_view_btn_ad.setGeometry(QRect(10, 10, 171, 41))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.profile_view_btn_ad.setPalette(palette17)
        self.profile_view_btn_ad.setFont(font)
        self.profile_view_btn_ad.setToolTipDuration(-1)
        self.profile_view_btn_ad.setCheckable(True)
        self.profile_view_btn_ad.setChecked(True)
        self.profile_view_btn_ad.setFlat(True)
        self.login_log_btn_ad = QPushButton(self.center_frame_ad)
        self.login_log_btn_ad.setObjectName(u"login_log_btn_ad")
        self.login_log_btn_ad.setGeometry(QRect(10, 60, 171, 41))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.login_log_btn_ad.setPalette(palette18)
        self.login_log_btn_ad.setFont(font)
        self.login_log_btn_ad.setCheckable(True)
        self.login_log_btn_ad.setFlat(True)
        self.center_top_frame_ad = QFrame(self.user_parent_frame_2)
        self.center_top_frame_ad.setObjectName(u"center_top_frame_ad")
        self.center_top_frame_ad.setGeometry(QRect(0, 0, 191, 51))
        self.center_top_frame_ad.setStyleSheet(u"")
        self.center_top_frame_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.center_top_frame_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.center_top_frame_ad.setLineWidth(1)
        self.username_title_ad = QLabel(self.center_top_frame_ad)
        self.username_title_ad.setObjectName(u"username_title_ad")
        self.username_title_ad.setGeometry(QRect(7, 5, 181, 41))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.username_title_ad.setPalette(palette19)
        self.username_title_ad.setFont(font1)
        self.username_title_ad.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_management = QStackedWidget(self.user_parent_frame_2)
        self.user_management.setObjectName(u"user_management")
        self.user_management.setEnabled(True)
        self.user_management.setGeometry(QRect(190, 0, 741, 621))
        self.view_auth_widget_ad = QWidget()
        self.view_auth_widget_ad.setObjectName(u"view_auth_widget_ad")
        self.view_auth_widget_ad.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.view_auth_frame_2 = QFrame(self.view_auth_widget_ad)
        self.view_auth_frame_2.setObjectName(u"view_auth_frame_2")
        self.view_auth_frame_2.setEnabled(True)
        self.view_auth_frame_2.setGeometry(QRect(0, 0, 741, 601))
        self.view_auth_frame_2.setStyleSheet(u"QLineEdit, QPlainTextEdit {\n"
"	background-color: #1e1f22;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"	color: #ffffff;\n"
"}\n"
"QFrame {\n"
"	background-color: #313338;\n"
"}\n"
"#intro_input{\n"
"	background-color: #1e1f22;\n"
"	color: #ffffff;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#profile_pic_change_btn{\n"
"	background-color: #5865f2;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#profile_pic_del_btn{\n"
"	background-color: #da373c;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#preview_frame {\n"
"	background-color: #111214;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#profile_pic_preview {\n"
"	background-color: rgba(255, 255, 255, 111);\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #2b2d31;\n"
"	color:#ffffff;\n"
"	font: 450 11pt \"\ud504\ub9ac\uc820\ud14c\uc774\uc158\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"	text-align: center;\n"
"	color: rgb(148, 155, 164);\n"
"}\n"
""
                        "\n"
"")
        self.view_auth_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.view_auth_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.main_frame_va_2 = QFrame(self.view_auth_frame_2)
        self.main_frame_va_2.setObjectName(u"main_frame_va_2")
        self.main_frame_va_2.setGeometry(QRect(0, 50, 741, 551))
        self.main_frame_va_2.setStyleSheet(u"")
        self.main_frame_va_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_va_2.setFrameShadow(QFrame.Shadow.Raised)
        self.perm_5 = QTableWidget(self.main_frame_va_2)
        if (self.perm_5.columnCount() < 1):
            self.perm_5.setColumnCount(1)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.perm_5.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        if (self.perm_5.rowCount() < 16):
            self.perm_5.setRowCount(16)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.perm_5.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.perm_5.setVerticalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.perm_5.setItem(0, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.perm_5.setItem(1, 0, __qtablewidgetitem28)
        self.perm_5.setObjectName(u"perm_5")
        self.perm_5.setGeometry(QRect(10, 20, 171, 531))
        self.perm_5.setFont(font2)
        self.perm_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.perm_5.setAutoFillBackground(False)
        self.perm_5.setFrameShape(QFrame.Shape.NoFrame)
        self.perm_5.setAutoScroll(False)
        self.perm_5.setTabKeyNavigation(True)
        self.perm_5.setRowCount(16)
        self.perm_5.setColumnCount(1)
        self.perm_5.horizontalHeader().setVisible(False)
        self.perm_5.horizontalHeader().setHighlightSections(True)
        self.perm_5.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.perm_5.horizontalHeader().setStretchLastSection(False)
        self.perm_5.verticalHeader().setProperty(u"showSortIndicator", False)
        self.perm_5.verticalHeader().setStretchLastSection(False)
        self.perm_6 = QTableWidget(self.main_frame_va_2)
        if (self.perm_6.columnCount() < 1):
            self.perm_6.setColumnCount(1)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.perm_6.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        if (self.perm_6.rowCount() < 16):
            self.perm_6.setRowCount(16)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.perm_6.setVerticalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.perm_6.setVerticalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.perm_6.setItem(0, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.perm_6.setItem(1, 0, __qtablewidgetitem33)
        self.perm_6.setObjectName(u"perm_6")
        self.perm_6.setGeometry(QRect(190, 20, 171, 531))
        self.perm_6.setFont(font2)
        self.perm_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.perm_6.setAutoFillBackground(False)
        self.perm_6.setFrameShape(QFrame.Shape.NoFrame)
        self.perm_6.setAutoScroll(False)
        self.perm_6.setTabKeyNavigation(True)
        self.perm_6.setRowCount(16)
        self.perm_6.setColumnCount(1)
        self.perm_6.horizontalHeader().setVisible(False)
        self.perm_6.horizontalHeader().setHighlightSections(True)
        self.perm_6.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.perm_6.horizontalHeader().setStretchLastSection(False)
        self.perm_6.verticalHeader().setProperty(u"showSortIndicator", False)
        self.perm_6.verticalHeader().setStretchLastSection(False)
        self.perm_7 = QTableWidget(self.main_frame_va_2)
        if (self.perm_7.columnCount() < 1):
            self.perm_7.setColumnCount(1)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.perm_7.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        if (self.perm_7.rowCount() < 16):
            self.perm_7.setRowCount(16)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.perm_7.setVerticalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.perm_7.setVerticalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.perm_7.setItem(0, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.perm_7.setItem(1, 0, __qtablewidgetitem38)
        self.perm_7.setObjectName(u"perm_7")
        self.perm_7.setGeometry(QRect(370, 20, 171, 531))
        self.perm_7.setFont(font2)
        self.perm_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.perm_7.setAutoFillBackground(False)
        self.perm_7.setFrameShape(QFrame.Shape.NoFrame)
        self.perm_7.setAutoScroll(False)
        self.perm_7.setTabKeyNavigation(True)
        self.perm_7.setRowCount(16)
        self.perm_7.setColumnCount(1)
        self.perm_7.horizontalHeader().setVisible(False)
        self.perm_7.horizontalHeader().setHighlightSections(True)
        self.perm_7.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.perm_7.horizontalHeader().setStretchLastSection(False)
        self.perm_7.verticalHeader().setProperty(u"showSortIndicator", False)
        self.perm_7.verticalHeader().setStretchLastSection(False)
        self.perm_8 = QTableWidget(self.main_frame_va_2)
        if (self.perm_8.columnCount() < 1):
            self.perm_8.setColumnCount(1)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.perm_8.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        if (self.perm_8.rowCount() < 16):
            self.perm_8.setRowCount(16)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.perm_8.setVerticalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.perm_8.setVerticalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.perm_8.setItem(0, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.perm_8.setItem(1, 0, __qtablewidgetitem43)
        self.perm_8.setObjectName(u"perm_8")
        self.perm_8.setGeometry(QRect(550, 20, 171, 531))
        self.perm_8.setFont(font2)
        self.perm_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.perm_8.setAutoFillBackground(False)
        self.perm_8.setFrameShape(QFrame.Shape.NoFrame)
        self.perm_8.setAutoScroll(False)
        self.perm_8.setTabKeyNavigation(True)
        self.perm_8.setRowCount(16)
        self.perm_8.setColumnCount(1)
        self.perm_8.horizontalHeader().setVisible(False)
        self.perm_8.horizontalHeader().setHighlightSections(True)
        self.perm_8.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.perm_8.horizontalHeader().setStretchLastSection(False)
        self.perm_8.verticalHeader().setProperty(u"showSortIndicator", False)
        self.perm_8.verticalHeader().setStretchLastSection(False)
        self.main_top_frame_va_2 = QFrame(self.view_auth_frame_2)
        self.main_top_frame_va_2.setObjectName(u"main_top_frame_va_2")
        self.main_top_frame_va_2.setEnabled(True)
        self.main_top_frame_va_2.setGeometry(QRect(0, 0, 741, 51))
        self.main_top_frame_va_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_top_frame_va_2.setFrameShadow(QFrame.Shadow.Raised)
        self.username_title_va_2 = QLabel(self.main_top_frame_va_2)
        self.username_title_va_2.setObjectName(u"username_title_va_2")
        self.username_title_va_2.setGeometry(QRect(20, 10, 511, 31))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.username_title_va_2.setPalette(palette20)
        self.username_title_va_2.setFont(font3)
        self.username_title_va_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ip_label_va_2 = QLabel(self.main_top_frame_va_2)
        self.ip_label_va_2.setObjectName(u"ip_label_va_2")
        self.ip_label_va_2.setGeometry(QRect(530, 10, 191, 31))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.ip_label_va_2.setPalette(palette21)
        self.ip_label_va_2.setFont(font3)
        self.ip_label_va_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.user_management.addWidget(self.view_auth_widget_ad)
        self.view_login_log_widget_ad = QWidget()
        self.view_login_log_widget_ad.setObjectName(u"view_login_log_widget_ad")
        self.view_login_frame_ad = QFrame(self.view_login_log_widget_ad)
        self.view_login_frame_ad.setObjectName(u"view_login_frame_ad")
        self.view_login_frame_ad.setEnabled(True)
        self.view_login_frame_ad.setGeometry(QRect(0, 0, 741, 601))
        self.view_login_frame_ad.setStyleSheet(u"QLineEdit, QPlainTextEdit {\n"
"	background-color: #1e1f22;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"	color: #ffffff;\n"
"}\n"
"QFrame {\n"
"	background-color: #313338;\n"
"}\n"
"#intro_input{\n"
"	background-color: #1e1f22;\n"
"	color: #ffffff;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#profile_pic_change_btn{\n"
"	background-color: #5865f2;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#profile_pic_del_btn{\n"
"	background-color: #da373c;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#preview_frame {\n"
"	background-color: #111214;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#profile_pic_preview {\n"
"	background-color: rgba(255, 255, 255, 111);\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #2b2d31;\n"
"	color:#ffffff;\n"
"	font: 450 11pt \"\ud504\ub9ac\uc820\ud14c\uc774\uc158\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"	text-align: center;\n"
"	color: rgb(148, 155, 164);\n"
"}")
        self.view_login_frame_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.view_login_frame_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.main_frame_vl_ad = QFrame(self.view_login_frame_ad)
        self.main_frame_vl_ad.setObjectName(u"main_frame_vl_ad")
        self.main_frame_vl_ad.setGeometry(QRect(0, 50, 741, 551))
        self.main_frame_vl_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_vl_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.login_log_widget_ad = QTableWidget(self.main_frame_vl_ad)
        if (self.login_log_widget_ad.columnCount() < 4):
            self.login_log_widget_ad.setColumnCount(4)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.login_log_widget_ad.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.login_log_widget_ad.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.login_log_widget_ad.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.login_log_widget_ad.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        self.login_log_widget_ad.setObjectName(u"login_log_widget_ad")
        self.login_log_widget_ad.setGeometry(QRect(10, 10, 721, 531))
        sizePolicy.setHeightForWidth(self.login_log_widget_ad.sizePolicy().hasHeightForWidth())
        self.login_log_widget_ad.setSizePolicy(sizePolicy)
        self.login_log_widget_ad.setFont(font4)
        self.login_log_widget_ad.setFrameShape(QFrame.Shape.NoFrame)
        self.login_log_widget_ad.setFrameShadow(QFrame.Shadow.Sunken)
        self.login_log_widget_ad.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.login_log_widget_ad.setShowGrid(False)
        self.login_log_widget_ad.setSortingEnabled(False)
        self.login_log_widget_ad.setWordWrap(True)
        self.login_log_widget_ad.setCornerButtonEnabled(True)
        self.login_log_widget_ad.setColumnCount(4)
        self.login_log_widget_ad.horizontalHeader().setVisible(True)
        self.login_log_widget_ad.horizontalHeader().setDefaultSectionSize(181)
        self.login_log_widget_ad.horizontalHeader().setHighlightSections(True)
        self.login_log_widget_ad.verticalHeader().setVisible(False)
        self.main_top_frame_vl_ad = QFrame(self.view_login_frame_ad)
        self.main_top_frame_vl_ad.setObjectName(u"main_top_frame_vl_ad")
        self.main_top_frame_vl_ad.setEnabled(True)
        self.main_top_frame_vl_ad.setGeometry(QRect(0, 0, 741, 51))
        self.main_top_frame_vl_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_top_frame_vl_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.user_id_title_vl_ad = QLabel(self.main_top_frame_vl_ad)
        self.user_id_title_vl_ad.setObjectName(u"user_id_title_vl_ad")
        self.user_id_title_vl_ad.setGeometry(QRect(20, 10, 511, 31))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.user_id_title_vl_ad.setPalette(palette22)
        self.user_id_title_vl_ad.setFont(font3)
        self.user_id_title_vl_ad.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.user_management.addWidget(self.view_login_log_widget_ad)
        self.profile_view_widget_ad = QWidget()
        self.profile_view_widget_ad.setObjectName(u"profile_view_widget_ad")
        self.profile_view_widget_ad.setStyleSheet(u"QFrame {\n"
"	background-color: #313338;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	font: 500 12pt \"\ud504\ub9ac\uc820\ud14c\uc774\uc158\";\n"
"	color: #949ba4;\n"
"}\n"
"\n"
"QPushButton:checked, QPushButton:hover {\n"
"	background-color: #404249;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit, QPlainTextEdit {\n"
"	background-color: #1e1f22;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#preview_frame_ad {\n"
"	background-color: #111214;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#profile_pic_ad {\n"
"	background-color: rgba(255, 255, 255, 111);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#profile_apply_frame {\n"
"	background-color: #111214;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#apply_inform_label {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#reset_btn {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#acc_del_btn_ad {\n"
""
                        "	background-color: rgba(255, 255, 255, 0);\n"
"	color: #da373c;\n"
"	border: 1px solid #da373c;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#acc_del_btn_ad:hover, #acc_del_btn_ad:pressed {\n"
"	background-color: #da373c;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#acc_sus_btn_ad {\n"
"	background-color: #da373c;\n"
"	color: #ffffff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#intro_edit_ad{\n"
"	background-color: #1e1f22;\n"
"	color: #ffffff;\n"
"	border: 1px solid;\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#preview_frame_ad {\n"
"	background-color: #111214;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#profile_pic_preview_ad {\n"
"	background-color: rgba(255, 255, 255, 111);\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"#reset_btn_ad {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#profile_apply_btn_ad {\n"
"	background-color: #248045;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#user_sel_scroll_area {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb"
                        "a(255, 255, 255, 0);\n"
"}")
        self.profile_view_frame_ad = QFrame(self.profile_view_widget_ad)
        self.profile_view_frame_ad.setObjectName(u"profile_view_frame_ad")
        self.profile_view_frame_ad.setEnabled(True)
        self.profile_view_frame_ad.setGeometry(QRect(0, 0, 741, 601))
        self.profile_view_frame_ad.setFont(font5)
        self.profile_view_frame_ad.setStyleSheet(u"")
        self.profile_view_frame_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.profile_view_frame_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.profile_main_frame_ad = QFrame(self.profile_view_frame_ad)
        self.profile_main_frame_ad.setObjectName(u"profile_main_frame_ad")
        self.profile_main_frame_ad.setGeometry(QRect(0, 50, 741, 551))
        self.profile_main_frame_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.profile_main_frame_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.view_frame_ad = QFrame(self.profile_main_frame_ad)
        self.view_frame_ad.setObjectName(u"view_frame_ad")
        self.view_frame_ad.setGeometry(QRect(40, 20, 341, 241))
        self.view_frame_ad.setStyleSheet(u"QPushButton {\n"
"	background-color: #313338;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: #ffffff;\n"
"}")
        self.view_frame_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.view_frame_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.profile_pic_ad = QPushButton(self.view_frame_ad)
        self.profile_pic_ad.setObjectName(u"profile_pic_ad")
        self.profile_pic_ad.setGeometry(QRect(10, 20, 71, 71))
        self.profile_pic_ad.setIcon(icon)
        self.profile_pic_ad.setIconSize(QSize(32, 32))
        self.profile_pic_ad.setAutoRepeatDelay(299)
        self.profile_pic_ad.setFlat(True)
        self.logo_preview_2 = QLabel(self.view_frame_ad)
        self.logo_preview_2.setObjectName(u"logo_preview_2")
        self.logo_preview_2.setGeometry(QRect(260, 20, 61, 61))
        self.logo_preview_2.setPixmap(QPixmap(u"../../Users/59613/Downloads/CAB (2).png"))
        self.logo_preview_2.setScaledContents(True)
        self.username_edit_ad = QLineEdit(self.view_frame_ad)
        self.username_edit_ad.setObjectName(u"username_edit_ad")
        self.username_edit_ad.setGeometry(QRect(90, 30, 231, 22))
        self.intro_edit_ad = QPlainTextEdit(self.view_frame_ad)
        self.intro_edit_ad.setObjectName(u"intro_edit_ad")
        self.intro_edit_ad.setGeometry(QRect(20, 100, 301, 91))
        self.auth_sel_box = QComboBox(self.view_frame_ad)
        self.auth_sel_box.addItem("")
        self.auth_sel_box.addItem("")
        self.auth_sel_box.addItem("")
        self.auth_sel_box.addItem("")
        self.auth_sel_box.addItem("")
        self.auth_sel_box.addItem("")
        self.auth_sel_box.setObjectName(u"auth_sel_box")
        self.auth_sel_box.setGeometry(QRect(20, 200, 131, 24))
        self.user_id_edit_ad = QLabel(self.view_frame_ad)
        self.user_id_edit_ad.setObjectName(u"user_id_edit_ad")
        self.user_id_edit_ad.setGeometry(QRect(90, 60, 231, 16))
        self.user_id_edit_ad.setFont(font4)
        self.adi_log_edit = QPlainTextEdit(self.profile_main_frame_ad)
        self.adi_log_edit.setObjectName(u"adi_log_edit")
        self.adi_log_edit.setGeometry(QRect(40, 430, 661, 91))
        self.user_list_ad = QTableWidget(self.profile_main_frame_ad)
        if (self.user_list_ad.columnCount() < 2):
            self.user_list_ad.setColumnCount(2)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.user_list_ad.setHorizontalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.user_list_ad.setHorizontalHeaderItem(1, __qtablewidgetitem49)
        self.user_list_ad.setObjectName(u"user_list_ad")
        self.user_list_ad.setEnabled(True)
        self.user_list_ad.setGeometry(QRect(400, 20, 301, 401))
        palette23 = QPalette()
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush4)
        brush6 = QBrush(QColor(45, 47, 51, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush6)
        brush7 = QBrush(QColor(37, 39, 42, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush7)
        brush8 = QBrush(QColor(15, 16, 17, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush8)
        brush9 = QBrush(QColor(20, 21, 23, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush9)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette23.setBrush(QPalette.Active, QPalette.BrightText, brush5)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        brush11 = QBrush(QColor(15, 15, 17, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush11)
        brush12 = QBrush(QColor(255, 255, 220, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipBase, brush12)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush13 = QBrush(QColor(255, 255, 255, 127))
        brush13.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette23.setBrush(QPalette.Active, QPalette.Accent, brush10)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush7)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush8)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush9)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.BrightText, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush11)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.Accent, brush10)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush7)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush9)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.BrightText, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        brush14 = QBrush(QColor(30, 31, 34, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush14)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush12)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
        brush15 = QBrush(QColor(15, 16, 17, 127))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        brush16 = QBrush(QColor(21, 22, 24, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Disabled, QPalette.Accent, brush16)
        self.user_list_ad.setPalette(palette23)
        self.user_list_ad.setRowCount(0)
        self.user_list_ad.horizontalHeader().setCascadingSectionResizes(False)
        self.user_list_ad.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.user_list_ad.horizontalHeader().setStretchLastSection(True)
        self.user_list_ad.verticalHeader().setVisible(False)
        self.user_list_ad.verticalHeader().setHighlightSections(False)
        self.control_frame_ad = QFrame(self.profile_main_frame_ad)
        self.control_frame_ad.setObjectName(u"control_frame_ad")
        self.control_frame_ad.setGeometry(QRect(30, 270, 361, 151))
        self.control_frame_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.control_frame_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.acc_sus_btn_ad = QPushButton(self.control_frame_ad)
        self.acc_sus_btn_ad.setObjectName(u"acc_sus_btn_ad")
        self.acc_sus_btn_ad.setGeometry(QRect(10, 50, 341, 41))
        self.acc_del_btn_ad = QPushButton(self.control_frame_ad)
        self.acc_del_btn_ad.setObjectName(u"acc_del_btn_ad")
        self.acc_del_btn_ad.setGeometry(QRect(10, 100, 341, 41))
        self.apply_frame_ad = QFrame(self.control_frame_ad)
        self.apply_frame_ad.setObjectName(u"apply_frame_ad")
        self.apply_frame_ad.setGeometry(QRect(0, 0, 361, 51))
        self.apply_frame_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.apply_frame_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.profile_apply_btn_ad = QPushButton(self.apply_frame_ad)
        self.profile_apply_btn_ad.setObjectName(u"profile_apply_btn_ad")
        self.profile_apply_btn_ad.setGeometry(QRect(100, 10, 251, 31))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        brush17 = QBrush(QColor(36, 128, 69, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush17)
        brush18 = QBrush(QColor(255, 255, 255, 128))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.profile_apply_btn_ad.setPalette(palette24)
        font8 = QFont()
        font8.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font8.setPointSize(12)
        font8.setWeight(QFont.Medium)
        font8.setItalic(False)
        self.profile_apply_btn_ad.setFont(font8)
        self.reset_btn_ad = QPushButton(self.apply_frame_ad)
        self.reset_btn_ad.setObjectName(u"reset_btn_ad")
        self.reset_btn_ad.setGeometry(QRect(10, 10, 81, 31))
        self.reset_btn_ad.setFont(font8)
        self.profile_main_top_frame_ad = QFrame(self.profile_view_frame_ad)
        self.profile_main_top_frame_ad.setObjectName(u"profile_main_top_frame_ad")
        self.profile_main_top_frame_ad.setEnabled(True)
        self.profile_main_top_frame_ad.setGeometry(QRect(0, 0, 741, 51))
        self.profile_main_top_frame_ad.setFrameShape(QFrame.Shape.StyledPanel)
        self.profile_main_top_frame_ad.setFrameShadow(QFrame.Shadow.Raised)
        self.cp_username_title_ad = QLabel(self.profile_main_top_frame_ad)
        self.cp_username_title_ad.setObjectName(u"cp_username_title_ad")
        self.cp_username_title_ad.setGeometry(QRect(20, 10, 511, 31))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.cp_username_title_ad.setPalette(palette25)
        self.cp_username_title_ad.setFont(font3)
        self.cp_username_title_ad.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.user_management.addWidget(self.profile_view_widget_ad)
        self.select_menu_widget.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.select_menu_widget.raise_()
        self.left_menubar.raise_()

        self.retranslateUi(MainWindow)

        self.select_menu_widget.setCurrentIndex(2)
        self.user_parent_widget.setCurrentIndex(1)
        self.user_management.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.profile_btn.setText("")
        self.chat_btn.setText("")
        self.admin_btn.setText("")
        self.profile_set_btn.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\ud544 \uc124\uc815", None))
        self.view_auth_btn.setText(QCoreApplication.translate("MainWindow", u"\uad8c\ud55c \ubcf4\uae30", None))
        self.data_priv_btn.setText(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130 \ubc0f \uac1c\uc778\uc815\ubcf4", None))
        self.login_log_btn.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778 \uae30\ub85d", None))
        self.acc_del_btn.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815 \uc0ad\uc81c", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc544\uc6c3", None))
        self.username_title_up.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        ___qtablewidgetitem = self.perm_1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\ud5c8\uc6a9 \uc5ec\ubd80", None));
        ___qtablewidgetitem1 = self.perm_1.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc18d", None));
        ___qtablewidgetitem2 = self.perm_1.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\ub78c", None));

        __sortingEnabled = self.perm_1.isSortingEnabled()
        self.perm_1.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.perm_1.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"O", None));
        ___qtablewidgetitem4 = self.perm_1.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"X", None));
        self.perm_1.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem5 = self.perm_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\ud5c8\uc6a9 \uc5ec\ubd80", None));
        ___qtablewidgetitem6 = self.perm_2.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc18d", None));
        ___qtablewidgetitem7 = self.perm_2.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\ub78c", None));

        __sortingEnabled1 = self.perm_2.isSortingEnabled()
        self.perm_2.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.perm_2.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"O", None));
        ___qtablewidgetitem9 = self.perm_2.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"X", None));
        self.perm_2.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem10 = self.perm_3.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\ud5c8\uc6a9 \uc5ec\ubd80", None));
        ___qtablewidgetitem11 = self.perm_3.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc18d", None));
        ___qtablewidgetitem12 = self.perm_3.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\ub78c", None));

        __sortingEnabled2 = self.perm_3.isSortingEnabled()
        self.perm_3.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.perm_3.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"O", None));
        ___qtablewidgetitem14 = self.perm_3.item(1, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"X", None));
        self.perm_3.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem15 = self.perm_4.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\ud5c8\uc6a9 \uc5ec\ubd80", None));
        ___qtablewidgetitem16 = self.perm_4.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc18d", None));
        ___qtablewidgetitem17 = self.perm_4.verticalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\ub78c", None));

        __sortingEnabled3 = self.perm_4.isSortingEnabled()
        self.perm_4.setSortingEnabled(False)
        ___qtablewidgetitem18 = self.perm_4.item(0, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"O", None));
        ___qtablewidgetitem19 = self.perm_4.item(1, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"X", None));
        self.perm_4.setSortingEnabled(__sortingEnabled3)

        self.username_title_va.setText(QCoreApplication.translate("MainWindow", u"{USERNAME}\uc758 \uad8c\ud55c \uc5f4\ub78c", None))
        self.ip_label_va.setText(QCoreApplication.translate("MainWindow", u"IP  255.255.255.255", None))
        ___qtablewidgetitem20 = self.login_log_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04", None));
        ___qtablewidgetitem21 = self.login_log_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"OS", None));
        ___qtablewidgetitem22 = self.login_log_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\uad6d\uac00", None));
        ___qtablewidgetitem23 = self.login_log_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        self.user_id_title_vl.setText(QCoreApplication.translate("MainWindow", u"{USERID} \uacc4\uc815\uc758 \ub85c\uadf8\uc778 \uae30\ub85d", None))
        self.ip_label_vl.setText(QCoreApplication.translate("MainWindow", u"IP  255.255.255.255", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"\ubcc4\uba85", None))
        self.username_input.setText("")
        self.intro_label.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uac1c", None))
        self.intro_input.setPlainText("")
        self.profile_pic_label.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\ud544 \uc0ac\uc9c4", None))
        self.profile_pic_change_btn.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc9c4 \ubcc0\uacbd\ud558\uae30", None))
        self.profile_pic_del_btn.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc9c4 \uc81c\uac70", None))
        self.preview_label.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\ub9ac\ubcf4\uae30", None))
        self.profile_pic_preview.setText("")
        self.username_preview.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        self.user_id_preview.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        self.intro_preview.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.auth_preview.setText(QCoreApplication.translate("MainWindow", u"\uc720\uc800", None))
        self.ip_preview.setText(QCoreApplication.translate("MainWindow", u"255.255.255.255", None))
        self.logo_preview.setText("")
        self.apply_inform_label.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5\ud558\uc9c0 \uc54a\uc740 \ubcc0\uacbd\uc0ac\ud56d\uc774 \uc788\uc2b5\ub2c8\ub2e4.", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uc124\uc815", None))
        self.profile_apply_btn.setText(QCoreApplication.translate("MainWindow", u"\ubcc0\uacbd\uc0ac\ud56d \uc800\uc7a5\ud558\uae30", None))
        self.username_title_ps.setText(QCoreApplication.translate("MainWindow", u"{USERNAME}\uc758 \ud504\ub85c\ud544", None))
        self.ip_label_ps.setText(QCoreApplication.translate("MainWindow", u"IP  255.255.255.255", None))
        self.chat_search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9...", None))
        self.chat_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uba54\uc138\uc9c0 \ubcf4\ub0b4\uae30", None))
        self.chat_profile_img.setText("")
        self.cp_username_title.setText(QCoreApplication.translate("MainWindow", u"{username}", None))
        self.profile_view_btn_ad.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\ud544 \ubcf4\uae30", None))
        self.login_log_btn_ad.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778 \uae30\ub85d", None))
        self.username_title_ad.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        ___qtablewidgetitem24 = self.perm_5.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\ud5c8\uc6a9 \uc5ec\ubd80", None));
        ___qtablewidgetitem25 = self.perm_5.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc18d", None));
        ___qtablewidgetitem26 = self.perm_5.verticalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\ub78c", None));

        __sortingEnabled4 = self.perm_5.isSortingEnabled()
        self.perm_5.setSortingEnabled(False)
        ___qtablewidgetitem27 = self.perm_5.item(0, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"O", None));
        ___qtablewidgetitem28 = self.perm_5.item(1, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"X", None));
        self.perm_5.setSortingEnabled(__sortingEnabled4)

        ___qtablewidgetitem29 = self.perm_6.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\ud5c8\uc6a9 \uc5ec\ubd80", None));
        ___qtablewidgetitem30 = self.perm_6.verticalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc18d", None));
        ___qtablewidgetitem31 = self.perm_6.verticalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\ub78c", None));

        __sortingEnabled5 = self.perm_6.isSortingEnabled()
        self.perm_6.setSortingEnabled(False)
        ___qtablewidgetitem32 = self.perm_6.item(0, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"O", None));
        ___qtablewidgetitem33 = self.perm_6.item(1, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"X", None));
        self.perm_6.setSortingEnabled(__sortingEnabled5)

        ___qtablewidgetitem34 = self.perm_7.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\ud5c8\uc6a9 \uc5ec\ubd80", None));
        ___qtablewidgetitem35 = self.perm_7.verticalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc18d", None));
        ___qtablewidgetitem36 = self.perm_7.verticalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\ub78c", None));

        __sortingEnabled6 = self.perm_7.isSortingEnabled()
        self.perm_7.setSortingEnabled(False)
        ___qtablewidgetitem37 = self.perm_7.item(0, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"O", None));
        ___qtablewidgetitem38 = self.perm_7.item(1, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"X", None));
        self.perm_7.setSortingEnabled(__sortingEnabled6)

        ___qtablewidgetitem39 = self.perm_8.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\ud5c8\uc6a9 \uc5ec\ubd80", None));
        ___qtablewidgetitem40 = self.perm_8.verticalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc18d", None));
        ___qtablewidgetitem41 = self.perm_8.verticalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\ub78c", None));

        __sortingEnabled7 = self.perm_8.isSortingEnabled()
        self.perm_8.setSortingEnabled(False)
        ___qtablewidgetitem42 = self.perm_8.item(0, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"O", None));
        ___qtablewidgetitem43 = self.perm_8.item(1, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"X", None));
        self.perm_8.setSortingEnabled(__sortingEnabled7)

        self.username_title_va_2.setText(QCoreApplication.translate("MainWindow", u"{USERNAME}\uc758 \uad8c\ud55c \uc5f4\ub78c", None))
        self.ip_label_va_2.setText(QCoreApplication.translate("MainWindow", u"IP  255.255.255.255", None))
        ___qtablewidgetitem44 = self.login_log_widget_ad.horizontalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04", None));
        ___qtablewidgetitem45 = self.login_log_widget_ad.horizontalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"OS", None));
        ___qtablewidgetitem46 = self.login_log_widget_ad.horizontalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\uad6d\uac00", None));
        ___qtablewidgetitem47 = self.login_log_widget_ad.horizontalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        self.user_id_title_vl_ad.setText(QCoreApplication.translate("MainWindow", u"{USERID} \uacc4\uc815\uc758 \ub85c\uadf8\uc778 \uae30\ub85d", None))
        self.profile_pic_ad.setText("")
        self.logo_preview_2.setText("")
        self.username_edit_ad.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790\uc758 \uc774\ub984(\ubcc4\uba85)\uc774 \ud45c\uc2dc\ub429\ub2c8\ub2e4.", None))
        self.intro_edit_ad.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790\uc758 \uc18c\uac1c\ubb38\uc774 \ud45c\uc2dc\ub429\ub2c8\ub2e4.", None))
        self.auth_sel_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc720\uc800", None))
        self.auth_sel_box.setItemText(1, QCoreApplication.translate("MainWindow", u"VIP", None))
        self.auth_sel_box.setItemText(2, QCoreApplication.translate("MainWindow", u"\uad00\ub9ac\uc790", None))
        self.auth_sel_box.setItemText(3, QCoreApplication.translate("MainWindow", u"\ucd5c\uace0 \uad00\ub9ac\uc790", None))
        self.auth_sel_box.setItemText(4, QCoreApplication.translate("MainWindow", u"\uc784\uc2dc \ucc28\ub2e8", None))
        self.auth_sel_box.setItemText(5, QCoreApplication.translate("MainWindow", u"\uc601\uad6c \uc815\uc9c0", None))

        self.user_id_edit_ad.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790\uc758 ID\uac00 \ud45c\uc2dc\ub429\ub2c8\ub2e4. ID\ub294 \ubcc0\uacbd\uc774 \ubd88\uac00\ud569\ub2c8\ub2e4.", None))
        self.adi_log_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0 \uae30\ub85d \ub610\ub294 \ucd94\uac00 \ucca8\uc5b8 \uc0ac\ud56d\uc774 \uae30\ub85d\ub429\ub2c8\ub2e4. \uad00\ub9ac\uc790\ub294 \uc774\ub97c \uc218\uc815\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4.", None))
        ___qtablewidgetitem48 = self.user_list_ad.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem49 = self.user_list_ad.horizontalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984", None));
        self.acc_sus_btn_ad.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815 \uc784\uc2dc / \uc601\uad6c \uc815\uc9c0", None))
        self.acc_del_btn_ad.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815 \uc0ad\uc81c", None))
        self.profile_apply_btn_ad.setText(QCoreApplication.translate("MainWindow", u"\ubcc0\uacbd\uc0ac\ud56d \uc800\uc7a5\ud558\uae30", None))
        self.reset_btn_ad.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uc124\uc815", None))
        self.cp_username_title_ad.setText(QCoreApplication.translate("MainWindow", u"{USERNAME}\uc758 \ud504\ub85c\ud544", None))
    # retranslateUi

