from PyQt4 import QtCore, QtGui
from Func_Calc import calcCur, calcDrop
from Tabelas import tab36e38, tab37e39, tabNeutro, tabProt


class Ui_CondSec(object):
    def _init_(self, MainWindow):
        MainWindow.setFixedSize(202, 238)
        MainWindow.setWindowTitle("Seção Condutores")
        self.centralwidget = QtGui.QWidget(MainWindow)
        
        self.btnMinSec = QtGui.QPushButton(self.centralwidget)
        self.btnMinSec.setGeometry(QtCore.QRect(30, 20, 141, 31))
        self.btnMinSec.setText("Seção Mínima")
        self.btnMinSec.clicked.connect(self.openMinSec)
        
        self.lneMinSec = QtGui.QLineEdit(self.centralwidget)
        self.lneMinSec.setGeometry(QtCore.QRect(30, 60, 141, 20))

        self.btnCondCap = QtGui.QPushButton(self.centralwidget)
        self.btnCondCap.setGeometry(QtCore.QRect(30, 90, 141, 31))
        self.btnCondCap.setText("Capacidade de Condução")
        self.btnCondCap.clicked.connect(self.openCalcCurrent)
        
        self.lneCondCap = QtGui.QLineEdit(self.centralwidget)
        self.lneCondCap.setGeometry(QtCore.QRect(30, 130, 141, 20))
        
        self.btnVolDrop = QtGui.QPushButton(self.centralwidget)
        self.btnVolDrop.setGeometry(QtCore.QRect(30, 160, 141, 31))
        self.btnVolDrop.setText("Queda de Tensão")
        self.btnVolDrop.clicked.connect(self.openCalcDropVol)

        self.lneVolDrop = QtGui.QLineEdit(self.centralwidget)
        self.lneVolDrop.setGeometry(QtCore.QRect(30, 200, 141, 20))
        MainWindow.setCentralWidget(self.centralwidget)

    def openMinSec(self):
        self.window = QtGui.QDialog()
        self.ui = Ui_MinSec()
        self.ui._init_(self.window)
        self.window.show()

    def openCalcCurrent(self):
        self.window = QtGui.QDialog()
        self.ui = Ui_CarCap()
        self.ui._init_(self.window)
        self.window.show()

    def openCalcDropVol(self):
        self.window = QtGui.QDialog()
        self.ui = Ui_DropVolt()
        self.ui._init_(self.window)
        self.window.show()
        
###############################Seção Mínima#####################################
class Ui_MinSec(object):
    def _init_(self, Dialog):
        Dialog.setFixedSize(376, 200)
        Dialog.setWindowTitle("Seção Mínima")
        self.centralwidget = QtGui.QWidget(Dialog)
        
        self.lblTypLine = QtGui.QLabel(self.centralwidget)
        self.lblTypLine.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.lblTypLine.setText("Tipo de Linha: ")
        
        self.cmbTypLine = QtGui.QComboBox(self.centralwidget)
        self.cmbTypLine.setGeometry(QtCore.QRect(130, 20, 221, 22))
        ItemsTypLine = ["", "Condutores e Cabos Isolados", "Condutores Nus"]
        self.cmbTypLine.addItems(ItemsTypLine)
        self.cmbTypLine.currentIndexChanged.connect(self.ItemsUseCirc)

        self.lblUseCirc = QtGui.QLabel(self.centralwidget)
        self.lblUseCirc.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.lblUseCirc.setText("Utilização do Circuito:")
        
        self.cmbUseCirc = QtGui.QComboBox(self.centralwidget)
        self.cmbUseCirc.setGeometry(QtCore.QRect(130, 50, 221, 22))
        
        self.bntMinSec = QtGui.QPushButton(self.centralwidget)
        self.bntMinSec.setGeometry(QtCore.QRect(200, 90, 75, 23))
        self.bntMinSec.setText("Calcular")
        self.bntMinSec.clicked.connect(self.CalcMinSec)

        self.lblMinSec = QtGui.QLabel(self.centralwidget)
        self.lblMinSec.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.lblMinSec.setText("Seção Mínima:")

        self.lneMinSec = QtGui.QLineEdit(self.centralwidget)
        self.lneMinSec.setGeometry(QtCore.QRect(130, 130, 221, 20))

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ItemsUseCirc(self, MainWindow):
        self.cmbUseCirc.clear()
        lineTyp = self.cmbTypLine.currentIndex()
        if lineTyp == 0:
            ItemsUseCirc = []
        else: 
            if lineTyp == 1:
                ItemsUseCirc = ["Circuitos de Iluminação", "Circuitos de Força",
                                 "Circuitos de Sinalização e Controle"]
            else:
                ItemsUseCirc = ["Circuito de Força",
                                 "Circuitos de Sinalização e Controle"]
        self.cmbUseCirc.addItems(ItemsUseCirc)

    def CalcMinSec(self):
        lineTyp = self.cmbTypLine.currentIndex()
        useCirc = self.cmbUseCirc.currentIndex()
        if lineTyp == 0:
            section = "Erro"
        else:
            if lineTyp == 1:
                if useCirc == 0:
                    section = "1,5 Cu e 16 Al"
                else: 
                    if useCirc == 1:
                        section = "2,5 Cu e 16 Al"
                    else:
                        section = "0,5 Cu"
            else:
                if useCirc == 0:
                    section = "10 Cu e 16 Al"
                else:
                    section = "4 Cu"
        self.lneMinSec.setText(section)

    def Info(self):
        self.msgbox = QtGui.QMessageBox(self.centralwidget)
        self.msgbox.setWindowTitle("Detalhes Sobre o Programa")
        self.msgbox.setText("O seguinte programa foi feito de acordo com a NBR 5410:2004 -> Tabela 47 página 113 -> Instalações fixas em geral")
        self.msgbox.exec_()

