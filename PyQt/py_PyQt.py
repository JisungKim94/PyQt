import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("untitled.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ob_listView = QListWidget(self.ob_listView )
        self.ob_listView.itemClicked.connect(self.chkItemClicked)
        self.ob_listView.itemDoubleClicked.connect(self.chkItemDoubleClicked)
        self.ob_listView.currentItemChanged.connect(self.chkCurrentItemChanged)

        fruits = ["banana", "apple", "melon", "pear"]
        view = self.ob_listView
        model = QStandardItemModel()
        for f in fruits:
            model.appendRow(QStandardItem(f))
        
    #ListWidget의 시그널에 연결된 함수들
    def chkItemClicked(self):
        print(self.listWidget_Test.currentItem().text())

    def chkItemDoubleClicked(self):
        print(str(self.listWidget_Test.currentRow()) + " : " + self.listWidget_Test.currentItem().text())

    def chkCurrentItemChanged(self) :
        print("Current Row : " + str(self.listWidget_Test.currentRow()))


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()