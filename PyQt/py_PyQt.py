import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os
import numpy as np
import matplotlib.pyplot as plt
from nptdms import TdmsFile
from DFT_zeropadding import class_DFT


# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("D:/Git/Tools/PyQt/TorqueRippleAnalyzer.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ===================================================================
        # ======================== list Widgets Init ========================
        # ===================================================================
        self.ob_listWidget.setAlternatingRowColors(True)
        self.ob_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # ===================================================================
        # ========================== Buttons Init ===========================
        # ===================================================================
        self.ob_Start_Button.clicked.connect(self.call_Start_Button_Function)

        # ===================================================================
        # ========================== Menubar Init ===========================
        # ===================================================================
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

    # ===================================================================
    # ========================== Call Function ==========================
    # ===================================================================
    # === Buttons
    def call_Start_Button_Function(self):
        Widget_items = self.ob_listWidget.selectedItems()

        if not self.ob_listWidget.currentItem():  # 파일 선택 안하고 껐을 때 오류 방지
            return

        for index in Widget_items:
            each_Widget_item = str(index.text())
            tdms_file = TdmsFile(each_Widget_item)

            selected_tmds_data_Torque = tdms_file["Motor Performace Test Data"]["DRIVE TORQUE"]
            selected_tmds_data_Time = tdms_file["Motor Performace Test Data"]["Time"]
            
            # ===================================================================
            # To do : Motor Speed 받아서 Order 계산 자동화
            # ===================================================================
            
            FFT = class_DFT(selected_tmds_data_Torque, selected_tmds_data_Time, 4)
            Magnitude, Order = FFT.def_DFT()

            plt.plot(Order, Magnitude)
            
        plt.xlim(0,24)
        plt.ylim(0,0.15)
        plt.yticks([i*0.05 for i in range(1,4)])
        plt.xticks([j*1 for j in range(0,25)])
        plt.grid()
        plt.show()


    # === Menubar
    def call_openfile_Function(self):
        self.ob_listWidget.clear()
        files_path = QFileDialog.getOpenFileNames(self, "Open Files", "./")

        if files_path[0]:               # 파일 선택 안하고 껐을 때 오류 방지
            for i in range(len(files_path[0])):
                self.ob_listWidget.addItem(files_path[0][i])


    def call_openfolder_Function(self):
        self.ob_listWidget.clear()
        Paths_On_Widget = []

        folder_path = QFileDialog.getExistingDirectory(self, "Open Folders", "./", QFileDialog.ShowDirsOnly)
        if not folder_path:             # 파일 선택 안하고 껐을 때 오류 방지
            return

        file_list = os.listdir(folder_path)
        file_list.sort()
        file_list_tdms = [file for file in file_list if file.endswith(".tdms")]

        for i in range(len(file_list_tdms)):
            Paths_On_Widget.append(folder_path + '/' + file_list_tdms[i])
            self.ob_listWidget.addItem(Paths_On_Widget[i])


    def call_close_Function(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()