from PyQt4 import QtCore, QtGui
from math import sqrt


class Ui_Calc_Corrente(object):
    def _init_(self, Dialog):
        Dialog.setObjectName("Calc_Corrente")
        Dialog.resize(370, 291)
        
        self.lblTipCirc = QtGui.QLabel(Dialog)
        self.lblTipCirc.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.lblTipCirc.setObjectName("lblTipCirc")
        self.lblTipCirc.setText("Tipo de Circuito:")
        
        self.cmbTipCirc = QtGui.QComboBox(Dialog)
        self.cmbTipCirc.setGeometry(QtCore.QRect(120, 20, 191, 22))
        self.cmbTipCirc.setObjectName("cmbTipCirc")
        itemsTipCirc = ["", "Monofásico", "Trifásico Equilibrado", "Trifásico Desequilibrado"]
        self.cmbTipCirc.addItems(itemsTipCirc)
        
        self.lblPot = QtGui.QLabel(Dialog)
        self.lblPot.setGeometry(QtCore.QRect(30, 60, 61, 16))
        self.lblPot.setObjectName("lblPot")
        self.lblPot.setText("Potência:")

        self.lnePot = QtGui.QLineEdit(Dialog)
        self.lnePot.setGeometry(QtCore.QRect(120, 60, 191, 20))
        self.lnePot.setObjectName("lnePot")
        
        self.lblTensao = QtGui.QLabel(Dialog)
        self.lblTensao.setGeometry(QtCore.QRect(30, 90, 46, 13))
        self.lblTensao.setObjectName("lblTensao")
        self.lblTensao.setText("Tensão:")
                
        self.lneTensao = QtGui.QLineEdit(Dialog)
        self.lneTensao.setGeometry(QtCore.QRect(120, 90, 191, 20))
        self.lneTensao.setObjectName("lneTensao")

        self.lblFator = QtGui.QLabel(Dialog)
        self.lblFator.setGeometry(QtCore.QRect(30, 120, 91, 16))
        self.lblFator.setObjectName("lblFator")
        self.lblFator.setText("Fator de Potência:")
        
        self.lneFator = QtGui.QLineEdit(Dialog)
        self.lneFator.setGeometry(QtCore.QRect(120, 120, 191, 20))
        self.lneFator.setObjectName("lneFator")
                
        self.lblRend = QtGui.QLabel(Dialog)
        self.lblRend.setGeometry(QtCore.QRect(30, 150, 91, 16))
        self.lblRend.setObjectName("lblRend")
        self.lblRend.setText("Rendimento:")
        
        self.lneRend = QtGui.QLineEdit(Dialog)
        self.lneRend.setGeometry(QtCore.QRect(120, 150, 191, 20))
        self.lneRend.setObjectName("lneRend")

        self.btnCalcular = QtGui.QPushButton(Dialog)
        self.btnCalcular.setGeometry(QtCore.QRect(170, 180, 75, 23))
        self.btnCalcular.setObjectName("btnCalcular")
        self.btnCalcular.setText("Calcular")
        self.btnCalcular.clicked.connect(self.CalcCorr)
        
        self.lblCorrente = QtGui.QLabel(Dialog)
        self.lblCorrente.setGeometry(QtCore.QRect(30, 210, 91, 16))
        self.lblCorrente.setObjectName("lblCorrente")
        self.lblCorrente.setText("Corrente")
        
        self.lneCorrente = QtGui.QLineEdit(Dialog)
        self.lneCorrente.setGeometry(QtCore.QRect(120, 210, 191, 20))
        self.lneCorrente.setObjectName("lneCorrente")

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def CalcCorr(self):
        TipCirc = self.cmbTipCirc.currentIndex()
        
        if TipCirc == 0:
            Corrente = "Erro"

        else:
            Potencia = float(self.lnePot.text())
            Tensao = float(self.lneTensao.text())
            Fator = float(self.lneFator.text())
            Rendimento = float(self.lneRend.text())

            if TipCirc == 1:
                Corrente = Potencia/(Tensao*Fator*Rendimento)
            elif TipCirc == 2:
                Corrente = Potencia/(sqrt(3)*Tensao*Fator*Rendimento)
            else:
                Corrente = Potencia/(3*Tensao*Fator*Rendimento)

            Corrente = round(Corrente,2)
            
        
        self.lneCorrente.setText(str(Corrente))
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Calc_Corrente()
    ui._init_(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

