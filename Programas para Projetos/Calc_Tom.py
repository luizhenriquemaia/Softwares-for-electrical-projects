# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc_Tom.ui'
#
# Created by: PyQt4 UI code generator 4.11.4

from PyQt4 import QtCore, QtGui
from Func_Calc import calculoTom


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(404, 263)
        MainWindow.setWindowTitle("Cálculo de TUGs")

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblAmb = QtGui.QLabel(self.centralwidget)
        self.lblAmb.setGeometry(QtCore.QRect(40, 20, 51, 16))
        self.lblAmb.setObjectName("lbl_Amb")
        self.lblAmb.setText("Ambiente")

        self.cmbAmb = QtGui.QComboBox(self.centralwidget)
        self.cmbAmb.setGeometry(QtCore.QRect(100, 20, 271, 22))
        self.cmbAmb.setObjectName("cmbAmb")
        ItemsAmb = ["", "Cômodo Comum", "Cozinha, Copa, Área de Serviço",
                    "Subsolo, Varanda, Garagem, Sótãos", "Banheiro"]
        self.cmbAmb.addItems(ItemsAmb)

        self.lblLarg = QtGui.QLabel(self.centralwidget)
        self.lblLarg.setGeometry(QtCore.QRect(40, 60, 51, 16))
        self.lblLarg.setObjectName("lblLarg")
        self.lblLarg.setText("Largura")

        self.txtLarg = QtGui.QLineEdit(self.centralwidget)
        self.txtLarg.setGeometry(QtCore.QRect(100, 60, 81, 31))
        self.txtLarg.setObjectName("txtLarg")

        self.lblComp = QtGui.QLabel(self.centralwidget)
        self.lblComp.setGeometry(QtCore.QRect(190, 60, 71, 16))
        self.lblComp.setObjectName("lblComp")
        self.lblComp.setText("Comprimento")

        self.txtComp = QtGui.QLineEdit(self.centralwidget)
        self.txtComp.setGeometry(QtCore.QRect(260, 60, 71, 31))
        self.txtComp.setObjectName("txtComp")

        self.btnPer = QtGui.QPushButton(self.centralwidget)
        self.btnPer.setGeometry(QtCore.QRect(340, 60, 31, 31))
        self.btnPer.setObjectName("btnPer")
        self.btnPer.setText("Ok")
        self.btnPer.clicked.connect(self.Periodo)

        self.txtPer = QtGui.QLineEdit(self.centralwidget)
        self.txtPer.setGeometry(QtCore.QRect(100, 100, 271, 31))
        self.txtPer.setObjectName("txtPer")
        
        self.lblPer = QtGui.QLabel(self.centralwidget)
        self.lblPer.setGeometry(QtCore.QRect(40, 110, 51, 16))
        self.lblPer.setObjectName("lblPer")
        self.lblPer.setText("Perímetro")

        self.lblTom = QtGui.QLabel(self.centralwidget)
        self.lblTom.setGeometry(QtCore.QRect(40, 200, 121, 16))
        self.lblTom.setObjectName("lblTom")
        self.lblTom.setText("Quantidade Tomadas")

        self.txtTom = QtGui.QLineEdit(self.centralwidget)
        self.txtTom.setGeometry(QtCore.QRect(170, 190, 201, 31))
        self.txtTom.setObjectName("txtTom")

        self.btnCalc = QtGui.QPushButton(self.centralwidget)
        self.btnCalc.setGeometry(QtCore.QRect(290, 150, 75, 23))
        self.btnCalc.setObjectName("btnCalc")
        self.btnCalc.setText("Calcular")
        self.btnCalc.clicked.connect(self.Calculo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


    def Periodo(self):
        largura = self.txtLarg.text()
        comprimento = self.txtComp.text()
        periodo = 2*(float(largura) + float(comprimento))
        self.txtPer.setText(str(periodo))
        
        return periodo


    def Calculo(self):
        periodo = self.txtPer.text()
        ambiente = self.cmbAmb.currentIndex()

        minTom = calculoTom(periodo, ambiente)
        self.txtTom.setText(str(minTom))
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
