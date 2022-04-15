from PySide6.QtWidgets import QDialog, QDialogButtonBox, QFileDialog
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QKeyEvent
from PySide6.QtCore import Qt, QItemSelectionModel
from ui.ui_new_item_dialog import Ui_new_item_dialog
from utils.file_operation import FileOperation
from utils.str_utils import StrUtils


class NewItemDialog(QDialog, Ui_new_item_dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.bind_button()

    # 初始化UI
    def init_ui(self):
        self.setWindowTitle('添加新项目')
        # 按钮文本设置
        self.buttonBox.button(QDialogButtonBox.Ok).setText('确认添加')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('取消')
        # 设置置顶按钮开关状态
        self.window_top_button.setCheckable(True)
        # 下拉选择文本列表
        type_list = ['动漫', '电影', '电视剧', '纪录片', '其他']
        area_list = [
            '中国大陆', '美国', '香港', '台湾', '日本', '韩国', '英国', '法国', '西班牙', '意大利',
            '泰国', '俄罗斯', '德国', '印度', '其他'
        ]
        quality_list = ['8K', '4K', '2K', '1080P', '720P', '更低']
        # 初始化下拉选择
        self.type_input.addItems(type_list)
        self.area_input.addItems(area_list)
        self.quality_input.addItems(quality_list)
        # 允许文件拖拽
        self.setAcceptDrops(True)
        # 初始化文件列表
        self.file_list = []
        # 文件列表添加到view
        self.file_view.addItems(self.file_list)

    # 按钮绑定
    def bind_button(self):
        # 窗口置顶按钮
        self.window_top_button.clicked.connect(self.window_top_clicked)
        # 移动置顶按钮
        self.move_top_button.clicked.connect(self.move_top_clicked)
        # 上移按钮
        self.move_up_button.clicked.connect(self.move_up_clicked)
        # 下移按钮
        self.move_down_button.clicked.connect(self.move_down_clicked)
        # 添加文件按钮
        self.add_file_button.clicked.connect(self.add_file_clicked)
        # 添加目录按钮
        self.add_directory_button.clicked.connect(self.add_directory_clicked)

    # 允许拖拽文件
    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        event.acceptProposedAction()

    # 放下文件时动作
    def dropEvent(self, event: QDropEvent) -> None:
        file_urls = event.mimeData().urls()
        if len(file_urls) != 0:
            for url in file_urls:
                file_path = url.toLocalFile()
                self.file_list.append(file_path)
            # 去重，排序，重新加载显示
            self.update_file_list(unique=True, sort=True)

    # 按键事件
    def keyPressEvent(self, event: QKeyEvent) -> None:
        # 按delete键删除当前项
        if event.key() == Qt.Key_Delete and self.focusWidget(
        ) == self.file_view:
            current = self.file_view.selectedIndexes()
            if current:
                current = list(map(lambda i: i.row(), current))
                current.sort(reverse=True)
                for i in current:
                    self.file_list.pop(i)
                # 重新加载显示
                self.update_file_list()

    def accept(self) -> None:
        if self.window_top_button.isChecked():
            self.parent().show()
        return super().accept()

    def reject(self) -> None:
        if self.window_top_button.isChecked():
            self.parent().show()
        return super().reject()

    # 窗口置顶按钮点击
    def window_top_clicked(self):
        if self.window_top_button.isChecked():
            # 设置窗口位置，阻止其回到默认位置
            self.setGeometry(self.geometry())
            # 窗口置顶
            self.done(5)
        else:
            #取消置顶
            self.done(6)

    # 移动置顶按钮点击
    def move_top_clicked(self):
        current = self.file_view.selectedIndexes()
        if current:
            current = list(map(lambda i: i.row(), current))
            tmp_list = []
            for i in current:
                tmp_list.append(self.file_list[i])
            for i in sorted(current, reverse=True):
                self.file_list.pop(i)
            self.file_list = tmp_list + self.file_list
            # 重新加载显示
            self.update_file_list()
            # 重新选中之前的项
            for i in range(len(current)):
                self.file_view.selectionModel().setCurrentIndex(
                    self.file_view.model().index(i),
                    QItemSelectionModel.Select)

    # 上移按钮点击
    def move_up_clicked(self):
        current = self.file_view.selectedIndexes()
        if current:
            current = list(map(lambda i: i.row(), current))
            current.sort()
            for index, i in enumerate(current):
                if (i != 0) and (i - 1 not in current):
                    tmp = self.file_list.pop(i)
                    self.file_list.insert(i - 1, tmp)
                    current[index] -= 1
                    break
            # 重新加载显示
            self.update_file_list()
            # 重新选中之前的项
            for i in current:
                self.file_view.selectionModel().setCurrentIndex(
                    self.file_view.model().index(i),
                    QItemSelectionModel.Select)

    # 下移按钮点击
    def move_down_clicked(self):
        current = self.file_view.selectedIndexes()
        if current:
            current = list(map(lambda i: i.row(), current))
            current.sort(reverse=True)
            for index, i in enumerate(current):
                if (i != len(self.file_list) - 1) and (i + 1 not in current):
                    tmp = self.file_list.pop(i)
                    self.file_list.insert(i + 1, tmp)
                    current[index] += 1
                    break
            # 重新加载显示
            self.update_file_list()
            # 重新选中之前的项
            for i in current:
                self.file_view.selectionModel().setCurrentIndex(
                    self.file_view.model().index(i),
                    QItemSelectionModel.Select)

    # 添加文件按钮点击
    def add_file_clicked(self):
        files, _ = QFileDialog.getOpenFileNames(self, '选择要添加的文件...', '.')
        if len(files) != 0:
            for file in files:
                self.file_list.append(file)
            # 去重，排序，重新加载显示
            self.update_file_list(unique=True, sort=True)

    # 添加目录按钮点击
    def add_directory_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, '选择要添加的文件所在目录...',
                                                     '.')
        files = FileOperation.get_files_from_path(directory)
        if len(files) != 0:
            for file in files:
                self.file_list.append(file)
            # 去重，排序，重新加载显示
            self.update_file_list(unique=True, sort=True)

    # 文件列表重新加载
    def update_file_list(self, unique: bool = False, sort: bool = False):
        if unique:
            # 去重
            tmp = list(set(self.file_list))
            tmp.sort(key=self.file_list.index)
            self.file_list = tmp
        if sort:
            # 试图排序
            self.file_list = StrUtils.file_name_sorted(self.file_list)
        # 重新加载显示
        self.file_view.clear()
        self.file_view.addItems(self.file_list)
