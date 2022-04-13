from PySide6.QtWidgets import QFrame, QCheckBox, QGroupBox
from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve, QAbstractAnimation
from ui.ui_filter_frame import Ui_filter_frame


class FilterFrame(QFrame, Ui_filter_frame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.origin_height = self.rect().height()
        self.init_ui()
        self.bind_button()

    # 初始化UI
    def init_ui(self):
        pass

    # 绑定按钮
    def bind_button(self):
        # 点击全部全选（全不选）其他
        self.type_all.clicked.connect(
            lambda: self.group_all_clicked(self.type_box, self.type_all))
        self.tag_all.clicked.connect(
            lambda: self.group_all_clicked(self.tag_box, self.tag_all))
        self.area_all.clicked.connect(
            lambda: self.group_all_clicked(self.area_box, self.area_all))
        self.year_all.clicked.connect(
            lambda: self.group_all_clicked(self.year_box, self.year_all))
        self.quality_all.clicked.connect(
            lambda: self.group_all_clicked(self.quality_box, self.quality_all))
        # 点击其他取消全部
        for item in self.type_box.children():
            if isinstance(item, QCheckBox) and item != self.type_all:
                item.clicked.connect(lambda: self.group_others_clicked(
                    self.type_box, self.type_all))
        for item in self.tag_box.children():
            if isinstance(item, QCheckBox) and item != self.tag_all:
                item.clicked.connect(lambda: self.group_others_clicked(
                    self.tag_box, self.tag_all))
        for item in self.area_box.children():
            if isinstance(item, QCheckBox) and item != self.area_all:
                item.clicked.connect(lambda: self.group_others_clicked(
                    self.area_box, self.area_all))
        for item in self.year_box.children():
            if isinstance(item, QCheckBox) and item != self.year_all:
                item.clicked.connect(lambda: self.group_others_clicked(
                    self.year_box, self.year_all))
        for item in self.quality_box.children():
            if isinstance(item, QCheckBox) and item != self.quality_all:
                item.clicked.connect(lambda: self.group_others_clicked(
                    self.quality_box, self.quality_all))

    def group_all_clicked(self, group: QGroupBox, all: QCheckBox):
        if all.isChecked():
            for item in group.children():
                if isinstance(item, QCheckBox) and item != all:
                    item.setChecked(True)
        else:
            for item in group.children():
                if isinstance(item, QCheckBox) and item != all:
                    item.setChecked(False)

    def group_others_clicked(self, group: QGroupBox, all: QCheckBox):
        all_is_true = True
        for item in group.children():
            if isinstance(item, QCheckBox) and item != all:
                if not item.isChecked():
                    all_is_true = False
        all.setChecked(all_is_true)

    def hide_and_show(self, vis: bool):
        # 显示
        if vis:
            self.setVisible(True)
            # 1.定义一个动画
            animation_vis = QPropertyAnimation(self)
            animation_vis.setTargetObject(self)
            animation_vis.setPropertyName(b'geometry')
            # 2.设置属性值
            animation_vis.setStartValue(
                QRect(self.rect().left(),
                      self.rect().top(),
                      self.rect().width(), 0))
            animation_vis.setEndValue(
                QRect(self.rect().left(),
                      self.rect().top(),
                      self.rect().width(), self.origin_height))
            # 3.设置缓速曲线
            animation_vis.setEasingCurve(QEasingCurve.OutExpo)
            # 4.设置时长
            animation_vis.setDuration(100)
            # 5.启动动画
            animation_vis.start(QAbstractAnimation.DeleteWhenStopped)
        # 隐藏
        else:
            # 1.定义一个动画
            animation_hide = QPropertyAnimation(self)
            animation_hide.setTargetObject(self)
            animation_hide.setPropertyName(b'geometry')
            # 2.设置属性值
            animation_hide.setStartValue(
                QRect(self.rect().left(),
                      self.rect().top(),
                      self.rect().width(), self.origin_height))
            animation_hide.setEndValue(
                QRect(self.rect().left(),
                      self.rect().top(),
                      self.rect().width(), 0))
            # 3.设置缓速曲线
            animation_hide.setEasingCurve(QEasingCurve.OutExpo)
            # 4.设置时长
            animation_hide.setDuration(140)
            # 5.启动动画
            animation_hide.start(QAbstractAnimation.DeleteWhenStopped)
            # 6.动画结束后控制部件显隐
            animation_hide.finished.connect(lambda: {self.setVisible(vis)})
