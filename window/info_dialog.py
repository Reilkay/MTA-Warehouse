from PySide6.QtWidgets import QFrame, QCheckBox, QGroupBox, QDialog
from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve, QAbstractAnimation
from ui.ui_info_dialog import Ui_info_dialog


class InfoDialog(QDialog, Ui_info_dialog):

    def __init__(self, parent=None, info: str = None):
        super().__init__(parent)
        self.setupUi(self)
        self.label.setText(info)

    def change_info(self, info: str):
        self.label.setText(info)