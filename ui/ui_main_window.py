# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QSizePolicy,
    QSpacerItem, QToolBar, QToolButton, QVBoxLayout,
    QWidget)

from frame.filter_frame import FilterFrame
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 604)
        self.new_item = QAction(MainWindow)
        self.new_item.setObjectName(u"new_item")
        icon = QIcon()
        icon.addFile(u":/resources/icon/new.svg", QSize(), QIcon.Normal, QIcon.On)
        self.new_item.setIcon(icon)
        self.delete_item = QAction(MainWindow)
        self.delete_item.setObjectName(u"delete_item")
        icon1 = QIcon()
        icon1.addFile(u":/resources/icon/delete.svg", QSize(), QIcon.Normal, QIcon.On)
        self.delete_item.setIcon(icon1)
        self.update = QAction(MainWindow)
        self.update.setObjectName(u"update")
        icon2 = QIcon()
        icon2.addFile(u":/resources/icon/update.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update.setIcon(icon2)
        self.import_file = QAction(MainWindow)
        self.import_file.setObjectName(u"import_file")
        icon3 = QIcon()
        icon3.addFile(u":/resources/icon/import.svg", QSize(), QIcon.Normal, QIcon.On)
        self.import_file.setIcon(icon3)
        self.export_file = QAction(MainWindow)
        self.export_file.setObjectName(u"export_file")
        icon4 = QIcon()
        icon4.addFile(u":/resources/icon/export.svg", QSize(), QIcon.Normal, QIcon.On)
        self.export_file.setIcon(icon4)
        self.export_excel = QAction(MainWindow)
        self.export_excel.setObjectName(u"export_excel")
        icon5 = QIcon()
        icon5.addFile(u":/resources/icon/export2excel.svg", QSize(), QIcon.Normal, QIcon.On)
        self.export_excel.setIcon(icon5)
        self.star_list = QAction(MainWindow)
        self.star_list.setObjectName(u"star_list")
        icon6 = QIcon()
        icon6.addFile(u":/resources/icon/star.svg", QSize(), QIcon.Normal, QIcon.On)
        self.star_list.setIcon(icon6)
        self.setting = QAction(MainWindow)
        self.setting.setObjectName(u"setting")
        icon7 = QIcon()
        icon7.addFile(u":/resources/icon/setting.svg", QSize(), QIcon.Normal, QIcon.On)
        self.setting.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.filter_frame = FilterFrame(self.centralwidget)
        self.filter_frame.setObjectName(u"filter_frame")
        self.filter_frame.setFrameShape(QFrame.StyledPanel)
        self.filter_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.filter_frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filter_button = QToolButton(self.centralwidget)
        self.filter_button.setObjectName(u"filter_button")
        self.filter_button.setStyleSheet(u"border-style:flat;")
        icon8 = QIcon()
        icon8.addFile(u":/resources/icon/filter.svg", QSize(), QIcon.Normal, QIcon.On)
        self.filter_button.setIcon(icon8)
        self.filter_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.filter_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.search_text = QLineEdit(self.centralwidget)
        self.search_text.setObjectName(u"search_text")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_text.sizePolicy().hasHeightForWidth())
        self.search_text.setSizePolicy(sizePolicy)
        self.search_text.setMinimumSize(QSize(200, 30))
        self.search_text.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.search_text)

        self.search_button = QToolButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMouseTracking(True)
        self.search_button.setStyleSheet(u"border-style:flat;")
        icon9 = QIcon()
        icon9.addFile(u":/resources/icon/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon9)
        self.search_button.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.search_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.main_view = QListWidget(self.centralwidget)
        self.main_view.setObjectName(u"main_view")

        self.verticalLayout_3.addWidget(self.main_view)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(Qt.LeftToolBarArea|Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar)

        self.toolBar.addAction(self.new_item)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.delete_item)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.update)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.import_file)
        self.toolBar.addAction(self.export_file)
        self.toolBar.addAction(self.export_excel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.star_list)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.setting)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.new_item.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
#if QT_CONFIG(tooltip)
        self.new_item.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
#endif // QT_CONFIG(tooltip)
        self.delete_item.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.delete_item.setToolTip(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
#endif // QT_CONFIG(tooltip)
        self.update.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
#if QT_CONFIG(tooltip)
        self.update.setToolTip(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
#endif // QT_CONFIG(tooltip)
        self.import_file.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
#if QT_CONFIG(tooltip)
        self.import_file.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
#endif // QT_CONFIG(tooltip)
        self.export_file.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
#if QT_CONFIG(tooltip)
        self.export_file.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
#endif // QT_CONFIG(tooltip)
        self.export_excel.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51faExcel", None))
#if QT_CONFIG(tooltip)
        self.export_excel.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u51faExcel", None))
#endif // QT_CONFIG(tooltip)
        self.star_list.setText(QCoreApplication.translate("MainWindow", u"\u6536\u85cf\u5939", None))
#if QT_CONFIG(tooltip)
        self.star_list.setToolTip(QCoreApplication.translate("MainWindow", u"\u6536\u85cf\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.setting.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.filter_button.setText("")
        self.search_button.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

