from PySide6.QtWidgets import QMainWindow, QPushButton
from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()

        # 按钮绑定
        self.filter_button.clicked.connect(self.filter_button_clicked)

    # 初始化页面
    def init_ui(self):
        # 默认隐藏筛选器
        self.filter_frame.setVisible(False)

    def filter_button_clicked(self):
        if self.filter_frame.isVisible():
            self.filter_frame.setVisible(False)
        else:
            self.filter_frame.setVisible(True)
