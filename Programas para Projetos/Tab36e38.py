def tab36e38(MetRef, CondCar, CorNom):
    
    if MetRef == 1:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 7:
                SecNom = 0.5
            elif CorNom > 7 and CorNom <= 9:
                SecNom = 0.75
            elif CorNom > 9 and CorNom <= 11:
                SecNom = 1
            elif CorNom > 11 and CorNom <= 14.5:
                SecNom = 1.5
            elif CorNom > 14.5 and CorNom <= 19.5:
                SecNom = 2.5
            elif CorNom > 19.5 and CorNom <= 26:
                SecNom = 4
            elif CorNom > 26 and CorNom <= 34:
                SecNom = 6
            elif CorNom > 34 and CorNom <= 46:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"
                
        else:
            if CorNom <= 7:
                SecNom = 0.5
            elif CorNom > 7 and CorNom <= 9:
                SecNom = 0.75
            elif CorNom > 9 and CorNom <= 10:
                SecNom = 1
            elif CorNom > 11 and CorNom <= 13.5:
                SecNom = 1.5
            elif CorNom > 13.5 and CorNom <= 18:
                SecNom = 2.5
            elif CorNom > 18 and CorNom <= 24:
                SecNom = 4
            elif CorNom > 24 and CorNom <= 31:
                SecNom = 6
            elif CorNom > 31 and CorNom <= 42:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"

    elif MetRef == 2:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 7:
                SecNom = 0.5
            elif CorNom > 7 and CorNom <= 9:
                SecNom = 0.75
            elif CorNom > 9 and CorNom <= 11:
                SecNom = 1
            elif CorNom > 11 and CorNom <= 14:
                SecNom = 1.5
            elif CorNom > 14 and CorNom <= 18.5:
                SecNom = 2.5
            elif CorNom > 18.5 and CorNom <= 25:
                SecNom = 4
            elif CorNom > 25 and CorNom <= 32:
                SecNom = 6
            elif Nom > 32 and CorNom <= 43:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"

        else:
            if CorNom <= 7:
                SecNom = 0.5
            elif CorNom > 7 and CorNom <= 9:
                SecNom = 0.75
            elif CorNom > 9 and CorNom <= 10:
                SecNom = 1
            elif CorNom > 10 and CorNom <= 13:
                SecNom = 1.5
            elif CorNom > 13 and CorNom <= 17.5:
                SecNom = 2.5
            elif CorNom > 17.5 and CorNom <= 23:
                SecNom = 4
            elif CorNom > 23 and CorNom <= 29:
                SecNom = 6
            elif CorNom > 29 and CorNom <= 39:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"

    elif MetRef == 3:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 9:
                SecNom = 0.5
            elif CorNom > 9 and CorNom <= 11:
                SecNom = 0.75
            elif CorNom > 11 and CorNom <= 14:
                SecNom = 1
            elif CorNom > 14 and CorNom <= 17.5:
                SecNom = 1.5
            elif CorNom > 17.5 and CorNom <= 24:
                SecNom = 2.5
            elif CorNom > 24 and CorNom <= 32:
                SecNom = 4
            elif CorNom > 32 and CorNom <= 41:
                SecNom = 6
            elif CorNom > 41 and CorNom <= 57:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"
                
        else:
            if CorNom <= 8:
                SecNom = 0.5
            elif CorNom > 8 and CorNom <= 10:
                SecNom = 0.75
            elif CorNom > 10 and CorNom <= 12:
                SecNom = 1
            elif CorNom > 12 and CorNom <= 15.5:
                SecNom = 1.5
            elif CorNom > 15.5 and CorNom <= 21:
                SecNom = 2.5
            elif CorNom > 21 and CorNom <= 28:
                SecNom = 4
            elif CorNom > 28 and CorNom <= 36:
                SecNom = 6
            elif CorNom > 36 and CorNom <= 50:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"

    elif MetRef == 4:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 9:
                SecNom = 0.5
            elif CorNom > 9 and CorNom <= 11:
                SecNom = 0.75
            elif CorNom > 11 and CorNom <= 13:
                SecNom = 1
            elif CorNom > 13 and CorNom <= 16.5:
                SecNom = 1.5
            elif CorNom > 16.5 and CorNom <= 23:
                SecNom = 2.5
            elif CorNom > 23 and CorNom <= 30:
                SecNom = 4
            elif CorNom > 30 and CorNom <= 38:
                SecNom = 6
            elif CorNom > 38 and CorNom <= 52:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"
                
        else:
            if CorNom <= 8:
                SecNom = 0.5
            elif CorNom > 8 and CorNom <= 10:
                SecNom = 0.75
            elif CorNom > 10 and CorNom <= 12:
                SecNom = 1
            elif CorNom > 12 and CorNom <= 15:
                SecNom = 1.5
            elif CorNom > 15 and CorNom <= 20:
                SecNom = 2.5
            elif CorNom > 20 and CorNom <= 27:
                SecNom = 4
            elif CorNom > 27 and CorNom <= 34:
                SecNom = 6
            elif CorNom > 34 and CorNom <= 46:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"

    elif MetRef == 5:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 10:
                SecNom = 0.5
            elif CorNom > 10 and CorNom <= 13:
                SecNom = 0.75
            elif CorNom > 13 and CorNom <= 15:
                SecNom = 1
            elif CorNom > 15 and CorNom <= 19.5:
                SecNom = 1.5
            elif CorNom > 19.5 and CorNom <= 27:
                SecNom = 2.5
            elif CorNom > 27 and CorNom <= 36:
                SecNom = 4
            elif CorNom > 36 and CorNom <= 46:
                SecNom = 6
            elif CorNom > 46 and CorNom <= 63:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"
                
        else:
            if CorNom <= 9:
                SecNom = 0.5
            elif CorNom > 9 and CorNom <= 11:
                SecNom = 0.75
            elif CorNom > 11 and CorNom <= 14:
                SecNom = 1
            elif CorNom > 14 and CorNom <= 17.5:
                SecNom = 1.5
            elif CorNom > 17.5 and CorNom <= 24:
                SecNom = 2.5
            elif CorNom > 24 and CorNom <= 32:
                SecNom = 4
            elif CorNom > 32 and CorNom <= 41:
                SecNom = 6
            elif CorNom > 41 and CorNom <= 57:
                SecNom = 10

    elif MetRef == 6:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 12:
                SecNom = 0.5
            elif CorNom > 12 and CorNom <= 15:
                SecNom = 0.75
            elif CorNom > 15 and CorNom <= 18:
                SecNom = 1
            elif CorNom > 18 and CorNom <= 22:
                SecNom = 1.5
            elif CorNom > 22 and CorNom <= 29:
                SecNom = 2.5
            elif CorNom > 29 and CorNom <= 38:
                SecNom = 4
            elif CorNom > 38 and CorNom <= 47:
                SecNom = 6
            elif CorNom > 47 and CorNom <= 63:
                SecNom = 10
                
        else:
            if CorNom <= 10:
                SecNom = 0.5
            elif CorNom > 10 and CorNom <= 12:
                SecNom = 0.75
            elif CorNom > 12 and CorNom <= 15:
                SecNom = 1
            elif CorNom > 15 and CorNom <= 18:
                SecNom = 1.5
            elif CorNom > 18 and CorNom <= 24:
                SecNom = 2.5
            elif CorNom > 24 and CorNom <= 31:
                SecNom = 4
            elif CorNom > 31 and CorNom <= 39:
                SecNom = 6
            elif CorNom > 39 and CorNom <= 52:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"

    elif MetRef == 7:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 11:
                SecNom = 0.5
            elif CorNom > 11 and CorNom <= 14:
                SecNom = 0.75
            elif CorNom > 14 and CorNom <= 17:
                SecNom = 1
            elif CorNom > 17 and CorNom <= 22:
                SecNom = 1.5
            elif CorNom > 22 and CorNom <= 30:
                SecNom = 2.5
            elif CorNom > 30 and CorNom <= 40:
                SecNom = 4
            elif CorNom > 40 and CorNom <= 51:
                SecNom = 6
            elif CorNom > 51 and CorNom <= 70:
                SecNom = 10
                
        else:
            if CorNom <= 9:
                SecNom = 0.5
            elif CorNom > 9 and CorNom <= 12:
                SecNom = 0.75
            elif CorNom > 12 and CorNom <= 14:
                SecNom = 1
            elif CorNom > 14 and CorNom <= 18.5:
                SecNom = 1.5
            elif CorNom > 18.5 and CorNom <= 25:
                SecNom = 2.5
            elif CorNom > 25 and CorNom <= 34:
                SecNom = 4
            elif CorNom > 34 and CorNom <= 43:
                SecNom = 6
            elif CorNom > 43 and CorNom <= 60:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"

    elif MetRef == 8:
        if CondCar == 1:
            if CorNom <= 11:
                SecNom = 0.5
            elif CorNom > 11 and CorNom <= 14:
                SecNom = 0.75
            elif CorNom > 14 and CorNom <= 17:
                SecNom = 1
            elif CorNom > 17 and CorNom <= 22:
                SecNom = 1.5
            elif CorNom > 22 and CorNom <= 31:
                SecNom = 2.5
            elif CorNom > 31 and CorNom <= 41:
                SecNom = 4
            elif CorNom > 41 and CorNom <= 53:
                SecNom = 6
            elif CorNom > 53 and CorNom <= 73:
                SecNom = 10
                
        elif CondCar == 2:
            if CorNom <= 8:
                SecNom = 0.5
            elif CorNom > 8 and CorNom <= 11:
                SecNom = 0.75
            elif CorNom > 11 and CorNom <= 13:
                SecNom = 1
            elif CorNom > 13 and CorNom <= 17:
                SecNom = 1.5
            elif CorNom > 17 and CorNom <= 24:
                SecNom = 2.5
            elif CorNom > 24 and CorNom <= 33:
                SecNom = 4
            elif CorNom > 33 and CorNom <= 43:
                SecNom = 6
            elif CorNom > 43 and CorNom <= 60:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"
                    
        elif CondCar == 3:
            if CorNom <= 9:
                SecNom = 0.5
            elif CorNom > 9 and CorNom <= 11:
                SecNom = 0.75
            elif CorNom > 11 and CorNom <= 14:
                SecNom = 1
            elif CorNom > 14 and CorNom <= 18:
                SecNom = 1.5
            elif CorNom > 18 and CorNom <= 25:
                SecNom = 2.5
            elif CorNom > 25 and CorNom <= 34:
                SecNom = 4
            elif CorNom > 34 and CorNom <= 45:
                SecNom = 6
            elif CorNom > 45 and CorNom <= 63:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"
                
    elif MetRef == 9:
        if CondCar == 1:
            if CorNom <= 12:
                SecNom = 0.5
            elif CorNom > 12 and CorNom <= 16:
                SecNom = 0.75
            elif CorNom > 16 and CorNom <= 19:
                SecNom = 1
            elif CorNom > 19 and CorNom <= 24:
                SecNom = 1.5
            elif CorNom > 24 and CorNom <= 34:
                SecNom = 2.5
            elif CorNom > 34 and CorNom <= 45:
                SecNom = 4
            elif CorNom > 45 and CorNom <= 59:
                SecNom = 6
            elif CorNom > 59 and CorNom <= 81:
                SecNom = 10
                
        elif CondCar == 2:
            if CorNom <= 10:
                SecNom = 0.5
            elif CorNom > 10 and CorNom <= 13:
                SecNom = 0.75
            elif CorNom > 13 and CorNom <= 16:
                SecNom = 1
            elif CorNom > 16 and CorNom <= 21:
                SecNom = 1.5
            elif CorNom > 21 and CorNom <= 29:
                SecNom = 2.5
            elif CorNom > 29 and CorNom <= 39:
                SecNom = 4
            elif CorNom > 39 and CorNom <= 51:
                SecNom = 6
            elif CorNom > 51 and CorNom <= 71:
                SecNom = 10
            else:
                SecNom = "Seção Nominal Não Cadastrada"
                
    return(SecNom)
