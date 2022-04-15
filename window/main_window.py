from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from data.MTA_data import MTAData
from ui.ui_main_window import Ui_MainWindow
from window.info_dialog import InfoDialog
from window.new_item_dialog import NewItemDialog
from utils.dao import Dao
from utils.str_utils import StrUtils


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.bind_button()
        self.bind_view_item()
        self.bind_action()

    # 初始化页面
    def init_ui(self):
        # 默认隐藏筛选器
        self.filter_frame.setVisible(False)
        # 创建详细信息窗口
        self.dl: InfoDialog = None
        # 获取数据
        self.mta_data_list = Dao().get_MTA_list()
        # 刷新列表显示，将数据填入
        self.update_main_list()

    # 刷新列表显示
    def update_main_list(self):
        # 将ListWidget清空
        self.main_view.clear()
        # 将数据填入ListWidget
        self.main_view.addItems(
            StrUtils.MTA_list_to_show_list(self.mta_data_list))

    # 按钮绑定
    def bind_button(self):
        # 筛选按钮
        self.filter_button.clicked.connect(self.filter_button_clicked)

    # ListWidgetItem绑定
    def bind_view_item(self):
        self.main_view.currentRowChanged.connect(self.mta_item_changed)

    # 动作绑定
    def bind_action(self):
        self.new_item.triggered.connect(self.new_item_triggered)

    # 筛选按钮点击 折叠/展开
    def filter_button_clicked(self):
        if self.filter_frame.isVisible():
            self.filter_frame.hide_and_show(False)
        else:
            self.filter_frame.hide_and_show(True)

    # mta项目点击/切换时打开详情弹窗
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

    # 点击添加按钮
    def new_item_triggered(self):
        dl = NewItemDialog(self)
        # 信号绑定
        dl.add_new_item.connect(self.append_new_item)
        resu = 0
        while True:
            resu = dl.exec()
            if resu == 5:
                dl.setWindowFlag(Qt.WindowStaysOnTopHint, True)
                self.hide()
            elif resu == 6:
                dl.setWindowFlag(Qt.WindowStaysOnTopHint, False)
                self.show()
            else:
                break
        if resu == 1:
            print("add")
            # 刷新列表显示
            self.update_main_list()
        else:
            print("no-add")

    # 将收到的mta数据添加进列表中，并永久化存储
    def append_new_item(self, mta: MTAData):
        print("get mta data!")
        self.mta_data_list.append(mta)
        Dao().add_MTA_item(mta)
