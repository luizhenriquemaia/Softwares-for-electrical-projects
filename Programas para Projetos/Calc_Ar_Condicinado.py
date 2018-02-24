from PyQt4 import QtCore, QtGui
from Func_Calc import calculoAr


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(310, 240)
        MainWindow.setWindowTitle("Cálculo Ar Condicionado")
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblExpo = QtGui.QLabel(self.centralwidget)
        self.lblExpo.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.lblExpo.setObjectName("lblAmbiente")
        self.lblExpo.setText("Ambiente Exposto ao Sol:")
        
        self.rbnExpo = QtGui.QRadioButton(self.centralwidget)
        self.rbnExpo.setGeometry(QtCore.QRect(160, 10, 51, 17))
        self.rbnExpo.setObjectName("rbnExpo")
        self.rbnExpo.setText("Sim")
        
        self.lblArea = QtGui.QLabel(self.centralwidget)
        self.lblArea.setGeometry(QtCore.QRect(20, 40, 141, 16))
        self.lblArea.setObjectName("lblArea")
        self.lblArea.setText("Area:")

        self.lneArea = QtGui.QLineEdit(self.centralwidget)
        self.lneArea.setGeometry(QtCore.QRect(160, 40, 110, 20))
        self.lneArea.setObjectName("lneArea")
        
        self.lblPessoas = QtGui.QLabel(self.centralwidget)
        self.lblPessoas.setGeometry(QtCore.QRect(20, 70, 141, 16))
        self.lblPessoas.setObjectName("lblPessoas")
        self.lblPessoas.setText("Pessoas no Ambiente:")
                
        self.lnePessoas = QtGui.QLineEdit(self.centralwidget)
        self.lnePessoas.setGeometry(QtCore.QRect(160, 70, 110, 20))
        self.lnePessoas.setObjectName("lnePessoas")
        
        self.lblAparelhos = QtGui.QLabel(self.centralwidget)
        self.lblAparelhos.setGeometry(QtCore.QRect(20, 100, 141, 16))
        self.lblAparelhos.setObjectName("lblAparelhos")
        self.lblAparelhos.setText("Aparelhos Fontes de Calor:")
                
        self.lneAparelhos = QtGui.QLineEdit(self.centralwidget)
        self.lneAparelhos.setGeometry(QtCore.QRect(160, 100, 110, 20))
        self.lneAparelhos.setObjectName("lneAparelhos")

        self.btnCalcular = QtGui.QPushButton(self.centralwidget)
        self.btnCalcular.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.btnCalcular.setObjectName("btnCalcular")
        self.btnCalcular.setText("Calcular")
        self.btnCalcular.clicked.connect(self.CalcAr)
        
        self.lblAr = QtGui.QLabel(self.centralwidget)
        self.lblAr.setGeometry(QtCore.QRect(20, 160, 141, 16))
        self.lblAr.setObjectName("lblAr")
        self.lblAr.setText("Potência Ar Condicionado:")
                
        self.lneArB = QtGui.QLineEdit(self.centralwidget)
        self.lneArB.setGeometry(QtCore.QRect(160, 160, 110, 20))
        self.lneArB.setObjectName("lneArB")

        self.lblIgual = QtGui.QLabel(self.centralwidget)
        self.lblIgual.setGeometry(QtCore.QRect(210, 180, 91, 16))
        self.lblIgual.setObjectName("lblIgual")
        self.lblIgual.setText("=")
                
        self.lneArW = QtGui.QLineEdit(self.centralwidget)
        self.lneArW.setGeometry(QtCore.QRect(160, 200, 110, 20))
        self.lneArW.setObjectName("lneArW")

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def CalcAr(self):
        exposicao = self.rbnExpo.isChecked()
        pessoas = int(self.lnePessoas.text())
        aparelhos = int(self.lneAparelhos.text())
        area = float(self.lneArea.text())
        
        arb = calculoAr(exposicao, pessoas, aparelhos, area)
        arw = round(((arb/3.412141633)/1000),2)
    
        self.lneArB.setText(str(arb)+ " BTUS")
        self.lneArW.setText(str(arw)+ " kW")
    


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