########################Capacidade de Condução de Corrente#####################
class Ui_CarCap(object):
    def _init_(self, Dialog):
        Dialog.setFixedSize(490, 340)
        Dialog.setWindowTitle("Capacidade de Condução de Corrente")
        self.centralwidget = QtGui.QWidget(Dialog)

        self.lblTypeIso = QtGui.QLabel(self.centralwidget)
        self.lblTypeIso.setGeometry(QtCore.QRect(20, 20, 150, 23))
        self.lblTypeIso.setText("Tipo de Isolação:")

        self.cmbTypeIso = QtGui.QComboBox(self.centralwidget)
        self.cmbTypeIso.setGeometry(QtCore.QRect(180, 20, 290, 23))
        ItemsTypeIso = ["", "PVC até 300mm²", "PVC Maior que 300mm²", "EPR", "XLPE"]
        self.cmbTypeIso.addItems(ItemsTypeIso)

        self.lblRefMet = QtGui.QLabel(self.centralwidget)
        self.lblRefMet.setGeometry(QtCore.QRect(20, 60, 150, 23))
        self.lblRefMet.setText("Método de Referência:")

        self.cmbRefMet = QtGui.QComboBox(self.centralwidget)
        self.cmbRefMet.setGeometry(QtCore.QRect(180, 60, 290, 23))
        ItemsRefMet = ["", "A1: Condutores Isolados em Eletroduto de Seção Circular Embutido em Parede Termicamente Isolante",
                       "A2: Cabo Multipolar em Eletroduto de Seção Circular Embutido em Parede Termicamente Isolante",
                       "B1: Condutores Isolados em Eletroduto de Seção Circular Sobre Parede de Madeira",
                       "B2: Cabo Multipolar em Eletroduto de Seção Circular Sobre Parede de Madeira",
                       "C: Cabos Unipolares ou Cabo Multipolar Sobre Parede de Madeira",
                       "D: Cabos Multipolar em Eletroduto Enterrado no Solo",
                       "E: Cabo Multipolar ao Ar Livre",
                       "F: Cabos Unipolares Justapostos ao Ar Livre",
                       "G: Cabos Unipolares Espaçados ao Ar Livre"]
        self.cmbRefMet.addItems(ItemsRefMet)
        self.cmbRefMet.activated.connect(self.ItemsFreeCond)

        self.lblNomCur = QtGui.QLabel(self.centralwidget)
        self.lblNomCur.setGeometry(QtCore.QRect(20, 100, 150, 23))
        self.lblNomCur.setText("Corrente Nominal:")

        self.lneNomCur = QtGui.QLineEdit(self.centralwidget)
        self.lneNomCur.setGeometry(QtCore.QRect(180, 100, 80, 23))
        
        self.btnCalCur = QtGui.QPushButton(self.centralwidget)
        self.btnCalCur.setGeometry(QtCore.QRect(270, 100, 70, 23))
        self.btnCalCur.setText("Calcular")
        self.btnCalCur.clicked.connect(self.CalcCurrent)
        
        self.btnFactor = QtGui.QPushButton(self.centralwidget)
        self.btnFactor.setGeometry(QtCore.QRect(350, 100, 120, 23))
        self.btnFactor.setText("Fatores de Correção")
        #self.btnFatores.clicked.connect()

        self.lblFreeCond = QtGui.QLabel(self.centralwidget)
        self.lblFreeCond.setGeometry(QtCore.QRect(20, 140, 150, 23))
        self.lblFreeCond.setText("Esquema de Condutores Vivos:")

        self.cmbFreeCond = QtGui.QComboBox(self.centralwidget)
        self.cmbFreeCond.setGeometry(QtCore.QRect(180, 140, 290, 23))

        self.btnCalcSec = QtGui.QPushButton(self.centralwidget)
        self.btnCalcSec.setGeometry(QtCore.QRect(290, 175, 75, 23))
        self.btnCalcSec.setText("Calcular")
        self.btnCalcSec.clicked.connect(self.CalCurrCap)

        self.lblCondSec = QtGui.QLabel(self.centralwidget)
        self.lblCondSec.setGeometry(QtCore.QRect(20, 210, 150, 23))
        self.lblCondSec.setText("Seção Condutor:")

        self.lneCondSec = QtGui.QLineEdit(self.centralwidget)
        self.lneCondSec.setGeometry(QtCore.QRect(180, 210, 290, 23))
        self.lneCondSec.setReadOnly(True)

        self.lblNeutroSec = QtGui.QLabel(self.centralwidget)
        self.lblNeutroSec.setGeometry(QtCore.QRect(20, 240, 150, 23))
        self.lblNeutroSec.setText("Seção Neutro:")

        self.lneNeutroSec = QtGui.QLineEdit(self.centralwidget)
        self.lneNeutroSec.setGeometry(QtCore.QRect(180, 240, 290, 23))
        self.lneNeutroSec.setReadOnly(True)

        self.lblProtSec = QtGui.QLabel(self.centralwidget)
        self.lblProtSec.setGeometry(QtCore.QRect(20, 270, 150, 23))
        self.lblProtSec.setText("Seção Proteção:")

        self.lneProtSec = QtGui.QLineEdit(self.centralwidget)
        self.lneProtSec.setGeometry(QtCore.QRect(180, 270, 290, 23))
        self.lneProtSec.setReadOnly(True)
        
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 300, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ItemsFreeCond(self, MainWindow):
        self.cmbFreeCond.clear()
        refMet = self.cmbRefMet.currentIndex()
        if refMet == 0:
            ItemsFreeCond = []
        elif refMet == 8:
            ItemsFreeCond = ["", "2 Condutores Carregados Justapostos", "3 Condutores Carregados Trifólio", "3 Condutores Carregados Justapostos"]
        elif refMet == 9:
            ItemsFreeCond = ["", "3 Condutores Carregados na Horizontal", "3 Condutores Carregados na Vertical"]
        else:
            ItemsFreeCond = ["", "Monofásico a Dois Condutores", "Monofásico a Três Condutores",
                              "Duas Fases Sem Neutro", "Duas Fases Com Neutro",
                              "Trifásico Sem Neutro", "Trifásico Com Neutro"]            
        self.cmbFreeCond.addItems(ItemsFreeCond)

    def CalCurrCap(self):
        typeIso = self.cmbTypeIso.currentIndex()
        refMet = self.cmbRefMet.currentIndex()
        numCondCharge = self.cmbFreeCond.currentIndex()
        
        if typeIso == 0 or refMet == 0 or numCondCharge == 0:
            condSec = "Erro"
        else:
            nomCurr = float(self.lneNomCur.text())
            if typeIso == 1 or typeIso == 2:
                condSec = tab36e38(refMet, numCondCharge, nomCurr)
            elif typeIso == 3 or typeIso == 4:
                condSec = tab37e39(refMet, numCondCharge, nomCurr)
            neutSec = tabNeutro(condSec)
            protSec = tabProt(condSec)
        self.lneCondSec.setText("{} mm²".format(str(condSec)))
        self.lneNeutroSec.setText("{} mm²".format(str(neutSec)))
        self.lneProtSec.setText("{} mm²".format(str(protSec)))

    def CalcCurrent(self):
        self.window = QtGui.QDialog()
        self.ui = Ui_CalcCurrent()
        self.ui._init_(self.window)
        self.window.show()
