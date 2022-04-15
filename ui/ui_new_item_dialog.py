# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_item_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_new_item_dialog(object):
    def setupUi(self, new_item_dialog):
        if not new_item_dialog.objectName():
            new_item_dialog.setObjectName(u"new_item_dialog")
        new_item_dialog.resize(573, 386)
        self.verticalLayout_3 = QVBoxLayout(new_item_dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(new_item_dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(new_item_dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(new_item_dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(new_item_dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_6 = QLabel(new_item_dialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(new_item_dialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.name_input = QLineEdit(new_item_dialog)
        self.name_input.setObjectName(u"name_input")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_input.sizePolicy().hasHeightForWidth())
        self.name_input.setSizePolicy(sizePolicy)
        self.name_input.setMinimumSize(QSize(150, 0))
        self.name_input.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_2.addWidget(self.name_input)

        self.name_chn_input = QLineEdit(new_item_dialog)
        self.name_chn_input.setObjectName(u"name_chn_input")
        sizePolicy.setHeightForWidth(self.name_chn_input.sizePolicy().hasHeightForWidth())
        self.name_chn_input.setSizePolicy(sizePolicy)
        self.name_chn_input.setMinimumSize(QSize(150, 0))
        self.name_chn_input.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_2.addWidget(self.name_chn_input)

        self.year_input = QLineEdit(new_item_dialog)
        self.year_input.setObjectName(u"year_input")
        sizePolicy.setHeightForWidth(self.year_input.sizePolicy().hasHeightForWidth())
        self.year_input.setSizePolicy(sizePolicy)
        self.year_input.setMinimumSize(QSize(150, 0))
        self.year_input.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_2.addWidget(self.year_input)

        self.type_input = QComboBox(new_item_dialog)
        self.type_input.setObjectName(u"type_input")
        sizePolicy.setHeightForWidth(self.type_input.sizePolicy().hasHeightForWidth())
        self.type_input.setSizePolicy(sizePolicy)
        self.type_input.setMinimumSize(QSize(150, 0))
        self.type_input.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_2.addWidget(self.type_input)

        self.area_input = QComboBox(new_item_dialog)
        self.area_input.setObjectName(u"area_input")
        sizePolicy.setHeightForWidth(self.area_input.sizePolicy().hasHeightForWidth())
        self.area_input.setSizePolicy(sizePolicy)
        self.area_input.setMinimumSize(QSize(150, 0))
        self.area_input.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_2.addWidget(self.area_input)

        self.quality_input = QComboBox(new_item_dialog)
        self.quality_input.setObjectName(u"quality_input")
        sizePolicy.setHeightForWidth(self.quality_input.sizePolicy().hasHeightForWidth())
        self.quality_input.setSizePolicy(sizePolicy)
        self.quality_input.setMinimumSize(QSize(150, 0))
        self.quality_input.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_2.addWidget(self.quality_input)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.tag_box = QGroupBox(new_item_dialog)
        self.tag_box.setObjectName(u"tag_box")
        self.gridLayout = QGridLayout(self.tag_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tag_homo = QCheckBox(self.tag_box)
        self.tag_homo.setObjectName(u"tag_homo")
        self.tag_homo.setChecked(False)

        self.gridLayout.addWidget(self.tag_homo, 1, 6, 1, 1)

        self.tag_action = QCheckBox(self.tag_box)
        self.tag_action.setObjectName(u"tag_action")
        self.tag_action.setChecked(False)

        self.gridLayout.addWidget(self.tag_action, 1, 3, 1, 1)

        self.tag_drama = QCheckBox(self.tag_box)
        self.tag_drama.setObjectName(u"tag_drama")
        self.tag_drama.setChecked(False)

        self.gridLayout.addWidget(self.tag_drama, 1, 0, 1, 1)

        self.tag_comedy = QCheckBox(self.tag_box)
        self.tag_comedy.setObjectName(u"tag_comedy")
        self.tag_comedy.setChecked(False)

        self.gridLayout.addWidget(self.tag_comedy, 1, 2, 1, 1)

        self.tag_love = QCheckBox(self.tag_box)
        self.tag_love.setObjectName(u"tag_love")
        self.tag_love.setChecked(False)

        self.gridLayout.addWidget(self.tag_love, 1, 4, 1, 1)

        self.tag_science = QCheckBox(self.tag_box)
        self.tag_science.setObjectName(u"tag_science")
        self.tag_science.setChecked(False)

        self.gridLayout.addWidget(self.tag_science, 1, 5, 1, 1)

        self.tag_music = QCheckBox(self.tag_box)
        self.tag_music.setObjectName(u"tag_music")
        self.tag_music.setChecked(False)

        self.gridLayout.addWidget(self.tag_music, 2, 0, 1, 1)

        self.tag_chorus = QCheckBox(self.tag_box)
        self.tag_chorus.setObjectName(u"tag_chorus")
        self.tag_chorus.setChecked(False)

        self.gridLayout.addWidget(self.tag_chorus, 2, 2, 1, 1)

        self.tag_biography = QCheckBox(self.tag_box)
        self.tag_biography.setObjectName(u"tag_biography")
        self.tag_biography.setChecked(False)

        self.gridLayout.addWidget(self.tag_biography, 2, 3, 1, 1)

        self.tag_history = QCheckBox(self.tag_box)
        self.tag_history.setObjectName(u"tag_history")
        self.tag_history.setChecked(False)

        self.gridLayout.addWidget(self.tag_history, 2, 4, 1, 1)

        self.tag_war = QCheckBox(self.tag_box)
        self.tag_war.setObjectName(u"tag_war")
        self.tag_war.setChecked(False)

        self.gridLayout.addWidget(self.tag_war, 2, 5, 1, 1)

        self.tag_swordsmen = QCheckBox(self.tag_box)
        self.tag_swordsmen.setObjectName(u"tag_swordsmen")
        self.tag_swordsmen.setChecked(False)

        self.gridLayout.addWidget(self.tag_swordsmen, 2, 6, 1, 1)

        self.tag_disaster = QCheckBox(self.tag_box)
        self.tag_disaster.setObjectName(u"tag_disaster")
        self.tag_disaster.setChecked(False)

        self.gridLayout.addWidget(self.tag_disaster, 4, 0, 1, 1)

        self.tag_adventrue = QCheckBox(self.tag_box)
        self.tag_adventrue.setObjectName(u"tag_adventrue")
        self.tag_adventrue.setChecked(False)

        self.gridLayout.addWidget(self.tag_adventrue, 4, 2, 1, 1)

        self.tag_fancy = QCheckBox(self.tag_box)
        self.tag_fancy.setObjectName(u"tag_fancy")
        self.tag_fancy.setChecked(False)

        self.gridLayout.addWidget(self.tag_fancy, 4, 3, 1, 1)

        self.tag_west = QCheckBox(self.tag_box)
        self.tag_west.setObjectName(u"tag_west")
        self.tag_west.setChecked(False)

        self.gridLayout.addWidget(self.tag_west, 4, 4, 1, 1)

        self.tag_suspence = QCheckBox(self.tag_box)
        self.tag_suspence.setObjectName(u"tag_suspence")
        self.tag_suspence.setChecked(False)

        self.gridLayout.addWidget(self.tag_suspence, 4, 5, 1, 1)

        self.tag_horror = QCheckBox(self.tag_box)
        self.tag_horror.setObjectName(u"tag_horror")
        self.tag_horror.setChecked(False)

        self.gridLayout.addWidget(self.tag_horror, 4, 6, 1, 1)

        self.tag_crime = QCheckBox(self.tag_box)
        self.tag_crime.setObjectName(u"tag_crime")
        self.tag_crime.setChecked(False)

        self.gridLayout.addWidget(self.tag_crime, 5, 0, 1, 1)

        self.tag_cartoon = QCheckBox(self.tag_box)
        self.tag_cartoon.setObjectName(u"tag_cartoon")
        self.tag_cartoon.setChecked(False)

        self.gridLayout.addWidget(self.tag_cartoon, 5, 2, 1, 1)

        self.tag_thriller = QCheckBox(self.tag_box)
        self.tag_thriller.setObjectName(u"tag_thriller")
        self.tag_thriller.setChecked(False)

        self.gridLayout.addWidget(self.tag_thriller, 5, 3, 1, 1)

        self.tag_sex = QCheckBox(self.tag_box)
        self.tag_sex.setObjectName(u"tag_sex")
        self.tag_sex.setChecked(False)

        self.gridLayout.addWidget(self.tag_sex, 5, 4, 1, 1)

        self.tag_other = QCheckBox(self.tag_box)
        self.tag_other.setObjectName(u"tag_other")
        self.tag_other.setChecked(False)

        self.gridLayout.addWidget(self.tag_other, 5, 5, 1, 1)


        self.horizontalLayout.addWidget(self.tag_box)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.move_top_button = QToolButton(new_item_dialog)
        self.move_top_button.setObjectName(u"move_top_button")
        icon = QIcon()
        icon.addFile(u":/resources/icon/move_top.svg", QSize(), QIcon.Normal, QIcon.On)
        self.move_top_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.move_top_button)

        self.move_up_button = QToolButton(new_item_dialog)
        self.move_up_button.setObjectName(u"move_up_button")
        icon1 = QIcon()
        icon1.addFile(u":/resources/icon/move_up.svg", QSize(), QIcon.Normal, QIcon.On)
        self.move_up_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.move_up_button)

        self.move_down_button = QToolButton(new_item_dialog)
        self.move_down_button.setObjectName(u"move_down_button")
        icon2 = QIcon()
        icon2.addFile(u":/resources/icon/move_down.svg", QSize(), QIcon.Normal, QIcon.On)
        self.move_down_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.move_down_button)

        self.window_top_button = QToolButton(new_item_dialog)
        self.window_top_button.setObjectName(u"window_top_button")
        icon3 = QIcon()
        icon3.addFile(u":/resources/icon/window_top.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/resources/icon/window_top_active.svg", QSize(), QIcon.Normal, QIcon.On)
        self.window_top_button.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.window_top_button)

        self.horizontalSpacer = QSpacerItem(225, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.add_file_button = QPushButton(new_item_dialog)
        self.add_file_button.setObjectName(u"add_file_button")
        sizePolicy.setHeightForWidth(self.add_file_button.sizePolicy().hasHeightForWidth())
        self.add_file_button.setSizePolicy(sizePolicy)
        self.add_file_button.setMinimumSize(QSize(200, 0))
        self.add_file_button.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.add_file_button)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.file_view = QListWidget(new_item_dialog)
        self.file_view.setObjectName(u"file_view")
        self.file_view.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_3.addWidget(self.file_view)

        self.buttonBox = QDialogButtonBox(new_item_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(new_item_dialog)
        self.buttonBox.accepted.connect(new_item_dialog.accept)
        self.buttonBox.rejected.connect(new_item_dialog.reject)

        QMetaObject.connectSlotsByName(new_item_dialog)
    # setupUi

    def retranslateUi(self, new_item_dialog):
        new_item_dialog.setWindowTitle(QCoreApplication.translate("new_item_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("new_item_dialog", u"\u7247\u540d", None))
        self.label_2.setText(QCoreApplication.translate("new_item_dialog", u"\u4e2d\u6587\u7247\u540d", None))
        self.label_4.setText(QCoreApplication.translate("new_item_dialog", u"\u5e74\u4efd", None))
        self.label_3.setText(QCoreApplication.translate("new_item_dialog", u"\u7c7b\u578b", None))
        self.label_6.setText(QCoreApplication.translate("new_item_dialog", u"\u5730\u533a", None))
        self.label_7.setText(QCoreApplication.translate("new_item_dialog", u"\u6e05\u6670\u5ea6", None))
        self.tag_box.setTitle(QCoreApplication.translate("new_item_dialog", u"\u6807\u7b7e", None))
        self.tag_homo.setText(QCoreApplication.translate("new_item_dialog", u"\u540c\u6027", None))
        self.tag_action.setText(QCoreApplication.translate("new_item_dialog", u"\u52a8\u4f5c", None))
        self.tag_drama.setText(QCoreApplication.translate("new_item_dialog", u"\u5267\u60c5", None))
        self.tag_comedy.setText(QCoreApplication.translate("new_item_dialog", u"\u559c\u5267", None))
        self.tag_love.setText(QCoreApplication.translate("new_item_dialog", u"\u7231\u60c5", None))
        self.tag_science.setText(QCoreApplication.translate("new_item_dialog", u"\u79d1\u5e7b", None))
        self.tag_music.setText(QCoreApplication.translate("new_item_dialog", u"\u97f3\u4e50", None))
        self.tag_chorus.setText(QCoreApplication.translate("new_item_dialog", u"\u6b4c\u821e", None))
        self.tag_biography.setText(QCoreApplication.translate("new_item_dialog", u"\u4f20\u8bb0", None))
        self.tag_history.setText(QCoreApplication.translate("new_item_dialog", u"\u5386\u53f2", None))
        self.tag_war.setText(QCoreApplication.translate("new_item_dialog", u"\u6218\u4e89", None))
        self.tag_swordsmen.setText(QCoreApplication.translate("new_item_dialog", u"\u6b66\u4fa0", None))
        self.tag_disaster.setText(QCoreApplication.translate("new_item_dialog", u"\u707e\u96be", None))
        self.tag_adventrue.setText(QCoreApplication.translate("new_item_dialog", u"\u5192\u9669", None))
        self.tag_fancy.setText(QCoreApplication.translate("new_item_dialog", u"\u5947\u5e7b", None))
        self.tag_west.setText(QCoreApplication.translate("new_item_dialog", u"\u897f\u90e8", None))
        self.tag_suspence.setText(QCoreApplication.translate("new_item_dialog", u"\u60ac\u7591", None))
        self.tag_horror.setText(QCoreApplication.translate("new_item_dialog", u"\u6050\u6016", None))
        self.tag_crime.setText(QCoreApplication.translate("new_item_dialog", u"\u72af\u7f6a", None))
        self.tag_cartoon.setText(QCoreApplication.translate("new_item_dialog", u"\u52a8\u753b", None))
        self.tag_thriller.setText(QCoreApplication.translate("new_item_dialog", u"\u60ca\u609a", None))
        self.tag_sex.setText(QCoreApplication.translate("new_item_dialog", u"\u60c5\u8272", None))
        self.tag_other.setText(QCoreApplication.translate("new_item_dialog", u"\u5176\u4ed6", None))
        self.move_top_button.setText(QCoreApplication.translate("new_item_dialog", u"\u7f6e\u9876", None))
        self.move_up_button.setText(QCoreApplication.translate("new_item_dialog", u"\u4e0a\u79fb", None))
        self.move_down_button.setText(QCoreApplication.translate("new_item_dialog", u"\u4e0b\u79fb", None))
        self.window_top_button.setText(QCoreApplication.translate("new_item_dialog", u"\u7a97\u53e3\u7f6e\u9876", None))
        self.add_file_button.setText(QCoreApplication.translate("new_item_dialog", u"\u6dfb\u52a0\u6587\u4ef6", None))
    # retranslateUi

