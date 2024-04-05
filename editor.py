from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
from ui import Ui_MainWindow
import os


class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir=""
        self.ui.btn_dir.clicked.connect(self.open)


    def open(self):
        try:
            self.workdir=QtWidgets.QFileDialog.getExistingDirectory()
            print(self.workdir)
            files=os.listdir(self.workdir)
            files_new=self.sort_files(files)
            self.ui.list_files.clear()
            for file in files_new:
                self.ui.list_files.addItem(file)
        except:
            alert=QtWidgets.QMessageBox()
            alert.setText("Шлях до папки не вибрано!")
            alert.exec()
    def sort_files(self,files):
        extentions=[".jpg",".svg",".png",".jpeg"]
        result=[]
        for file in files:
            for ex in extentions:
                if file.endswith(ex):
                    result.append(file)
        return result





app=QtWidgets.QApplication([])
ex=ImageEditor()
ex.show()
app.exec()
