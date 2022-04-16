# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_setting_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_setting_dialog(object):
    def setupUi(self, setting_dialog):
        if not setting_dialog.objectName():
            setting_dialog.setObjectName(u"setting_dialog")
        setting_dialog.resize(695, 453)
        self.gridLayout = QGridLayout(setting_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(setting_dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.save_position = QComboBox(self.frame)
        self.save_position.setObjectName(u"save_position")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_position.sizePolicy().hasHeightForWidth())
        self.save_position.setSizePolicy(sizePolicy1)
        self.save_position.setMinimumSize(QSize(150, 0))

        self.verticalLayout_2.addWidget(self.save_position)

        self.save_path = QLineEdit(self.frame)
        self.save_path.setObjectName(u"save_path")
        sizePolicy1.setHeightForWidth(self.save_path.sizePolicy().hasHeightForWidth())
        self.save_path.setSizePolicy(sizePolicy1)
        self.save_path.setMinimumSize(QSize(300, 0))

        self.verticalLayout_2.addWidget(self.save_path)

        self.directory_rename_rule = QLineEdit(self.frame)
        self.directory_rename_rule.setObjectName(u"directory_rename_rule")
        sizePolicy1.setHeightForWidth(self.directory_rename_rule.sizePolicy().hasHeightForWidth())
        self.directory_rename_rule.setSizePolicy(sizePolicy1)
        self.directory_rename_rule.setMinimumSize(QSize(300, 0))

        self.verticalLayout_2.addWidget(self.directory_rename_rule)

        self.auto_rename = QComboBox(self.frame)
        self.auto_rename.setObjectName(u"auto_rename")
        sizePolicy1.setHeightForWidth(self.auto_rename.sizePolicy().hasHeightForWidth())
        self.auto_rename.setSizePolicy(sizePolicy1)
        self.auto_rename.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_2.addWidget(self.auto_rename)

        self.auto_rename_rule = QLineEdit(self.frame)
        self.auto_rename_rule.setObjectName(u"auto_rename_rule")
        self.auto_rename_rule.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_2.addWidget(self.auto_rename_rule)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        icon = QIcon()
        icon.addFile(u":/resources/icon/warehouse.svg", QSize(), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(setting_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(setting_dialog)
        self.buttonBox.accepted.connect(setting_dialog.accept)
        self.buttonBox.rejected.connect(setting_dialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(setting_dialog)
    # setupUi

    def retranslateUi(self, setting_dialog):
        setting_dialog.setWindowTitle(QCoreApplication.translate("setting_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("setting_dialog", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("setting_dialog", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("setting_dialog", u"\u76ee\u5f55\u547d\u540d\u89c4\u5219", None))
        self.label_4.setText(QCoreApplication.translate("setting_dialog", u"\u6587\u4ef6\u91cd\u547d\u540d", None))
        self.label_5.setText(QCoreApplication.translate("setting_dialog", u"\u6587\u4ef6\u547d\u540d\u89c4\u5219", None))
        self.label_6.setText(QCoreApplication.translate("setting_dialog", u"\u5f53\u4fdd\u5b58\u4f4d\u7f6e\u4e3acustom\u65f6\uff0c\u9700\u8981\u586b\u5199\u4fdd\u5b58\u8def\u5f84", None))
        self.label_9.setText(QCoreApplication.translate("setting_dialog", u"\u4fdd\u5b58\u8def\u5f84\u65e0\u6548\u65f6\u81ea\u52a8\u4f7f\u7528\u9ed8\u8ba4\u8def\u5f84", None))
        self.label_8.setText(QCoreApplication.translate("setting_dialog", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("setting_dialog", u"\u662f\u5426\u81ea\u52a8\u5c06\u6dfb\u52a0\u7684\u5267\u96c6\u91cd\u547d\u540d\u4e3a\u6807\u51c6\u683c\u5f0f", None))
        self.label_7.setText(QCoreApplication.translate("setting_dialog", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("setting_dialog", u"\u4ed3\u5e93\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("setting_dialog", u"\u663e\u793a\u8bbe\u7f6e", None))
    # retranslateUi

