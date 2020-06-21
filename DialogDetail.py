# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogDetail.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import requests
import urllib

baseURL = "https://api.jikan.moe/v3/anime/"

class Ui_DialogDetail(object):
    def setupUi(self, DialogDetail):
        DialogDetail.setObjectName("DialogDetail")
        DialogDetail.resize(779, 608)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        DialogDetail.setFont(font)
        self.btnBack = QtWidgets.QPushButton(DialogDetail)
        self.btnBack.setGeometry(QtCore.QRect(20, 550, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.widget = QtWidgets.QWidget(DialogDetail)
        self.widget.setGeometry(QtCore.QRect(20, 10, 731, 523))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblTitle = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setScaledContents(True)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_4.addWidget(self.lblTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblImage = QtWidgets.QLabel(self.widget)
        self.lblImage.setMinimumSize(QtCore.QSize(225, 315))
        self.lblImage.setMaximumSize(QtCore.QSize(225, 315))
        self.lblImage.setScaledContents(True)
        self.lblImage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblImage.setObjectName("lblImage")
        self.horizontalLayout.addWidget(self.lblImage, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tblChara = QtWidgets.QTableWidget(self.widget)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.tblChara.setFont(font)
        self.tblChara.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblChara.setDragDropOverwriteMode(False)
        self.tblChara.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tblChara.setGridStyle(QtCore.Qt.SolidLine)
        self.tblChara.setObjectName("tblChara")
        self.tblChara.setColumnCount(3)
        self.tblChara.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        item.setFont(font)
        self.tblChara.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        item.setFont(font)
        self.tblChara.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        item.setFont(font)
        self.tblChara.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tblChara)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listEpisode = QtWidgets.QListWidget(self.widget)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.listEpisode.setFont(font)
        self.listEpisode.setObjectName("listEpisode")
        self.verticalLayout.addWidget(self.listEpisode)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogDetail)
        self.btnBack.clicked.connect(DialogDetail.close)
        QtCore.QMetaObject.connectSlotsByName(DialogDetail)

    #Fill UI
    def setDetail(self, ID_Anime) :
        #Get API
        self.getAnime = requests.get(baseURL + str(ID_Anime)).json()

        #Fill label title and image
        self.lblTitle.setText(self.getAnime['title'])
        self.lblTitle.adjustSize()
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)

        #Set IMG from URL
        url = str(self.getAnime['image_url'])
        getImg = urllib.request.urlopen(url).read()
        
        image = QtGui.QImage()
        image.loadFromData(getImg)

        self.lblImage.setPixmap(QtGui.QPixmap(image))
        self.lblImage.setScaledContents(True)

        self.fillTableChara(ID_Anime)
        self.fillListEps(ID_Anime)


    def fillTableChara(self, ID_Anime) :
        #Get API
        self.getAnimeChara = requests.get(baseURL + str(ID_Anime) + '/characters_staff').json()
        data = self.getAnimeChara['characters']
        
        #Var for table
        row = int(0)
        self.tblChara.setRowCount(len(data))
        #Start Add
        for item in data :
            #Get Voice Actors
            dataVA = item['voice_actors']
            voice_actor = ""
            for count_va in dataVA :
                voice_actor = voice_actor + count_va['name'] + '(' + count_va['language'] + ')' + ';\n'
            
            #Add to Table
            #Add Name
            self.tblChara.setItem(row, 0, QTableWidgetItem(item['name']))
            #Add Role
            self.tblChara.setItem(row, 1, QTableWidgetItem(item['role']))
            #Add Voice Actor
            self.tblChara.setItem(row, 2, QTableWidgetItem(voice_actor))
            row += 1
        
        #Resize column and row to content
        self.tblChara.resizeColumnsToContents()
        self.tblChara.resizeRowsToContents()

    def fillListEps(self, ID_Anime) :
        #Get API
        self.getAnimeEps = requests.get(baseURL + str(ID_Anime) + '/episodes').json()
        data = self.getAnimeEps['episodes']
        
        if data :
            for item in data :
                if item['title_romanji']:
                    count = str(item['episode_id'])
                    self.listEpisode.addItem(count + '. ' + str(item['title_romanji']))
                else :
                    count = str(item['episode_id'])
                    self.listEpisode.addItem(count + '. ' + str(item['title']))
        else :
            print('tidak ada didaftar !')
            self.listEpisode.addItem('No episode list !')

    def retranslateUi(self, DialogDetail):
        _translate = QtCore.QCoreApplication.translate
        DialogDetail.setWindowTitle(_translate("DialogDetail", "Anime"))
        self.btnBack.setText(_translate("DialogDetail", "Close"))
        self.lblTitle.setText(_translate("DialogDetail", "Title"))
        self.lblImage.setText(_translate("DialogDetail", "IMAGE"))
        self.label_2.setText(_translate("DialogDetail", "List Character :"))
        item = self.tblChara.horizontalHeaderItem(0)
        item.setText(_translate("DialogDetail", "Name"))
        item = self.tblChara.horizontalHeaderItem(1)
        item.setText(_translate("DialogDetail", "Role"))
        item = self.tblChara.horizontalHeaderItem(2)
        item.setText(_translate("DialogDetail", "Seiyuu"))
        self.label.setText(_translate("DialogDetail", "List Episode :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogDetail = QtWidgets.QDialog()
    ui = Ui_DialogDetail()
    ui.setupUi(DialogDetail)
    DialogDetail.show()
    sys.exit(app.exec_())
