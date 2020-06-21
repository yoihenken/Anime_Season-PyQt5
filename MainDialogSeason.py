# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogSeason.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from DialogDetail import*
import requests

baseURL = "https://api.jikan.moe/v3/season/"

class Ui_DialogSeason(QMainWindow):
    def setupUi(self, DialogSeason):
        DialogSeason.setObjectName("DialogSeason")
        DialogSeason.resize(365, 486)
        font = QtGui.QFont()
        font.setPointSize(12)
        DialogSeason.setFont(font)
        self.label_3 = QtWidgets.QLabel(DialogSeason)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.listSeason = QtWidgets.QListWidget(DialogSeason)
        self.listSeason.setGeometry(QtCore.QRect(25, 260, 321, 192))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.listSeason.setFont(font)
        self.listSeason.setObjectName("listSeason")
        self.layoutWidget = QtWidgets.QWidget(DialogSeason)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 139, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbSeason = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cbSeason.setFont(font)
        self.cbSeason.setObjectName("cbSeason")
        self.cbSeason.addItem("")
        self.cbSeason.addItem("")
        self.cbSeason.addItem("")
        self.cbSeason.addItem("")
        self.verticalLayout_2.addWidget(self.cbSeason)
        self.lnYear = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(8)
        self.lnYear.setFont(font)
        self.lnYear.setObjectName("lnYear")
        self.verticalLayout_2.addWidget(self.lnYear)
        self.layoutWidget1 = QtWidgets.QWidget(DialogSeason)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 50, 84, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lblTitle_2 = QtWidgets.QLabel(DialogSeason)
        self.lblTitle_2.setGeometry(QtCore.QRect(60, 0, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle_2.setFont(font)
        self.lblTitle_2.setObjectName("lblTitle_2")
        self.pushButton = QtWidgets.QPushButton(DialogSeason)
        self.pushButton.setGeometry(QtCore.QRect(230, 70, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DialogSeason)
        QtCore.QMetaObject.connectSlotsByName(DialogSeason)

        #Coding
        self.pushButton.clicked.connect(self.actionSubmit)
        self.listSeason.doubleClicked.connect(self.detailAnime)

    #MessageBox method
    def message(self, title, value) :
        QtWidgets.QMessageBox().about(QtWidgets.QMessageBox(), title, value)


    def actionSubmit(self) :
        #Delete list
        self.listSeason.clear()
        
        #Get Value season
        season = str(self.cbSeason.currentText())
        print(season)
        
        #Get Value Year
        year = 0
        #Try Catch jika year diisi integer
        try :
            year = int(self.lnYear.text())
            print(year)

            #Get API
            self.getAnime = requests.get(baseURL + str(year) + "/" + str(season)+ "/").json()
            data = self.getAnime['anime']

            if data :
                self.fillList(data)
            else :
                print('tidak ada didaftar !')
                self.message("No Anime", "There is nothing in this Season dan this Year!")
        
        except ValueError :
            print('gabisaaas')
            self.message("Error !", "Fill with number!")
    
    #Fill list Season
    def fillList(self, data=[]) :
        count = 0
        for item in data :
            count += 1
            self.listSeason.addItem(str(count) + '. ' + item['title'])

    #Go to new Form
    def detailAnime(self) :
        data = self.getAnime['anime']
        getID = []
        for item in data :
            getID.append(int(item['mal_id']))
        print(getID)
        ID_Anime = getID.pop(self.listSeason.currentRow())
        print(ID_Anime)

        #Open new form
        form = QDialog()
        self.uiAnime = Ui_DialogDetail()
        self.uiAnime.setupUi(form)
        self.uiAnime.setDetail(ID_Anime) #Send ID From Anime API
        form.show()
        form.exec_()
        
    def retranslateUi(self, DialogSeason):
        _translate = QtCore.QCoreApplication.translate
        DialogSeason.setWindowTitle(_translate("DialogSeason", "Anime Season"))
        self.label_3.setText(_translate("DialogSeason", "List Anime :"))
        self.cbSeason.setItemText(0, _translate("DialogSeason", "Summer"))
        self.cbSeason.setItemText(1, _translate("DialogSeason", "Spring"))
        self.cbSeason.setItemText(2, _translate("DialogSeason", "Fall"))
        self.cbSeason.setItemText(3, _translate("DialogSeason", "Winter"))
        self.label.setText(_translate("DialogSeason", "Season :"))
        self.label_2.setText(_translate("DialogSeason", "Year :"))
        self.lblTitle_2.setText(_translate("DialogSeason", "Anime For Life"))
        self.pushButton.setText(_translate("DialogSeason", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogSeason = QtWidgets.QDialog()
    ui = Ui_DialogSeason()
    ui.setupUi(DialogSeason)
    DialogSeason.show()
    sys.exit(app.exec_())
