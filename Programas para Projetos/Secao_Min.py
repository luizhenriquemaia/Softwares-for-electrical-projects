# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Secao_Min.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SecaoMin")
        MainWindow.setFixedSize(376, 170)
        MainWindow.setWindowTitle("Cálculo de Seção Mínima")
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblTipLinha = QtGui.QLabel(self.centralwidget)
        self.lblTipLinha.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.lblTipLinha.setObjectName("lblTipLinha")
        self.lblTipLinha.setText("Tipo de Linha: ")
        
        self.cmbTipLinha = QtGui.QComboBox(self.centralwidget)
        self.cmbTipLinha.setGeometry(QtCore.QRect(130, 20, 221, 22))
        self.cmbTipLinha.setObjectName("cmbTipLinha")
        ItemsTipLinha = ["", "Condutores e Cabos Isolados", "Condutores Nus"]
        self.cmbTipLinha.addItems(ItemsTipLinha)
        self.cmbTipLinha.currentIndexChanged.connect(self.ItemsUtilCirc)

        self.lblUtilCirc = QtGui.QLabel(self.centralwidget)
        self.lblUtilCirc.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.lblUtilCirc.setObjectName("lblUtilCirc")
        self.lblUtilCirc.setText("Utilização do Circuito")
        
        self.cmbUtilCirc = QtGui.QComboBox(self.centralwidget)
        self.cmbUtilCirc.setGeometry(QtCore.QRect(130, 50, 221, 22))
        self.cmbUtilCirc.setObjectName("cmbUtilCirc")

        self.lblSecaoMin = QtGui.QLabel(self.centralwidget)
        self.lblSecaoMin.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.lblSecaoMin.setObjectName("lblSecaoMin")
        self.lblSecaoMin.setText("Seção Mínima:")

        self.txtSecaoMin = QtGui.QLineEdit(self.centralwidget)
        self.txtSecaoMin.setGeometry(QtCore.QRect(130, 130, 190, 20))
        self.txtSecaoMin.setObjectName("txtSecaoMin")

        self.bntSecaoMin = QtGui.QPushButton(self.centralwidget)
        self.bntSecaoMin.setGeometry(QtCore.QRect(200, 90, 75, 23))
        self.bntSecaoMin.setObjectName("bntSecaoMin")
        self.bntSecaoMin.setText("Calcular")
        self.bntSecaoMin.clicked.connect(self.CalcSecaoMin)

        self.bntInfo = QtGui.QPushButton(self.centralwidget)
        self.bntInfo.setGeometry(QtCore.QRect(321,130, 30, 20))
        self.bntInfo.setObjectName("bntSecaoMin")
        self.bntInfo.setText("?")
        self.bntInfo.clicked.connect(self.Info)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


    def ItemsUtilCirc(self, MainWindow):
        self.cmbUtilCirc.clear()
        TipLinha = self.cmbTipLinha.currentIndex()

        if TipLinha == 0:
            ItemsUtilCirc = []
        else: 
            if TipLinha == 1:
                ItemsUtilCirc = ["Circuitos de Iluminação", "Circuitos de Força",
                                 "Circuitos de Sinalização e Controle"]
            else:
                ItemsUtilCirc = ["Circuito de Força",
                                 "Circuitos de Sinalização e Controle"]
            
        self.cmbUtilCirc.addItems(ItemsUtilCirc)


    def CalcSecaoMin(self):
        TipLinha = self.cmbTipLinha.currentIndex()
        TipUtilCirc = self.cmbUtilCirc.currentIndex()

        if TipLinha == 0:
            Secao = "Erro"
        else:
            if TipLinha == 1:
                if TipUtilCirc == 0:
                    Secao = "1,5 Cu e 16 Al"
                else: 
                    if TipUtilCirc == 1:
                        Secao = "2,5 Cu e 16 Al"
                    else:
                        Secao = "0,5 Cu"
            else:
                if TipUtilCirc == 0:
                    Secao = "10 Cu e 16 Al"
                else:
                    Secao = "4 Cu"

        self.txtSecaoMin.setText(Secao)


    def Info(self):
        self.msgbox = QtGui.QMessageBox(self.centralwidget)
        self.msgbox.setWindowTitle("Detalhes Sobre o Programa")
        self.msgbox.setText("O seguinte programa foi feito de acordo com a NBR 5410:2004 -> Tabela 47 página 113 -> Instalações fixas em geral")
        self.msgbox.exec_()
        
        
          
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

