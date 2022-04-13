# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_filter_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_filter_frame(object):
    def setupUi(self, filter_frame):
        if not filter_frame.objectName():
            filter_frame.setObjectName(u"filter_frame")
        filter_frame.resize(674, 371)
        self.verticalLayout = QVBoxLayout(filter_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.type_box = QGroupBox(filter_frame)
        self.type_box.setObjectName(u"type_box")
        self.gridLayout_5 = QGridLayout(self.type_box)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.type_movie = QCheckBox(self.type_box)
        self.type_movie.setObjectName(u"type_movie")
        self.type_movie.setChecked(True)

        self.gridLayout_5.addWidget(self.type_movie, 0, 3, 1, 1)

        self.type_record = QCheckBox(self.type_box)
        self.type_record.setObjectName(u"type_record")
        self.type_record.setChecked(True)

        self.gridLayout_5.addWidget(self.type_record, 0, 5, 1, 1)

        self.type_other = QCheckBox(self.type_box)
        self.type_other.setObjectName(u"type_other")
        self.type_other.setChecked(True)

        self.gridLayout_5.addWidget(self.type_other, 0, 6, 1, 1)

        self.type_anime = QCheckBox(self.type_box)
        self.type_anime.setObjectName(u"type_anime")
        self.type_anime.setChecked(True)

        self.gridLayout_5.addWidget(self.type_anime, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 8, 1, 1)

        self.type_all = QCheckBox(self.type_box)
        self.type_all.setObjectName(u"type_all")
        self.type_all.setChecked(True)

        self.gridLayout_5.addWidget(self.type_all, 0, 1, 1, 1)

        self.type_drama = QCheckBox(self.type_box)
        self.type_drama.setObjectName(u"type_drama")
        self.type_drama.setChecked(True)

        self.gridLayout_5.addWidget(self.type_drama, 0, 4, 1, 1)


        self.verticalLayout.addWidget(self.type_box)

        self.tag_box = QGroupBox(filter_frame)
        self.tag_box.setObjectName(u"tag_box")
        self.gridLayout = QGridLayout(self.tag_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tag_science = QCheckBox(self.tag_box)
        self.tag_science.setObjectName(u"tag_science")
        self.tag_science.setChecked(True)

        self.gridLayout.addWidget(self.tag_science, 1, 6, 1, 1)

        self.tag_swordsmen = QCheckBox(self.tag_box)
        self.tag_swordsmen.setObjectName(u"tag_swordsmen")
        self.tag_swordsmen.setChecked(True)

        self.gridLayout.addWidget(self.tag_swordsmen, 4, 0, 1, 1)

        self.tag_all = QCheckBox(self.tag_box)
        self.tag_all.setObjectName(u"tag_all")
        self.tag_all.setChecked(True)

        self.gridLayout.addWidget(self.tag_all, 1, 0, 1, 1)

        self.tag_other = QCheckBox(self.tag_box)
        self.tag_other.setObjectName(u"tag_other")
        self.tag_other.setChecked(True)

        self.gridLayout.addWidget(self.tag_other, 4, 12, 1, 1)

        self.tag_comedy = QCheckBox(self.tag_box)
        self.tag_comedy.setObjectName(u"tag_comedy")
        self.tag_comedy.setChecked(True)

        self.gridLayout.addWidget(self.tag_comedy, 1, 3, 1, 1)

        self.tag_drama = QCheckBox(self.tag_box)
        self.tag_drama.setObjectName(u"tag_drama")
        self.tag_drama.setChecked(True)

        self.gridLayout.addWidget(self.tag_drama, 1, 2, 1, 1)

        self.tag_crime = QCheckBox(self.tag_box)
        self.tag_crime.setObjectName(u"tag_crime")
        self.tag_crime.setChecked(True)

        self.gridLayout.addWidget(self.tag_crime, 4, 8, 1, 1)

        self.tag_homo = QCheckBox(self.tag_box)
        self.tag_homo.setObjectName(u"tag_homo")
        self.tag_homo.setChecked(True)

        self.gridLayout.addWidget(self.tag_homo, 1, 7, 1, 1)

        self.tag_music = QCheckBox(self.tag_box)
        self.tag_music.setObjectName(u"tag_music")
        self.tag_music.setChecked(True)

        self.gridLayout.addWidget(self.tag_music, 1, 8, 1, 1)

        self.tag_adventrue = QCheckBox(self.tag_box)
        self.tag_adventrue.setObjectName(u"tag_adventrue")
        self.tag_adventrue.setChecked(True)

        self.gridLayout.addWidget(self.tag_adventrue, 4, 3, 1, 1)

        self.tag_biography = QCheckBox(self.tag_box)
        self.tag_biography.setObjectName(u"tag_biography")
        self.tag_biography.setChecked(True)

        self.gridLayout.addWidget(self.tag_biography, 1, 10, 1, 1)

        self.tag_disaster = QCheckBox(self.tag_box)
        self.tag_disaster.setObjectName(u"tag_disaster")
        self.tag_disaster.setChecked(True)

        self.gridLayout.addWidget(self.tag_disaster, 4, 2, 1, 1)

        self.tag_history = QCheckBox(self.tag_box)
        self.tag_history.setObjectName(u"tag_history")
        self.tag_history.setChecked(True)

        self.gridLayout.addWidget(self.tag_history, 1, 11, 1, 1)

        self.tag_horror = QCheckBox(self.tag_box)
        self.tag_horror.setObjectName(u"tag_horror")
        self.tag_horror.setChecked(True)

        self.gridLayout.addWidget(self.tag_horror, 4, 7, 1, 1)

        self.tag_chorus = QCheckBox(self.tag_box)
        self.tag_chorus.setObjectName(u"tag_chorus")
        self.tag_chorus.setChecked(True)

        self.gridLayout.addWidget(self.tag_chorus, 1, 9, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 13, 1, 1)

        self.tag_thriller = QCheckBox(self.tag_box)
        self.tag_thriller.setObjectName(u"tag_thriller")
        self.tag_thriller.setChecked(True)

        self.gridLayout.addWidget(self.tag_thriller, 4, 10, 1, 1)

        self.tag_war = QCheckBox(self.tag_box)
        self.tag_war.setObjectName(u"tag_war")
        self.tag_war.setChecked(True)

        self.gridLayout.addWidget(self.tag_war, 1, 12, 1, 1)

        self.tag_sex = QCheckBox(self.tag_box)
        self.tag_sex.setObjectName(u"tag_sex")
        self.tag_sex.setChecked(True)

        self.gridLayout.addWidget(self.tag_sex, 4, 11, 1, 1)

        self.tag_love = QCheckBox(self.tag_box)
        self.tag_love.setObjectName(u"tag_love")
        self.tag_love.setChecked(True)

        self.gridLayout.addWidget(self.tag_love, 1, 5, 1, 1)

        self.tag_west = QCheckBox(self.tag_box)
        self.tag_west.setObjectName(u"tag_west")
        self.tag_west.setChecked(True)

        self.gridLayout.addWidget(self.tag_west, 4, 5, 1, 1)

        self.tag_cartoon = QCheckBox(self.tag_box)
        self.tag_cartoon.setObjectName(u"tag_cartoon")
        self.tag_cartoon.setChecked(True)

        self.gridLayout.addWidget(self.tag_cartoon, 4, 9, 1, 1)

        self.tag_suspence = QCheckBox(self.tag_box)
        self.tag_suspence.setObjectName(u"tag_suspence")
        self.tag_suspence.setChecked(True)

        self.gridLayout.addWidget(self.tag_suspence, 4, 6, 1, 1)

        self.tag_action = QCheckBox(self.tag_box)
        self.tag_action.setObjectName(u"tag_action")
        self.tag_action.setChecked(True)

        self.gridLayout.addWidget(self.tag_action, 1, 4, 1, 1)

        self.tag_fancy = QCheckBox(self.tag_box)
        self.tag_fancy.setObjectName(u"tag_fancy")
        self.tag_fancy.setChecked(True)

        self.gridLayout.addWidget(self.tag_fancy, 4, 4, 1, 1)


        self.verticalLayout.addWidget(self.tag_box)

        self.area_box = QGroupBox(filter_frame)
        self.area_box.setObjectName(u"area_box")
        self.gridLayout_2 = QGridLayout(self.area_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.area_all = QCheckBox(self.area_box)
        self.area_all.setObjectName(u"area_all")
        self.area_all.setChecked(True)

        self.gridLayout_2.addWidget(self.area_all, 0, 0, 1, 1)

        self.area_France = QCheckBox(self.area_box)
        self.area_France.setObjectName(u"area_France")
        self.area_France.setChecked(True)

        self.gridLayout_2.addWidget(self.area_France, 0, 10, 1, 1)

        self.area_India = QCheckBox(self.area_box)
        self.area_India.setObjectName(u"area_India")
        self.area_India.setChecked(True)

        self.gridLayout_2.addWidget(self.area_India, 1, 5, 1, 1)

        self.area_Russia = QCheckBox(self.area_box)
        self.area_Russia.setObjectName(u"area_Russia")
        self.area_Russia.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Russia, 1, 3, 1, 1)

        self.area_America = QCheckBox(self.area_box)
        self.area_America.setObjectName(u"area_America")
        self.area_America.setChecked(True)

        self.gridLayout_2.addWidget(self.area_America, 0, 4, 1, 1)

        self.area_Korea = QCheckBox(self.area_box)
        self.area_Korea.setObjectName(u"area_Korea")
        self.area_Korea.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Korea, 0, 8, 1, 1)

        self.area_Italy = QCheckBox(self.area_box)
        self.area_Italy.setObjectName(u"area_Italy")
        self.area_Italy.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Italy, 0, 13, 1, 1)

        self.area_Japan = QCheckBox(self.area_box)
        self.area_Japan.setObjectName(u"area_Japan")
        self.area_Japan.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Japan, 0, 7, 1, 1)

        self.area_Britain = QCheckBox(self.area_box)
        self.area_Britain.setObjectName(u"area_Britain")
        self.area_Britain.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Britain, 0, 9, 1, 1)

        self.area_Thailand = QCheckBox(self.area_box)
        self.area_Thailand.setObjectName(u"area_Thailand")
        self.area_Thailand.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Thailand, 1, 0, 1, 1)

        self.area_China = QCheckBox(self.area_box)
        self.area_China.setObjectName(u"area_China")
        self.area_China.setChecked(True)

        self.gridLayout_2.addWidget(self.area_China, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 14, 1, 1)

        self.area_Taiwan = QCheckBox(self.area_box)
        self.area_Taiwan.setObjectName(u"area_Taiwan")
        self.area_Taiwan.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Taiwan, 0, 6, 1, 1)

        self.area_Other = QCheckBox(self.area_box)
        self.area_Other.setObjectName(u"area_Other")
        self.area_Other.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Other, 1, 6, 1, 1)

        self.area_Hongkong = QCheckBox(self.area_box)
        self.area_Hongkong.setObjectName(u"area_Hongkong")
        self.area_Hongkong.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Hongkong, 0, 5, 1, 1)

        self.area_Spain = QCheckBox(self.area_box)
        self.area_Spain.setObjectName(u"area_Spain")
        self.area_Spain.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Spain, 0, 11, 1, 1)

        self.area_Germany = QCheckBox(self.area_box)
        self.area_Germany.setObjectName(u"area_Germany")
        self.area_Germany.setChecked(True)

        self.gridLayout_2.addWidget(self.area_Germany, 1, 4, 1, 1)


        self.verticalLayout.addWidget(self.area_box)

        self.year_box = QGroupBox(filter_frame)
        self.year_box.setObjectName(u"year_box")
        self.gridLayout_3 = QGridLayout(self.year_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.year_1970 = QCheckBox(self.year_box)
        self.year_1970.setObjectName(u"year_1970")
        self.year_1970.setChecked(True)

        self.gridLayout_3.addWidget(self.year_1970, 0, 6, 1, 1)

        self.year_1960 = QCheckBox(self.year_box)
        self.year_1960.setObjectName(u"year_1960")
        self.year_1960.setChecked(True)

        self.gridLayout_3.addWidget(self.year_1960, 0, 7, 1, 1)

        self.year_before = QCheckBox(self.year_box)
        self.year_before.setObjectName(u"year_before")
        self.year_before.setChecked(True)

        self.gridLayout_3.addWidget(self.year_before, 0, 8, 1, 1)

        self.year_1990 = QCheckBox(self.year_box)
        self.year_1990.setObjectName(u"year_1990")
        self.year_1990.setChecked(True)

        self.gridLayout_3.addWidget(self.year_1990, 0, 4, 1, 1)

        self.year_all = QCheckBox(self.year_box)
        self.year_all.setObjectName(u"year_all")
        self.year_all.setChecked(True)

        self.gridLayout_3.addWidget(self.year_all, 0, 0, 1, 1)

        self.year_2000 = QCheckBox(self.year_box)
        self.year_2000.setObjectName(u"year_2000")
        self.year_2000.setChecked(True)

        self.gridLayout_3.addWidget(self.year_2000, 0, 3, 1, 1)

        self.year_2010 = QCheckBox(self.year_box)
        self.year_2010.setObjectName(u"year_2010")
        self.year_2010.setChecked(True)

        self.gridLayout_3.addWidget(self.year_2010, 0, 2, 1, 1)

        self.year_2020 = QCheckBox(self.year_box)
        self.year_2020.setObjectName(u"year_2020")
        self.year_2020.setChecked(True)

        self.gridLayout_3.addWidget(self.year_2020, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 9, 1, 1)

        self.year_1980 = QCheckBox(self.year_box)
        self.year_1980.setObjectName(u"year_1980")
        self.year_1980.setChecked(True)

        self.gridLayout_3.addWidget(self.year_1980, 0, 5, 1, 1)


        self.verticalLayout.addWidget(self.year_box)

        self.quality_box = QGroupBox(filter_frame)
        self.quality_box.setObjectName(u"quality_box")
        self.gridLayout_4 = QGridLayout(self.quality_box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.quality_8K = QCheckBox(self.quality_box)
        self.quality_8K.setObjectName(u"quality_8K")
        self.quality_8K.setChecked(True)

        self.gridLayout_4.addWidget(self.quality_8K, 0, 1, 1, 1)

        self.quality_1080P = QCheckBox(self.quality_box)
        self.quality_1080P.setObjectName(u"quality_1080P")
        self.quality_1080P.setChecked(True)

        self.gridLayout_4.addWidget(self.quality_1080P, 0, 4, 1, 1)

        self.quality_all = QCheckBox(self.quality_box)
        self.quality_all.setObjectName(u"quality_all")
        self.quality_all.setChecked(True)

        self.gridLayout_4.addWidget(self.quality_all, 0, 0, 1, 1)

        self.quality_4K = QCheckBox(self.quality_box)
        self.quality_4K.setObjectName(u"quality_4K")
        self.quality_4K.setChecked(True)

        self.gridLayout_4.addWidget(self.quality_4K, 0, 2, 1, 1)

        self.quality_2K = QCheckBox(self.quality_box)
        self.quality_2K.setObjectName(u"quality_2K")
        self.quality_2K.setChecked(True)

        self.gridLayout_4.addWidget(self.quality_2K, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 13, 1, 1)

        self.quality_lower = QCheckBox(self.quality_box)
        self.quality_lower.setObjectName(u"quality_lower")
        self.quality_lower.setChecked(True)

        self.gridLayout_4.addWidget(self.quality_lower, 0, 6, 1, 1)

        self.quality_720P = QCheckBox(self.quality_box)
        self.quality_720P.setObjectName(u"quality_720P")
        self.quality_720P.setChecked(True)

        self.gridLayout_4.addWidget(self.quality_720P, 0, 5, 1, 1)


        self.verticalLayout.addWidget(self.quality_box)


        self.retranslateUi(filter_frame)

        QMetaObject.connectSlotsByName(filter_frame)
    # setupUi

    def retranslateUi(self, filter_frame):
        filter_frame.setWindowTitle(QCoreApplication.translate("filter_frame", u"Frame", None))
        self.type_box.setTitle(QCoreApplication.translate("filter_frame", u"\u7c7b\u578b", None))
        self.type_movie.setText(QCoreApplication.translate("filter_frame", u"\u7535\u5f71", None))
        self.type_record.setText(QCoreApplication.translate("filter_frame", u"\u7eaa\u5f55\u7247", None))
        self.type_other.setText(QCoreApplication.translate("filter_frame", u"\u5176\u4ed6", None))
        self.type_anime.setText(QCoreApplication.translate("filter_frame", u"\u52a8\u6f2b", None))
        self.type_all.setText(QCoreApplication.translate("filter_frame", u"\u5168\u90e8", None))
        self.type_drama.setText(QCoreApplication.translate("filter_frame", u"\u7535\u89c6\u5267", None))
        self.tag_box.setTitle(QCoreApplication.translate("filter_frame", u"\u6807\u7b7e", None))
        self.tag_science.setText(QCoreApplication.translate("filter_frame", u"\u79d1\u5e7b", None))
        self.tag_swordsmen.setText(QCoreApplication.translate("filter_frame", u"\u6b66\u4fa0", None))
        self.tag_all.setText(QCoreApplication.translate("filter_frame", u"\u5168\u90e8", None))
        self.tag_other.setText(QCoreApplication.translate("filter_frame", u"\u5176\u4ed6", None))
        self.tag_comedy.setText(QCoreApplication.translate("filter_frame", u"\u559c\u5267", None))
        self.tag_drama.setText(QCoreApplication.translate("filter_frame", u"\u5267\u60c5", None))
        self.tag_crime.setText(QCoreApplication.translate("filter_frame", u"\u72af\u7f6a", None))
        self.tag_homo.setText(QCoreApplication.translate("filter_frame", u"\u540c\u6027", None))
        self.tag_music.setText(QCoreApplication.translate("filter_frame", u"\u97f3\u4e50", None))
        self.tag_adventrue.setText(QCoreApplication.translate("filter_frame", u"\u5192\u9669", None))
        self.tag_biography.setText(QCoreApplication.translate("filter_frame", u"\u4f20\u8bb0", None))
        self.tag_disaster.setText(QCoreApplication.translate("filter_frame", u"\u707e\u96be", None))
        self.tag_history.setText(QCoreApplication.translate("filter_frame", u"\u5386\u53f2", None))
        self.tag_horror.setText(QCoreApplication.translate("filter_frame", u"\u6050\u6016", None))
        self.tag_chorus.setText(QCoreApplication.translate("filter_frame", u"\u6b4c\u821e", None))
        self.tag_thriller.setText(QCoreApplication.translate("filter_frame", u"\u60ca\u609a", None))
        self.tag_war.setText(QCoreApplication.translate("filter_frame", u"\u6218\u4e89", None))
        self.tag_sex.setText(QCoreApplication.translate("filter_frame", u"\u60c5\u8272", None))
        self.tag_love.setText(QCoreApplication.translate("filter_frame", u"\u7231\u60c5", None))
        self.tag_west.setText(QCoreApplication.translate("filter_frame", u"\u897f\u90e8", None))
        self.tag_cartoon.setText(QCoreApplication.translate("filter_frame", u"\u52a8\u753b", None))
        self.tag_suspence.setText(QCoreApplication.translate("filter_frame", u"\u60ac\u7591", None))
        self.tag_action.setText(QCoreApplication.translate("filter_frame", u"\u52a8\u4f5c", None))
        self.tag_fancy.setText(QCoreApplication.translate("filter_frame", u"\u5947\u5e7b", None))
        self.area_box.setTitle(QCoreApplication.translate("filter_frame", u"\u5730\u533a", None))
        self.area_all.setText(QCoreApplication.translate("filter_frame", u"\u5168\u90e8", None))
        self.area_France.setText(QCoreApplication.translate("filter_frame", u"\u6cd5\u56fd", None))
        self.area_India.setText(QCoreApplication.translate("filter_frame", u"\u5370\u5ea6", None))
        self.area_Russia.setText(QCoreApplication.translate("filter_frame", u"\u4fc4\u7f57\u65af", None))
        self.area_America.setText(QCoreApplication.translate("filter_frame", u"\u7f8e\u56fd", None))
        self.area_Korea.setText(QCoreApplication.translate("filter_frame", u"\u97e9\u56fd", None))
        self.area_Italy.setText(QCoreApplication.translate("filter_frame", u"\u610f\u5927\u5229", None))
        self.area_Japan.setText(QCoreApplication.translate("filter_frame", u"\u65e5\u672c", None))
        self.area_Britain.setText(QCoreApplication.translate("filter_frame", u"\u82f1\u56fd", None))
        self.area_Thailand.setText(QCoreApplication.translate("filter_frame", u"\u6cf0\u56fd", None))
        self.area_China.setText(QCoreApplication.translate("filter_frame", u"\u4e2d\u56fd\u5927\u9646", None))
        self.area_Taiwan.setText(QCoreApplication.translate("filter_frame", u"\u53f0\u6e7e", None))
        self.area_Other.setText(QCoreApplication.translate("filter_frame", u"\u5176\u4ed6", None))
        self.area_Hongkong.setText(QCoreApplication.translate("filter_frame", u"\u9999\u6e2f", None))
        self.area_Spain.setText(QCoreApplication.translate("filter_frame", u"\u897f\u73ed\u7259", None))
        self.area_Germany.setText(QCoreApplication.translate("filter_frame", u"\u5fb7\u56fd", None))
        self.year_box.setTitle(QCoreApplication.translate("filter_frame", u"\u5e74\u4ee3", None))
        self.year_1970.setText(QCoreApplication.translate("filter_frame", u"1970", None))
        self.year_1960.setText(QCoreApplication.translate("filter_frame", u"1960", None))
        self.year_before.setText(QCoreApplication.translate("filter_frame", u"\u66f4\u65e9", None))
        self.year_1990.setText(QCoreApplication.translate("filter_frame", u"1990", None))
        self.year_all.setText(QCoreApplication.translate("filter_frame", u"\u5168\u90e8", None))
        self.year_2000.setText(QCoreApplication.translate("filter_frame", u"2000", None))
        self.year_2010.setText(QCoreApplication.translate("filter_frame", u"2010", None))
        self.year_2020.setText(QCoreApplication.translate("filter_frame", u"2020", None))
        self.year_1980.setText(QCoreApplication.translate("filter_frame", u"1980", None))
        self.quality_box.setTitle(QCoreApplication.translate("filter_frame", u"\u6e05\u6670\u5ea6", None))
        self.quality_8K.setText(QCoreApplication.translate("filter_frame", u"8K", None))
        self.quality_1080P.setText(QCoreApplication.translate("filter_frame", u"1080P", None))
        self.quality_all.setText(QCoreApplication.translate("filter_frame", u"\u5168\u90e8", None))
        self.quality_4K.setText(QCoreApplication.translate("filter_frame", u"4K", None))
        self.quality_2K.setText(QCoreApplication.translate("filter_frame", u"2K", None))
        self.quality_lower.setText(QCoreApplication.translate("filter_frame", u"\u66f4\u4f4e", None))
        self.quality_720P.setText(QCoreApplication.translate("filter_frame", u"720P", None))
    # retranslateUi