##        if QtCore.SIGNAL == "accepted()":
##            self.lneNomCur.setText(lneCurrent.text())
##        else:
##            print("não")


############################Função Cálculo de Corrente Nominal#################
class Ui_CalcCurrent(object):
    def _init_(self, Dialog):
        Dialog.resize(370, 291)
        self.lblCircType = QtGui.QLabel(Dialog)
        self.lblCircType.setGeometry(QtCore.QRect(30, 20, 111, 20))
        self.lblCircType.setText("Tipo de Circuito:")
        
        self.cmbCircType = QtGui.QComboBox(Dialog)
        self.cmbCircType.setGeometry(QtCore.QRect(120, 20, 191, 20))
        itemsTipCirc = ["", "Monofásico", "Trifásico Equilibrado", "Trifásico Desequilibrado"]
        self.cmbCircType.addItems(itemsTipCirc)
        
        self.lblPower = QtGui.QLabel(Dialog)
        self.lblPower.setGeometry(QtCore.QRect(30, 60, 61, 20))
        self.lblPower.setText("Potência:")

        self.lnePower = QtGui.QLineEdit(Dialog)
        self.lnePower.setGeometry(QtCore.QRect(120, 60, 191, 20))
        
        self.lblVoltage = QtGui.QLabel(Dialog)
        self.lblVoltage.setGeometry(QtCore.QRect(30, 90, 46, 20))
        self.lblVoltage.setText("Tensão:")
                
        self.lneVoltage = QtGui.QLineEdit(Dialog)
        self.lneVoltage.setGeometry(QtCore.QRect(120, 90, 191, 20))

        self.lblFactor = QtGui.QLabel(Dialog)
        self.lblFactor.setGeometry(QtCore.QRect(30, 120, 91, 20))
        self.lblFactor.setText("Fator de Potência:")
        
        self.lneFactor = QtGui.QLineEdit(Dialog)
        self.lneFactor.setGeometry(QtCore.QRect(120, 120, 191, 20))
                
        self.lblEffic = QtGui.QLabel(Dialog)
        self.lblEffic.setGeometry(QtCore.QRect(30, 150, 91, 20))
        self.lblEffic.setText("Rendimento:")
        
        self.lneEffic = QtGui.QLineEdit(Dialog)
        self.lneEffic.setGeometry(QtCore.QRect(120, 150, 191, 20))

        self.btnCalculate = QtGui.QPushButton(Dialog)
        self.btnCalculate.setGeometry(QtCore.QRect(170, 180, 75, 20))
        self.btnCalculate.setText("Calcular")
        self.btnCalculate.clicked.connect(self.CalcCurr)
        
        self.lblCurrent = QtGui.QLabel(Dialog)
        self.lblCurrent.setGeometry(QtCore.QRect(30, 210, 91, 20))
        self.lblCurrent.setText("Corrente")
        
        self.lneCurrent = QtGui.QLineEdit(Dialog)
        self.lneCurrent.setGeometry(QtCore.QRect(120, 210, 191, 20))

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def CalcCurr(self):
        circType = self.cmbCircType.currentIndex()
        if circType == 0:
            current = "Erro"
        else:
            power = float(self.lnePower.text())
            voltage = float(self.lneVoltage.text())
            factor = float(self.lneFactor.text())
            effic = float(self.lneEffic.text())
            current = calcCur(circType, power, voltage, factor, effic)
        self.lneCurrent.setText(str(current))

    def accepted(self):
        current = float(self.lneCurrent.text())
        print(current)
        



