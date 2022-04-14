from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QStringListModel
from ui.ui_main_window import Ui_MainWindow
from utils.dao import Dao
from utils.str_utils import StrUtils


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
        # 获取数据
        self.mta_data_list = Dao().get_MTA_list()
        # 将数据填入ListView
        self.main_view_model = QStringListModel()
        self.main_view_model.setStringList(
            StrUtils.MTA_list_to_show_list(self.mta_data_list))
        self.main_view.setModel(self.main_view_model)

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
