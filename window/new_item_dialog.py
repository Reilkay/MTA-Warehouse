from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QKeyEvent
from PySide6.QtCore import Qt
from ui.ui_new_item_dialog import Ui_new_item_dialog


class NewItemDialog(QDialog, Ui_new_item_dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()

    # 初始化UI
    def init_ui(self):
        self.setWindowTitle('添加新项目')
        # 按钮文本设置
        self.buttonBox.button(QDialogButtonBox.Ok).setText('确认添加')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('取消')
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

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent) -> None:
        file_urls = event.mimeData().urls()
        if len(file_urls) != 0:
            for url in file_urls:
                file_path = url.toLocalFile()
                self.file_list.append(file_path)
            # 去重
            tmp = list(set(self.file_list))
            tmp.sort(key=self.file_list.index)
            self.file_list = tmp
            self.file_view.clear()
            self.file_view.addItems(self.file_list)
            print(self.file_list)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        # 按delete键删除
        if event.key() == Qt.Key_Delete and self.focusWidget(
        ) == self.file_view:
            current = self.file_view.selectedIndexes()
            current = list(map(lambda i: i.row(), current))
            current.sort(reverse=True)
            if current:
                for i in current:
                    self.file_list.pop(i)
                self.file_view.clear()
                self.file_view.addItems(self.file_list)

    def accept(self) -> None:
        return super().accept()

    def reject(self) -> None:
        return super().reject()