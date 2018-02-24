from PyQt4 import QtCore, QtGui
from Calc_Corrente import Ui_Calc_Corrente
from Tab36e38 import *
from Tab37e39 import *


class Ui_Cap_Cond(object):
    def _init_(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(580, 260)
        MainWindow.setWindowTitle("Cálculo da Seção Nominal do Condutor Por Capacidade de Condução de Corrente")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lblTipIso = QtGui.QLabel(self.centralwidget)
        self.lblTipIso.setGeometry(QtCore.QRect(20, 20, 150, 23))
        self.lblTipIso.setObjectName("lblTipIsol")
        self.lblTipIso.setText("Tipo de Isolação")

        self.cmbTipIso = QtGui.QComboBox(self.centralwidget)
        self.cmbTipIso.setGeometry(QtCore.QRect(180, 20, 380, 23))
        self.cmbTipIso.setObjectName("cmbTipIsol")
        ItemsTipIso = ["", "PVC até 300mm²", "PVC Maior que 300mm²", "EPR", "XLPE"]
        self.cmbTipIso.addItems(ItemsTipIso)

        self.lblMetRef = QtGui.QLabel(self.centralwidget)
        self.lblMetRef.setGeometry(QtCore.QRect(20, 60, 150, 23))
        self.lblMetRef.setObjectName("lblMetRef")
        self.lblMetRef.setText("Método de Referência")

        self.cmbMetRef = QtGui.QComboBox(self.centralwidget)
        self.cmbMetRef.setGeometry(QtCore.QRect(180, 60, 380, 23))
        self.cmbMetRef.setObjectName("cmbMetRef")
        ItemsMetRef = ["", "A1: Condutores Isolados em Eletroduto de Seção Circular Embutido em Parede Termicamente Isolante",
                       "A2: Cabo Multipolar em Eletroduto de Seção Circular Embutido em Parede Termicamente Isolante",
                       "B1: Condutores Isolados em Eletroduto de Seção Circular Sobre Parede de Madeira",
                       "B2: Cabo Multipolar em Eletroduto de Seção Circular Sobre Parede de Madeira",
                       "C: Cabos Unipolares ou Cabo Multipolar Sobre Parede de Madeira",
                       "D: Cabos Multipolar em Eletroduto Enterrado no Solo",
                       "E: Cabo Multipolar ao Ar Livre",
                       "F: Cabos Unipolares Justapostos ao Ar Livre",
                       "G: Cabos Unipolares Espaçados ao Ar Livre"]
        self.cmbMetRef.addItems(ItemsMetRef)
        self.cmbMetRef.activated.connect(self.ItemsCondVivos)

        self.lblCorNom = QtGui.QLabel(self.centralwidget)
        self.lblCorNom.setGeometry(QtCore.QRect(20, 100, 150, 23))
        self.lblCorNom.setObjectName("lblCorNom")
        self.lblCorNom.setText("Corrente Nominal")

        self.lneCorNom = QtGui.QLineEdit(self.centralwidget)
        self.lneCorNom.setGeometry(QtCore.QRect(180, 100, 80, 23))
        self.lneCorNom.setObjectName("cmbCorNom")
        
        self.btnCalCorNom = QtGui.QPushButton(self.centralwidget)
        self.btnCalCorNom.setGeometry(QtCore.QRect(270, 100, 70, 23))
        self.btnCalCorNom.setObjectName("btnCalCorNom")
        self.btnCalCorNom.setText("Calcular")
        self.btnCalCorNom.clicked.connect(self.Cal_Corrente)

        self.lblFatores = QtGui.QLabel(self.centralwidget)
        self.lblFatores.setGeometry(QtCore.QRect(380, 100, 100, 23))
        self.lblFatores.setObjectName("lblFatores")
        self.lblFatores.setText("Fatores de Correção:")
        
        self.btnFatores = QtGui.QPushButton(self.centralwidget)
        self.btnFatores.setGeometry(QtCore.QRect(490, 100, 70, 23))
        self.btnFatores.setObjectName("btnFatores")
        self.btnFatores.setText("Aplicar")
        #self.btnFatores.clicked.connect()

        self.lblCondVivos = QtGui.QLabel(self.centralwidget)
        self.lblCondVivos.setGeometry(QtCore.QRect(20, 140, 150, 23))
        self.lblCondVivos.setObjectName("lblCondVivos")
        self.lblCondVivos.setText("Esquema de Condutores Vivos")

        self.cmbCondVivos = QtGui.QComboBox(self.centralwidget)
        self.cmbCondVivos.setGeometry(QtCore.QRect(180, 140, 380, 23))
        self.cmbCondVivos.setObjectName("cmbCondVivos")

        self.btnCalcSecao = QtGui.QPushButton(self.centralwidget)
        self.btnCalcSecao.setGeometry(QtCore.QRect(340, 180, 75, 23))
        self.btnCalcSecao.setObjectName("btnCalcSecao")
        self.btnCalcSecao.setText("Calcular")
        self.btnCalcSecao.clicked.connect(self.CalCapCorr)

        self.lblSecaoNom = QtGui.QLabel(self.centralwidget)
        self.lblSecaoNom.setGeometry(QtCore.QRect(20, 210, 150, 23))
        self.lblSecaoNom.setObjectName("lblSecaoNom")
        self.lblSecaoNom.setText("Seção Nominal Condutor")

        self.lneSecaoNom = QtGui.QLineEdit(self.centralwidget)
        self.lneSecaoNom.setGeometry(QtCore.QRect(180, 210, 355, 23))
        self.lneSecaoNom.setObjectName("lineEdit")
        self.lneSecaoNom.setReadOnly(True)

        self.btnInfoSecaoNom = QtGui.QPushButton(self.centralwidget)
        self.btnInfoSecaoNom.setGeometry(QtCore.QRect(540, 210, 20, 23))
        self.btnInfoSecaoNom.setObjectName("btnInfoSecaoNom")
        self.btnInfoSecaoNom.setText("?")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def ItemsCondVivos(self, MainWindow):
        self.cmbCondVivos.clear()
        MetRef = self.cmbMetRef.currentIndex()

        if MetRef == 0:
            ItemsCondVivos = []
        elif MetRef == 8:
            ItemsCondVivos = ["", "2 Condutores Carregados Justapostos", "3 Condutores Carregados Trifólio", "3 Condutores Carregados Justapostos"]
        elif MetRef == 9:
            ItemsCondVivos = ["", "3 Condutores Carregados na Horizontal", "3 Condutores Carregados na Vertical"]
        else:
            ItemsCondVivos = ["", "Monofásico a Dois Condutores", "Monofásico a Três Condutores",
                              "Duas Fases Sem Neutro", "Duas Fases Com Neutro",
                              "Trifásico Sem Neutro", "Trifásico Com Neutro"]
            
        self.cmbCondVivos.addItems(ItemsCondVivos)

    def CalCapCorr(self):
        TipIso = self.cmbTipIso.currentIndex()
        MetRef = self.cmbMetRef.currentIndex()
        NumCondCar = self.cmbCondVivos.currentIndex()
        
        if TipIso == 0 or MetRef == 0 or NumCondCar == 0:
            SecNom = "Erro"
        else:
            CorNom = float(self.lneCorNom.text())
            if TipIso == 1 or TipIso == 2:
                SecNom = tab36e38(MetRef, NumCondCar, CorNom)
            elif TipIso == 3 or TipIso == 4:
                SecNom = tab37e39(MetRef, NumCondCar, CorNom)
        self.lneSecaoNom.setText(str(SecNom))


    def Cal_Corrente(self):
        self.Calc_Corrente = Ui_Calc_Corrente()
        self.Calc_Corrente.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Cap_Cond()
    ui._init_(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
