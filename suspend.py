# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suspend.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_suspend_form(object):
    def setupUi(self, suspend_form):
        if not suspend_form.objectName():
            suspend_form.setObjectName(u"suspend_form")
        suspend_form.resize(351, 400)
        suspend_form.setStyleSheet(u"QWidget {background-color: #313338;}\n"
"QLabel {color: #ffffff;}\n"
"QComboBox {color: #ffffff;}\n"
"QPlainTextEdit{color: #ffffff; background-color: #1e1f22; border-radius: 10px;}\n"
"QPushButton{background-color: #da373c; color: #ffffff;}")
        self.username = QLabel(suspend_form)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(10, 10, 331, 21))
        font = QFont()
        font.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font.setPointSize(14)
        self.username.setFont(font)
        self.user_id = QLabel(suspend_form)
        self.user_id.setObjectName(u"user_id")
        self.user_id.setGeometry(QRect(10, 40, 331, 16))
        font1 = QFont()
        font1.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font1.setPointSize(10)
        self.user_id.setFont(font1)
        self.comboBox = QComboBox(suspend_form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(80, 70, 261, 31))
        self.label_3 = QLabel(suspend_form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 70, 71, 31))
        font2 = QFont()
        font2.setFamilies([u"\ud504\ub9ac\uc820\ud14c\uc774\uc158"])
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.reason_edit = QPlainTextEdit(suspend_form)
        self.reason_edit.setObjectName(u"reason_edit")
        self.reason_edit.setGeometry(QRect(10, 130, 331, 211))
        self.label_4 = QLabel(suspend_form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 100, 71, 31))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.suspend_btn = QPushButton(suspend_form)
        self.suspend_btn.setObjectName(u"suspend_btn")
        self.suspend_btn.setGeometry(QRect(10, 350, 331, 41))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(218, 55, 60, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
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
        self.suspend_btn.setPalette(palette)
        self.suspend_btn.setFont(font)

        self.retranslateUi(suspend_form)

        QMetaObject.connectSlotsByName(suspend_form)
    # setupUi

    def retranslateUi(self, suspend_form):
        suspend_form.setWindowTitle(QCoreApplication.translate("suspend_form", u"\uacc4\uc815 \uc815\uc9c0", None))
        self.username.setText(QCoreApplication.translate("suspend_form", u"\uc720\uc800\uba85", None))
        self.user_id.setText(QCoreApplication.translate("suspend_form", u"\uc720\uc800 ID", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("suspend_form", u"1\uc77c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("suspend_form", u"3\uc77c", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("suspend_form", u"5\uc77c", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("suspend_form", u"7\uc77c", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("suspend_form", u"14\uc77c", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("suspend_form", u"30\uc77c", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("suspend_form", u"90\uc77c", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("suspend_form", u"365\uc77c", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("suspend_form", u"\uc601\uad6c \uc815\uc9c0", None))

        self.comboBox.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("suspend_form", u"\uc815\uc9c0\uc77c \uc218", None))
        self.label_4.setText(QCoreApplication.translate("suspend_form", u"\uc0ac\uc720", None))
        self.suspend_btn.setText(QCoreApplication.translate("suspend_form", u"\uacc4\uc815 \uc784\uc2dc / \uc601\uad6c \uc815\uc9c0", None))
    # retranslateUi

