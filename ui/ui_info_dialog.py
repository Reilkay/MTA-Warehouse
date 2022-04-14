# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_info_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_info_dialog(object):
    def setupUi(self, info_dialog):
        if not info_dialog.objectName():
            info_dialog.setObjectName(u"info_dialog")
        info_dialog.resize(199, 218)
        self.verticalLayout = QVBoxLayout(info_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(info_dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(info_dialog)

        QMetaObject.connectSlotsByName(info_dialog)
    # setupUi

    def retranslateUi(self, info_dialog):
        info_dialog.setWindowTitle(QCoreApplication.translate("info_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("info_dialog", u"TextLabel", None))
    # retranslateUi

