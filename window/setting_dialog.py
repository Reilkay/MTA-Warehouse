from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from ui.ui_setting_dialog import Ui_setting_dialog
from utils.config import Config


class SettingDialog(QDialog, Ui_setting_dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.init_ui()
        self.bind_op()

    def init_ui(self):
        self.setWindowTitle('设置')
        # 获取当前配置信息
        self.config = Config().get()
        print(self.config)
        # 配置填入页面
        # 保存位置
        save = ['cwd', 'warehouse', 'custom']
        self.save_position.addItems(save)
        if self.config['warehouse']['save_position'] in save:
            self.save_position.setCurrentText(
                self.config['warehouse']['save_position'])
        else:
            self.save_position.setCurrentIndex(0)
            self.config['warehouse']['save_position'] = 'cwd'
        # 保存路径
        self.save_path.setText(self.config['warehouse']['save_path'])
        if not self.config['warehouse']['save_position'] == 'custom':
            self.save_path.setEnabled(False)
        # 目录命名规则
        self.directory_rename_rule.setText(
            self.config['warehouse']['directory_rename_rule'])
        # 自动重命名
        auto = ['true', 'false']
        self.auto_rename.addItems(auto)
        if self.config['warehouse']['auto_rename'] in auto:
            self.auto_rename.setCurrentText(
                self.config['warehouse']['auto_rename'])
        else:
            self.auto_rename.setCurrentIndex(0)
            self.config['warehouse']['auto_rename'] = 'true'
        # 自动重命名规则
        self.auto_rename_rule.setText(
            self.config['warehouse']['auto_rename_rule'])
        if not self.config['warehouse']['auto_rename'] == 'true':
            self.auto_rename_rule.setEnabled(False)

    # 绑定输入操作
    def bind_op(self):
        self.save_position.currentTextChanged.connect(
            self.save_position_changed)
        self.save_path.editingFinished.connect(self.save_path_finished)
        self.directory_rename_rule.editingFinished.connect(
            self.directory_rename_rule_finished)
        self.auto_rename.currentTextChanged.connect(self.auto_rename_changed)
        self.auto_rename_rule.editingFinished.connect(
            self.auto_rename_rule_finished)

    # 改变保存位置
    def save_position_changed(self, text: str):
        if text == 'custom':
            self.save_path.setEnabled(True)
        else:
            self.save_path.setEnabled(False)
        self.config['warehouse']['save_position'] = text

    # 改变保存路径
    def save_path_finished(self):
        self.config['warehouse']['save_path'] = self.save_path.text()

    # 改变目录命名规则
    def directory_rename_rule_finished(self):
        self.config['warehouse'][
            'directory_rename_rule'] = self.directory_rename_rule.text()

    # 改变自动重命名
    def auto_rename_changed(self, text: str):
        if text == 'true':
            self.auto_rename_rule.setEnabled(True)
        else:
            self.auto_rename_rule.setEnabled(False)
        self.config['warehouse']['auto_rename'] = text

    # 改变自动重命名规则
    def auto_rename_rule_finished(self):
        self.config['warehouse'][
            'sauto_rename_rule'] = self.auto_rename_rule.text()

    def accept(self) -> None:
        Config().update(self.config)
        return super().accept()

    def reject(self) -> None:
        return super().reject()