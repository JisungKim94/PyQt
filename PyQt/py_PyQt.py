import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os
import numpy as np
from nptdms import TdmsFile

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("D:/Git/Tools/PyQt/TorqueRippleAnalyzer.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ====================== list Widgets Init
        self.ob_listWidget.setAlternatingRowColors(True)
        self.ob_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # ====================== Buttons Init
        self.ob_Start_Button.clicked.connect(self.call_Start_Button_Function)

        # ====================== Menubar Init
        # === Open new file
        new_action = QAction(QIcon("open.png"), "&Open File", self)
        new_action.setShortcut("Ctrl+O")
        new_action.setStatusTip("파일 열기")
        new_action.triggered.connect(self.call_openfile_Function)

        # === Open folder
        open_action = QAction(QIcon("open.png"), "&Open Folder", self)
        open_action.setShortcut("Ctrl+K")
        open_action.setStatusTip("폴더 열기")
        open_action.triggered.connect(self.call_openfolder_Function)

        # === Exit folder
        close_action = QAction(QIcon("close.png"), "&Exit", self)
        close_action.setShortcut("Ctrl+F4")
        close_action.setStatusTip("종료")
        close_action.triggered.connect(self.call_close_Function)

        # === Connect menu
        self.ob_menuFile.addAction(new_action)
        self.ob_menuFile.addAction(open_action)
        self.ob_menuFile.addAction(close_action)

    # ====================== Call Function
    # === list Widgets

    # === Buttons
    def call_Start_Button_Function(self):
        Widget_items = self.ob_listWidget.selectedItems()

        if not self.ob_listWidget.currentItem():    # 파일 선택 안하고 껐을 때 오류 방지
            return

        for index in Widget_items:
            each_Widget_item = str(index.text())
            tdms_file = TdmsFile(each_Widget_item)
            # print(tdms_file)
            # print(tdms_file['Motor Performace Test Data'])
            selected_tmds_data = tdms_file['Motor Performace Test Data']['Time']
            # print(selected_tmds_data.data)

    # === Menubar
    def call_openfile_Function(self):
        self.ob_listWidget.clear()
        files_path = QFileDialog.getOpenFileNames(self, "Open Files", "./")
        
        if files_path[0]:  # 파일 선택 안하고 껐을 때 오류 방지
            for i in range(len(files_path[0])):
                # with open(files_path[0][i], "r") as f:
                    # pass
                # file 내부 데이터 불러오기
                # file_data = f.read()
                self.ob_listWidget.addItem(files_path[0][i])


    def call_openfolder_Function(self):
        self.ob_listWidget.clear()

        folder_path = QFileDialog.getExistingDirectory(self, "Open Folders", "./")
        if not folder_path:  # 파일 선택 안하고 껐을 때 오류 방지
            return

        file_list = os.listdir(folder_path)
        file_list.sort()
        file_list_py = [file for file in file_list if file.endswith(".tdms")]

        for i in range(len(file_list_py)):
            self.ob_listWidget.addItem(file_list_py[i])

    def call_close_Function(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()