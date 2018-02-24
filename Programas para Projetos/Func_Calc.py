def calculoTom(periodo, ambiente):

    if ambiente == 0:
        minTom = "selecione um ambiente"

    else:   
        if ambiente == 1:
            minTom = float(periodo)/5

        if ambiente == 2:
            minTom = float(periodo)/3.5

        if ambiente == 3:
            minTom = 1

        if ambiente == 4:
            minTom = 1

    minTom = round(minTom, 2)
            
    return(minTom)


def calculoAr(exposicao, pessoas, aparelhos, area):
    if exposicao == True:
        btuM = 800
    else:
        btuM = 600

    if pessoas <= 2:
        btuP = 0
    else:
        btuP = (pessoas - 2) * btuM

    ar = round((btuM * area) + btuP + (aparelhos * btuM), 2)

    return(ar)
