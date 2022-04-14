from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from ui.ui_main_window import Ui_MainWindow
from window.info_dialog import InfoDialog
from utils.dao import Dao
from utils.str_utils import StrUtils


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.bind_button()
        self.bind_view_item()

    # 初始化页面
    def init_ui(self):
        # 默认隐藏筛选器
        self.filter_frame.setVisible(False)
        # 创建详细信息窗口
        self.dl: InfoDialog = None
        # 获取数据
        self.mta_data_list = Dao().get_MTA_list()
        # 将数据填入ListWidget
        self.main_view.addItems(
            StrUtils.MTA_list_to_show_list(self.mta_data_list))

    # 按钮绑定
    def bind_button(self):
        # 筛选按钮
        self.filter_button.clicked.connect(self.filter_button_clicked)

    def bind_view_item(self):
        self.main_view.currentRowChanged.connect(self.mta_item_changed)

    # 筛选按钮点击 折叠/展开
    def filter_button_clicked(self):
        if self.filter_frame.isVisible():
            self.filter_frame.hide_and_show(False)
        else:
            self.filter_frame.hide_and_show(True)

    def mta_item_changed(self, current: int):
        if current != -1:
            info = StrUtils.get_MTA_info(self.mta_data_list[current])
            if not self.dl:
                self.dl = InfoDialog(self, info=info)
                self.dl.show()
                self.dl.setGeometry(self.x() + self.width(),
                                    self.y() + 40, self.dl.width(),
                                    self.dl.height())
            else:
                self.dl.change_info(info)
                if self.dl.isHidden():
                    self.dl.show()
                    self.dl.setGeometry(self.x() + self.width(),
                                        self.y() + 40, self.dl.width(),
                                        self.dl.height())
