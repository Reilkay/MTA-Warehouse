from PySide6.QtWidgets import QMainWindow, QPushButton
from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.bind_button()

    # 初始化页面
    def init_ui(self):
        # 默认隐藏筛选器
        self.filter_frame.setVisible(False)

    # 按钮绑定
    def bind_button(self):
        # 筛选按钮
        self.filter_button.clicked.connect(self.filter_button_clicked)

    # 筛选按钮点击 折叠/展开
    def filter_button_clicked(self):
        if self.filter_frame.isVisible():
            self.filter_frame.hide_and_show(False)
        else:
            self.filter_frame.hide_and_show(True)