############################Queda de Tensão######################################
class Ui_DropVolt(object):
    def _init_(self, Dialog):
        Dialog.resize(330, 330)
        Dialog.setWindowTitle("Queda de Tensão")

        self.lblTypeSis = QtGui.QLabel(Dialog)
        self.lblTypeSis.setGeometry(QtCore.QRect(30, 20, 110, 20))
        self.lblTypeSis.setText("Tipo de Sistema:")
        
        self.cmbTypeSis = QtGui.QComboBox(Dialog)
        self.cmbTypeSis.setGeometry(QtCore.QRect(140, 20, 150, 20))
        itemsTypeSis = ["", "Monofásico", "Trifásico"]
        self.cmbTypeSis.addItems(itemsTypeSis)

        self.lblVoltage = QtGui.QLabel(Dialog)
        self.lblVoltage.setGeometry(QtCore.QRect(30, 50, 110, 20))
        self.lblVoltage.setText("Tensao (V):")
        
        self.lneVoltage = QtGui.QLineEdit(Dialog)
        self.lneVoltage.setGeometry(QtCore.QRect(140, 50, 150, 20))
        
        self.lblCur = QtGui.QLabel(Dialog)
        self.lblCur.setGeometry(QtCore.QRect(30, 80, 110, 20))
        self.lblCur.setText("Corrente (A):")

        self.lneCur = QtGui.QLineEdit(Dialog)
        self.lneCur.setGeometry(QtCore.QRect(140, 80, 150, 20))
        
        self.lblDist = QtGui.QLabel(Dialog)
        self.lblDist.setGeometry(QtCore.QRect(30, 110, 110, 20))
        self.lblDist.setText("Distância (m):")
                
        self.lneDist = QtGui.QLineEdit(Dialog)
        self.lneDist.setGeometry(QtCore.QRect(140, 110, 150, 20))

        self.lblDrop = QtGui.QLabel(Dialog)
        self.lblDrop.setGeometry(QtCore.QRect(30, 140, 110, 20))
        self.lblDrop.setText("Queda de Tensão (%):")
        
        self.lneDrop = QtGui.QLineEdit(Dialog)
        self.lneDrop.setGeometry(QtCore.QRect(140, 140, 150, 20))

        self.btnCalc = QtGui.QPushButton(Dialog)
        self.btnCalc.setGeometry(QtCore.QRect(180, 170, 75, 20))
        self.btnCalc.setText("Calcular")
        self.btnCalc.clicked.connect(self.CalcSecao)
                
        self.lblCondSec = QtGui.QLabel(Dialog)
        self.lblCondSec.setGeometry(QtCore.QRect(30, 200, 110, 20))
        self.lblCondSec.setText("Seção Condutor:")
        
        self.lneCondSec = QtGui.QLineEdit(Dialog)
        self.lneCondSec.setGeometry(QtCore.QRect(140, 200, 150, 20))

        self.lblNeutroSec = QtGui.QLabel(Dialog)
        self.lblNeutroSec.setGeometry(QtCore.QRect(30, 230, 110, 20))
        self.lblNeutroSec.setText("Seção Neutro:")
        
        self.lneNeutroSec = QtGui.QLineEdit(Dialog)
        self.lneNeutroSec.setGeometry(QtCore.QRect(140, 230, 150, 20))
        
        self.lblProtSec = QtGui.QLabel(Dialog)
        self.lblProtSec.setGeometry(QtCore.QRect(30, 260, 110, 20))
        self.lblProtSec.setText("Seção Proteção:")
        
        self.lneProtSec = QtGui.QLineEdit(Dialog)
        self.lneProtSec.setGeometry(QtCore.QRect(140, 260, 150, 20))
        
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-50, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def CalcSecao(self):
        typeSis = self.cmbTypeSis.currentIndex()        
        if typeSis == 0:
            condSec = "Erro"
        else:
            condSec = calcDrop(typeSis, float(self.lneCur.text()),
                       float(self.lneDist.text()), float(self.lneDrop.text()),
                       float(self.lneVoltage.text()))
            neutSec = tabNeutro(condSec)
            protSec = tabProt(condSec)
        self.lneCondSec.setText("{} mm²".format(str(condSec),str(protSec)))
        self.lneNeutroSec.setText("{} mm²".format(str(neutSec)))
        self.lneProtSec.setText("{} mm²".format(str(protSec)))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_CondSec()
    ui._init_(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
