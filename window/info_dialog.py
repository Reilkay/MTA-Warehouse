from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from ui.ui_info_dialog import Ui_info_dialog


class InfoDialog(QDialog, Ui_info_dialog):

    def __init__(self, parent=None, info: str = None):
        super().__init__(parent)
        self.setupUi(self)
        self.label.setText(info)
        self.setWindowTitle('详细信息')
        # self.setAttribute(Qt.WA_ShowWithoutActivating, True)
        self.setWindowFlags(Qt.Tool)

    def change_info(self, info: str):
        self.label.setText(info)