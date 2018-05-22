import sys
from Func_Calc import calcAir, calcTugs
from PyQt4 import QtCore, QtGui
from Sec_Cond import Ui_CondSec
from Tabelas import tab33, tab35, tab32
from math import pi


class Ui_Eletric(object):
    def _init_(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 242)
        MainWindow.setWindowTitle("Projetos Elétricos")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.butAir = QtGui.QPushButton(self.centralwidget)
        self.butAir.setGeometry(QtCore.QRect(30, 32, 201, 31))
        self.butAir.setObjectName("butAir")
        self.butAir.setText("Cálculo Potência Ar Condicionado")
        self.butAir.clicked.connect(self.openAir)

        self.butTugs = QtGui.QPushButton(self.centralwidget)
        self.butTugs.setGeometry(QtCore.QRect(30, 80, 201, 31))
        self.butTugs.setObjectName("butTugs")
        self.butTugs.setText("Cálculo Quantidade Mínima TUGs")
        self.butTugs.clicked.connect(self.openTugs)

        self.butCondSec = QtGui.QPushButton(self.centralwidget)
        self.butCondSec.setGeometry(QtCore.QRect(30, 130, 201, 31))
        self.butCondSec.setObjectName("butCondSec")
        self.butCondSec.setText("Cálculo Seção de Condutores")
        self.butCondSec.clicked.connect(self.openCondSec)

        self.butEleSec = QtGui.QPushButton(self.centralwidget)
        self.butEleSec.setGeometry(QtCore.QRect(30, 180, 201, 31))
        self.butEleSec.setObjectName("butEleSec")
        self.butEleSec.setText("Cálculo Seção de Eletrodutos e Calhas")
        self.butEleSec.clicked.connect(self.openEleSec)

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openAir(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_Air()
        self.ui._init_(self.window)
        self.window.show()

    def openTugs(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_Tugs()
        self.ui._init_(self.window)
        self.window.show()

    def openCondSec(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_CondSec()
        self.ui._init_(self.window)
        self.window.show()

    def openEleSec(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_SecEle()
        self.ui._init_(self.window)
        self.window.show()
        

class Ui_Air(object):
    def _init_(self, MainWindow):
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
        
        self.lblPeople = QtGui.QLabel(self.centralwidget)
        self.lblPeople.setGeometry(QtCore.QRect(20, 70, 141, 16))
        self.lblPeople.setObjectName("lblPeople")
        self.lblPeople.setText("Pessoas no Ambiente:")
                
        self.lnePeople = QtGui.QLineEdit(self.centralwidget)
        self.lnePeople.setGeometry(QtCore.QRect(160, 70, 110, 20))
        self.lnePeople.setObjectName("lnePeople")
        
        self.lblDevices = QtGui.QLabel(self.centralwidget)
        self.lblDevices.setGeometry(QtCore.QRect(20, 100, 141, 16))
        self.lblDevices.setObjectName("lblDevices")
        self.lblDevices.setText("Aparelhos Fontes de Calor:")
                
        self.lneDevices = QtGui.QLineEdit(self.centralwidget)
        self.lneDevices.setGeometry(QtCore.QRect(160, 100, 110, 20))
        self.lneDevices.setObjectName("lneDevices")

        self.btnCalc = QtGui.QPushButton(self.centralwidget)
        self.btnCalc.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.btnCalc.setObjectName("btnCalc")
        self.btnCalc.setText("Calcular")
        self.btnCalc.clicked.connect(self.CalcAr)
        
        self.lblAir = QtGui.QLabel(self.centralwidget)
        self.lblAir.setGeometry(QtCore.QRect(20, 160, 141, 16))
        self.lblAir.setObjectName("lblAir")
        self.lblAir.setText("Potência Ar Condicionado:")
                
        self.lneAirB = QtGui.QLineEdit(self.centralwidget)
        self.lneAirB.setGeometry(QtCore.QRect(160, 160, 110, 20))
        self.lneAirB.setObjectName("lneAirB")

        self.lblEqual = QtGui.QLabel(self.centralwidget)
        self.lblEqual.setGeometry(QtCore.QRect(210, 180, 91, 16))
        self.lblEqual.setObjectName("lblEqual")
        self.lblEqual.setText("=")
                
        self.lneAirW = QtGui.QLineEdit(self.centralwidget)
        self.lneAirW.setGeometry(QtCore.QRect(160, 200, 110, 20))
        self.lneAirW.setObjectName("lneAirW")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def CalcAr(self):
        expose = self.rbnExpo.isChecked()
        people = int(self.lnePeople.text())
        devices = int(self.lneDevices.text())
        area = float(self.lneArea.text())
        
        airb = calcAir(expose, people, devices, area)
        airw = round(((airb/3.412141633)/1000),2)
    
        self.lneAirB.setText(str(airb)+ " BTUS")
        self.lneAirW.setText(str(airw)+ " kW")


class Ui_Tugs(object):
    def _init_(self, MainWindow):
        MainWindow.setFixedSize(325, 180)
        MainWindow.setWindowTitle("Cálculo de TUGs")
        self.centralwidget = QtGui.QWidget(MainWindow)
        
        self.lblEnv = QtGui.QLabel(self.centralwidget)
        self.lblEnv.setGeometry(QtCore.QRect(20, 20, 55, 20))
        self.lblEnv.setText("Ambiente:")

        self.cmbEnv = QtGui.QComboBox(self.centralwidget)
        self.cmbEnv.setGeometry(QtCore.QRect(80, 20, 225, 20))
        ItemsEnv = ["", "Cômodo Comum", "Cozinha, Copa, Área de Serviço",
                    "Subsolo, Varanda, Garagem, Sótãos", "Banheiro"]
        self.cmbEnv.addItems(ItemsEnv)

        self.lblDim = QtGui.QLabel(self.centralwidget)
        self.lblDim.setGeometry(QtCore.QRect(20, 50, 55, 20))
        self.lblDim.setText("Dimensões:")

        self.lneWidth = QtGui.QLineEdit(self.centralwidget)
        self.lneWidth.setGeometry(QtCore.QRect(80, 50, 95, 20))

        self.lneLength = QtGui.QLineEdit(self.centralwidget)
        self.lneLength.setGeometry(QtCore.QRect(185, 50, 95, 20))

        self.btnPer = QtGui.QPushButton(self.centralwidget)
        self.btnPer.setGeometry(QtCore.QRect(285, 50, 20, 20))
        self.btnPer.setText("=")
        self.btnPer.clicked.connect(self.Period)

        self.lblPer = QtGui.QLabel(self.centralwidget)
        self.lblPer.setGeometry(QtCore.QRect(20, 80, 55, 20))
        self.lblPer.setText("Perímetro:")

        self.lnePer = QtGui.QLineEdit(self.centralwidget)
        self.lnePer.setGeometry(QtCore.QRect(80, 80, 225, 20))

        self.btnCalc = QtGui.QPushButton(self.centralwidget)
        self.btnCalc.setGeometry(QtCore.QRect(160, 110, 75, 20))
        self.btnCalc.setText("Calcular")
        self.btnCalc.clicked.connect(self.Calculate)
        
        self.lneTugs = QtGui.QLineEdit(self.centralwidget)
        self.lneTugs.setGeometry(QtCore.QRect(80, 140, 225, 20))

        MainWindow.setCentralWidget(self.centralwidget)

    def Period(self):
        width = self.lneWidth.text()
        length = self.lneLength.text()
        period = 2*(float(width) + float(length))
        self.lnePer.setText(str(period))
        return period

    def Calculate(self):
        period = self.lnePer.text()
        environment = self.cmbEnv.currentIndex()
        minTugs = calcTugs(period, environment)
        self.lneTugs.setText("Quantidade de TUGs = {}".format(str(minTugs)))
        

class Ui_SecEle(object):
    def _init_(self, MainWindow):
        MainWindow.setFixedSize(500, 300)
        MainWindow.setWindowTitle("Cálculo de Eletrodutos")
        self.centralwidget = QtGui.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.lblQuant = QtGui.QLabel(self.centralwidget)
        self.lblQuant.setGeometry(QtCore.QRect(45, 20, 55, 20))
        self.lblQuant.setText("Quantidade")
        
        self.lneQuant = QtGui.QLineEdit(self.centralwidget)
        self.lneQuant.setGeometry(QtCore.QRect(20, 40, 100, 20))

        self.lblSecCond = QtGui.QLabel(self.centralwidget)
        self.lblSecCond.setGeometry(QtCore.QRect(55, 60, 55, 20))
        self.lblSecCond.setText("Seção")
        
        self.lneSecCond = QtGui.QLineEdit(self.centralwidget)
        self.lneSecCond.setGeometry(QtCore.QRect(20, 80, 100, 20))

        self.lblTipoCond = QtGui.QLabel(self.centralwidget)
        self.lblTipoCond.setGeometry(QtCore.QRect(60, 100, 55, 20))
        self.lblTipoCond.setText("Tipo")

        self.cmbTipoCond = QtGui.QComboBox(self.centralwidget)
        self.cmbTipoCond.setGeometry(QtCore.QRect(20, 120, 100, 20))
        ItemsTipoCond = ["", "Condutor", "Cabo Isolado", "Cabo Unipolar"]
        self.cmbTipoCond.addItems(ItemsTipoCond)
        
        self.btnAdd = QtGui.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(45, 150, 55, 20))
        self.btnAdd.setText("Incluir")
        self.btnAdd.clicked.connect(self.AddItems)

        self.tabCond = QtGui.QTableWidget(self.centralwidget)
        self.tabCond.setGeometry(QtCore.QRect(130, 20, 350, 140))
        self.tabCond.setColumnCount(4)
        self.tabCond.setHorizontalHeaderLabels(("Quantidade;Seção(mm²);Tipo;Del").split(";"))
        self.tabCond.setRowCount(0)
        header = self.tabCond.horizontalHeader()
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        self.tabCond.cellDoubleClicked.connect(self.DelItems)

        self.btnCalc = QtGui.QPushButton(self.centralwidget)
        self.btnCalc.setGeometry(QtCore.QRect(250, 170, 70, 20))
        self.btnCalc.setText("Calcular")
        self.btnCalc.clicked.connect(self.CalcElet)

        self.lblElePVC = QtGui.QLabel(self.centralwidget)
        self.lblElePVC.setGeometry(QtCore.QRect(20, 200, 90, 20))
        self.lblElePVC.setText("Eletroduto PVC")

        self.lblElePA = QtGui.QLabel(self.centralwidget)
        self.lblElePA.setGeometry(QtCore.QRect(20, 230, 20, 20))
        self.lblElePA.setText("A:")

        self.lneElePA = QtGui.QLineEdit(self.centralwidget)
        self.lneElePA.setGeometry(QtCore.QRect(50, 230, 100, 20))
        
        self.lblElePB = QtGui.QLabel(self.centralwidget)
        self.lblElePB.setGeometry(QtCore.QRect(20, 260, 20, 20))
        self.lblElePB.setText("B:")

        self.lneElePB = QtGui.QLineEdit(self.centralwidget)
        self.lneElePB.setGeometry(QtCore.QRect(50, 260, 100, 20))

        self.lblEleAco = QtGui.QLabel(self.centralwidget)
        self.lblEleAco.setGeometry(QtCore.QRect(170, 200, 90, 20))
        self.lblEleAco.setText("Eletroduto Aço")

        self.lblEleAE = QtGui.QLabel(self.centralwidget)
        self.lblEleAE.setGeometry(QtCore.QRect(170, 230, 30, 20))
        self.lblEleAE.setText("Extra:")

        self.lneEleAE = QtGui.QLineEdit(self.centralwidget)
        self.lneEleAE.setGeometry(QtCore.QRect(215, 230, 100, 20))
        
        self.lblEleAP = QtGui.QLabel(self.centralwidget)
        self.lblEleAP.setGeometry(QtCore.QRect(170, 260, 40, 20))
        self.lblEleAP.setText("Pesada:")

        self.lneEleAP = QtGui.QLineEdit(self.centralwidget)
        self.lneEleAP.setGeometry(QtCore.QRect(215, 260, 100, 20))
        
        self.lblEleCal = QtGui.QLabel(self.centralwidget)
        self.lblEleCal.setGeometry(QtCore.QRect(330, 200, 90, 20))
        self.lblEleCal.setText("Eletro Calhas")

        self.lneEleCal = QtGui.QLineEdit(self.centralwidget)
        self.lneEleCal.setGeometry(QtCore.QRect(330, 230, 100, 20))


    def AddItems(self):
        quant = QtGui.QTableWidgetItem(self.lneQuant.text())
        sec = QtGui.QTableWidgetItem(self.lneSecCond.text())
        tipo = QtGui.QTableWidgetItem(self.cmbTipoCond.currentText())
        delete = QtGui.QTableWidgetItem("-")
        rowPosition = self.tabCond.rowCount()
        
        self.tabCond.insertRow(rowPosition)
        self.tabCond.setItem(rowPosition, 0, quant)
        self.tabCond.setItem(rowPosition, 1, sec)
        self.tabCond.setItem(rowPosition, 2, tipo)
        self.tabCond.setItem(rowPosition, 3, delete)

        quant.setTextAlignment(QtCore.Qt.AlignCenter)
        sec.setTextAlignment(QtCore.Qt.AlignCenter)
        tipo.setTextAlignment(QtCore.Qt.AlignCenter)
        delete.setTextAlignment(QtCore.Qt.AlignCenter)
        return


    def DelItems(self):
        item = self.tabCond.currentColumn()
        row = self.tabCond.currentRow()
        if item == 3:
            self.tabCond.removeRow(row)
        else:
            pass
        return


    def CalcElet(self):
        quant = []
        sec = []
        tipo = []
        diamCond = []
        secCond = []
        rows = self.tabCond.rowCount()
        #Vetores de Dados
        for i in range(0, rows):
            quant.append(int(self.tabCond.item(i, 0).text()))
            sec.append(float(self.tabCond.item(i, 1).text()))
            tipo.append(self.tabCond.item(i, 2).text())
        #Diametro Externo Condutores
        for i in range(0, len(tipo)):
            diamCond.append(tab33(tipo[i],sec[i]))
        #Seção Total Condutores
        for i in range(0, len(diamCond)):
            secCond.append((quant[i]*pi*diamCond[i]**2)/4)
        #Area dos Eletrodutos e Eletrocalhas
        secCondTot = round(sum(secCond),2)

        if sum(quant) <= 2:
            elePvcA = tab32(1, 2, secCondTot, 1)
            elePvcB = tab32(1, 2, secCondTot, 2)
            eleAcoE = tab32(2, 2, secCondTot, 1)
            eleAcoP = tab32(2, 2, secCondTot, 2)
        elif sum(quant) >= 3:
            elePvcA = tab32(1, 3, secCondTot, 1)
            elePvcB = tab32(1, 3, secCondTot, 2)
            eleAcoE = tab32(2, 3, secCondTot, 1)
            eleAcoP = tab32(2, 3, secCondTot, 2)

        self.lneElePA.setText("{} mm²".format(str(elePvcA)))
        self.lneElePB.setText("{} mm²".format(str(elePvcB)))
        self.lneEleAE.setText("{} mm²".format(str(eleAcoE)))
        self.lneEleAP.setText("{} mm²".format(str(eleAcoP)))
        self.lneEleCal.setText("{} mm³".format(str(tab35(secCondTot))))
        
        print("Quantidade: {}\nSeção: {}\nTipo: {}".format(quant, sec, tipo))
        print("Diametros: {}".format(diamCond))
        print("Seção: {}".format(secCond))
        print("Seção Total: {}".format(secCondTot))        
        return


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Eletric()
    ui._init_(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
