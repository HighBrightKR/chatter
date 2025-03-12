# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        if not login_dialog.objectName():
            login_dialog.setObjectName(u"login_dialog")
        login_dialog.setEnabled(True)
        login_dialog.resize(400, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_dialog.sizePolicy().hasHeightForWidth())
        login_dialog.setSizePolicy(sizePolicy)
        login_dialog.setStyleSheet(u"#id_input, #pw_input {\n"
"    border: 1px solid gray;  /* \ud68c\uc0c9 \ud14c\ub450\ub9ac */\n"
"    border-radius: 5px;  /* \ubaa8\uc11c\ub9ac \ub465\uae00\uac8c (\uc120\ud0dd \uc0ac\ud56d) */\n"
"    padding: 10px;  /* \ub0b4\ubd80 \uc5ec\ubc31 */\n"
"}\n"
"\n"
"#main_frame {\n"
"    border-radius: 20px;  /* \ubaa8\uc11c\ub9ac\ub97c \ub465\uae00\uac8c (\ud53d\uc140 \ub2e8\uc704) */\n"
"    background-color: #ffffff;  /* \ubc30\uacbd\uc0c9 (\ud770\uc0c9) */\n"
"}\n"
"\n"
"#id_find:hover, #pw_find:hover {\n"
"    text-decoration: underline;\n"
"    color: #000000;\n"
"    cursor: pointer;\n"

"}\n"
"\n"
"#exit_btn {\n"
"    background-color: #e74c3c;  /* \ubd89\uc740 \uc0c9 */\n"
"    color: white;  /* \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 */\n"
"    border: none;  /* \ud14c\ub450\ub9ac \uc5c6\uc560\uae30 (\uc120\ud0dd \uc0ac\ud56d) */\n"
"    padding: 10px 20px;  /* \ub0b4\ubd80 \uc5ec\ubc31 */\n"
"    border-radius: 5px;  /* \ub465\uadfc \ud14c\ub450\ub9ac */\n"
"}")
        self.main_frame = QFrame(login_dialog)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(-1, 9, 400, 591))
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.login_label = QLabel(self.main_frame)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(10, 30, 381, 181))
        font = QFont()
        font.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font.setPointSize(36)
        font.setBold(True)
        self.login_label.setFont(font)
        self.login_label.setTextFormat(Qt.TextFormat.AutoText)
        self.login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_label.setWordWrap(True)
        self.login_btn = QPushButton(self.main_frame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(20, 370, 361, 41))
        palette = QPalette()
        brush = QBrush(QColor(36, 107, 235, 179))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 228))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(249, 249, 249, 77))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 92))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.login_btn.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.login_btn.setFont(font1)
        self.login_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_btn.setMouseTracking(False)
        self.login_btn.setAutoDefault(True)
        self.login_btn.setFlat(True)
        self.pw_input = QLineEdit(self.main_frame)
        self.pw_input.setObjectName(u"id_input")
        self.pw_input.setGeometry(QRect(20, 300, 361, 41))
        sizePolicy.setHeightForWidth(self.pw_input.sizePolicy().hasHeightForWidth())
        self.pw_input.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font2.setPointSize(11)
        self.pw_input.setFont(font2)
        self.pw_input.setMaxLength(16)
        self.pw_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.id_input = QLineEdit(self.main_frame)
        self.id_input.setObjectName(u"id_input")
        self.id_input.setGeometry(QRect(20, 230, 361, 41))
        sizePolicy.setHeightForWidth(self.id_input.sizePolicy().hasHeightForWidth())
        self.id_input.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font3.setPointSize(12)
        self.id_input.setFont(font3)
        self.id_input.setToolTipDuration(-1)
        self.id_input.setMaxLength(16)
        self.id_input.setEchoMode(QLineEdit.EchoMode.Normal)
        self.id_input.setCursorPosition(0)
        self.id_input.setClearButtonEnabled(False)
        self.id_find = QLabel(self.main_frame)
        self.id_find.setObjectName(u"id_find")
        self.id_find.setGeometry(QRect(110, 430, 81, 16))
        self.id_find.setFont(font3)
        self.id_find.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pw_find = QLabel(self.main_frame)
        self.pw_find.setObjectName(u"pw_find")
        self.pw_find.setGeometry(QRect(200, 430, 81, 16))
        self.pw_find.setFont(font3)
        self.pw_find.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exit_btn = QPushButton(self.main_frame)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(20, 520, 361, 41))
        palette1 = QPalette()
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        brush5 = QBrush(QColor(231, 76, 60, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.exit_btn.setPalette(palette1)
        self.exit_btn.setFont(font1)
        self.exit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exit_btn.setMouseTracking(False)
        self.exit_btn.setAutoDefault(True)
        self.exit_btn.setFlat(True)

        self.retranslateUi(login_dialog)

        self.login_btn.setDefault(False)
        self.exit_btn.setDefault(False)


        QMetaObject.connectSlotsByName(login_dialog)
    # setupUi

    def retranslateUi(self, login_dialog):
        login_dialog.setWindowTitle(QCoreApplication.translate("login_dialog", u"Dialog", None))
        self.login_label.setText(QCoreApplication.translate("login_dialog", u"\ud1b5\ud569 \ub85c\uadf8\uc778", None))
        self.login_btn.setText(QCoreApplication.translate("login_dialog", u"\ub85c\uadf8\uc778", None))
        self.id_input.setText("")
        self.id_input.setPlaceholderText(QCoreApplication.translate("login_dialog", u"\ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud558\uc138\uc694", None))
        self.pw_input.setInputMask("")
        self.pw_input.setText("")
        self.pw_input.setPlaceholderText(QCoreApplication.translate("login_dialog", u"\uc544\uc774\ub514\ub97c \uc785\ub825\ud558\uc138\uc694", None))
        self.id_find.setText(QCoreApplication.translate("login_dialog", u"\uc544\uc774\ub514 \ucc3e\uae30", None))
        self.pw_find.setText(QCoreApplication.translate("login_dialog", u"\ube44\ubc00\ubc88\ud638 \ucc3e\uae30", None))
        self.exit_btn.setText(QCoreApplication.translate("login_dialog", u"\uc885\ub8cc", None))
    # retranslateUi

