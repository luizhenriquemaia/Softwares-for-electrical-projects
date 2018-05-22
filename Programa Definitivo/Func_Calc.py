from math import sqrt

def calcTugs(period, environment):
    if environment == 0:
        minTugs = "selecione um ambiente"
    else:   
        if environment == 1:
            minTugs = float(period)/5
        if environment == 2:
            minTugs = float(period)/3.5
        if environment == 3:
            minTugs = 1
        if environment == 4:
            minTugs = 1
    minTugs = round(minTugs, 2)
    return(minTugs)

def calcAir(expose, people, devices, area):
    if expose == True:
        btuM = 800
    else:
        btuM = 600
    if people <= 2:
        btuP = 0
    else:
        btuP = (people - 2) * btuM
    air = round((btuM * area) + btuP + (devices * btuM), 2)
    return(air)

def calcCur(circType, power, voltage, factor, efficiency):
    if circType == 1:
        current = power/(voltage*factor*efficiency)
    elif circType == 2:
        current = power/(sqrt(3)*voltage*factor*efficiency)
    else:
        circType = power/(3*Tensao*factor*efficiency)
    current = round(current,2)
    return(current)

def calcDrop(typeSis, current, distance, drop, voltage):
    if typeSis == 1:
        condSec = (200*(1/56)*current*distance)/(drop*voltage)
    elif typeSis == 2:
        condSec = (100*sqrt(3)*(1/56)*current*distance)/(drop*voltage)
    condSec = round(condSec,2)
    return(condSec)
