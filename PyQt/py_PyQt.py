import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os
import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
from nptdms import TdmsFile
from DFT_zeropadding import class_DFT


# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("C:/98_Git/Tools/PyQt/TorqueRippleAnalyzer.ui")[0]
=======
from nptdms import TdmsFile

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("D:/Git/Tools/PyQt/TorqueRippleAnalyzer.ui")[0]
>>>>>>> e082bf40fe2ee338213ec5bc31106f42fec570ab

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

<<<<<<< HEAD
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
=======
        # ====================== list Widgets Init
        self.ob_listWidget.setAlternatingRowColors(True)
        self.ob_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # ====================== Buttons Init
        self.ob_Start_Button.clicked.connect(self.call_Start_Button_Function)

        # ====================== Menubar Init
>>>>>>> e082bf40fe2ee338213ec5bc31106f42fec570ab
        # === Open new file
        new_action = QAction(QIcon("open.png"), "&Open File", self)
        new_action.setShortcut("Ctrl+O")
        new_action.setStatusTip("파일 열기")
        new_action.triggered.connect(self.call_openfile_Function)
<<<<<<< HEAD
=======

>>>>>>> e082bf40fe2ee338213ec5bc31106f42fec570ab
        # === Open folder
        open_action = QAction(QIcon("open.png"), "&Open Folder", self)
        open_action.setShortcut("Ctrl+K")
        open_action.setStatusTip("폴더 열기")
        open_action.triggered.connect(self.call_openfolder_Function)
<<<<<<< HEAD
=======

>>>>>>> e082bf40fe2ee338213ec5bc31106f42fec570ab
        # === Exit folder
        close_action = QAction(QIcon("close.png"), "&Exit", self)
        close_action.setShortcut("Ctrl+F4")
        close_action.setStatusTip("종료")
        close_action.triggered.connect(self.call_close_Function)
<<<<<<< HEAD
=======

>>>>>>> e082bf40fe2ee338213ec5bc31106f42fec570ab
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
<<<<<<< HEAD

            selected_tmds_data_Torque = tdms_file["Motor Performace Test Data"]["DRIVE TORQUE"]
            selected_tmds_data_Time = tdms_file["Motor Performace Test Data"]["Time"]
            FFT = class_DFT(selected_tmds_data_Torque, selected_tmds_data_Time, 4)
            Magnitude, Frequency = FFT.def_DFT()
            plt.plot(Frequency, Magnitude)
            
        plt.xlim(0,100)
        plt.grid()
        plt.show()

=======
            # print(tdms_file)
            # print(tdms_file['Motor Performace Test Data'])
            selected_tmds_data = tdms_file['Motor Performace Test Data']['Time']
        files_path = QFileDialog.getOpenFileNames(self, "Open Files", "./")
<<<<<<< HEAD

        if files_path[0]:               # 파일 선택 안하고 껐을 때 오류 방지
            for i in range(len(files_path[0])):
=======
        
        if files_path[0]:  # 파일 선택 안하고 껐을 때 오류 방지
            for i in range(len(files_path[0])):
                # with open(files_path[0][i], "r") as f:
                    # pass
                # file 내부 데이터 불러오기
                # file_data = f.read()
>>>>>>> e082bf40fe2ee338213ec5bc31106f42fec570ab
                self.ob_listWidget.addItem(files_path[0][i])


    def call_openfolder_Function(self):
        self.ob_listWidget.clear()
<<<<<<< HEAD
        Paths_On_Widget = []

        folder_path = QFileDialog.getExistingDirectory(self, "Open Folders", "./", QFileDialog.ShowDirsOnly)
        if not folder_path:             # 파일 선택 안하고 껐을 때 오류 방지
=======

        folder_path = QFileDialog.getExistingDirectory(self, "Open Folders", "./")
        if not folder_path:  # 파일 선택 안하고 껐을 때 오류 방지
>>>>>>> e082bf40fe2ee338213ec5bc31106f42fec570ab
            return

        file_list = os.listdir(folder_path)
        file_list.sort()
<<<<<<< HEAD
        file_list_tdms = [file for file in file_list if file.endswith(".tdms")]

        for i in range(len(file_list_tdms)):
            Paths_On_Widget.append(folder_path + '/' + file_list_tdms[i])
            self.ob_listWidget.addItem(Paths_On_Widget[i])

=======
        file_list_py = [file for file in file_list if file.endswith(".tdms")]

        for i in range(len(file_list_py)):
            self.ob_listWidget.addItem(file_list_py[i])
>>>>>>> e082bf40fe2ee338213ec5bc31106f42fec570ab

    def call_close_Function(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()