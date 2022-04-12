from PySide6.QtWidgets import QFrame, QCheckBox
from ui.ui_filter_frame import Ui_filter_frame


class FilterFrame(QFrame, Ui_filter_frame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.bind_button()

    def init_ui(self):
        self.type_all.setChecked(True)
        self.tag_all.setChecked(True)
        self.area_all.setChecked(True)
        self.year_all.setChecked(True)
        self.quality_all.setChecked(True)

    def bind_button(self):
        # 点击全部取消其他
        self.type_all.toggled.connect(self.type_all_toggled)
        # 点击其他取消全部
        for item in self.type_box.children():
            if isinstance(item, QCheckBox) and item.objectName() != 'type_all':
                item.clicked.connect(self.type_others_clicked)

    def type_all_toggled(self):
        if self.type_all.isChecked():
            for item in self.type_box.children():
                if isinstance(item,
                              QCheckBox) and item.objectName() != 'type_all':
                    item.setChecked(False)

    def type_others_clicked(self):
        if self.type_all.isChecked():
            self.type_all.setChecked(False)