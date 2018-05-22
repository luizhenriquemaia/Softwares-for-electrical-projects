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
            elif CorNom > 46 and CorNom <= 61:
                SecNom = 16
            elif CorNom > 61 and CorNom <= 80:
                SecNom = 25
            elif CorNom > 80 and CorNom <= 99:
                SecNom = 35
            elif CorNom > 99 and CorNom <= 119:
                SecNom = 50
            elif CorNom > 119 and CorNom <= 151:
                SecNom = 70
            elif CorNom > 151 and CorNom <= 182:
                SecNom = 95
            elif CorNom > 182 and CorNom <= 210:
                SecNom = 120
            elif CorNom > 210 and CorNom <= 240:
                SecNom = 150
            elif CorNom > 240 and CorNom <= 273:
                SecNom = 185
            elif CorNom > 273 and CorNom <= 321:
                SecNom = 240
            elif CorNom > 312 and CorNom <= 367:
                SecNom = 300
            elif CorNom > 367 and CorNom <= 438:
                SecNom = 400
            elif CorNom > 438 and CorNom <= 502:
                SecNom = 500
            elif CorNom > 502 and CorNom <= 578:
                SecNom = 630
            elif CorNom > 578 and CorNom <= 669:
                SecNom = 800
            elif CorNom > 669 and CorNom <= 767:
                SecNom = 1000
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
            elif CorNom > 42 and CorNom <= 56:
                SecNom = 16
            elif CorNom > 56 and CorNom <= 73:
                SecNom = 25
            elif CorNom > 73 and CorNom <= 89:
                SecNom = 35
            elif CorNom > 89 and CorNom <= 108:
                SecNom = 50
            elif CorNom > 108 and CorNom <= 136:
                SecNom = 70
            elif CorNom > 136 and CorNom <= 164:
                SecNom = 95
            elif CorNom > 164 and CorNom <= 188:
                SecNom = 120
            elif CorNom > 188 and CorNom <= 216:
                SecNom = 150
            elif CorNom > 216 and CorNom <= 245:
                SecNom = 185
            elif CorNom > 245 and CorNom <= 286:
                SecNom = 240
            elif CorNom > 286 and CorNom <= 328:
                SecNom = 300
            elif CorNom > 328 and CorNom <= 390:
                SecNom = 400
            elif CorNom > 390 and CorNom <= 447:
                SecNom = 500
            elif CorNom > 447 and CorNom <= 514:
                SecNom = 630
            elif CorNom > 514 and CorNom <= 593:
                SecNom = 800
            elif CorNom > 593 and CorNom <= 679:
                SecNom = 1000
            else:
                SecNom = "Seção Nominal Não Cadastrada"

                ######################################\
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
            elif CorNom > 32 and CorNom <= 43:
                SecNom = 10
            elif CorNom > 43 and CorNom <= 57:
                SecNom = 16
            elif CorNom > 57 and CorNom <= 75:
                SecNom = 25
            elif CorNom > 75 and CorNom <= 92:
                SecNom = 35
            elif CorNom > 92 and CorNom <= 110:
                SecNom = 50
            elif CorNom > 110 and CorNom <= 139:
                SecNom = 70
            elif CorNom > 139 and CorNom <= 167:
                SecNom = 95
            elif CorNom > 167 and CorNom <= 192:
                SecNom = 120
            elif CorNom > 192 and CorNom <= 219:
                SecNom = 150
            elif CorNom > 219 and CorNom <= 248:
                SecNom = 185
            elif CorNom > 248 and CorNom <= 291:
                SecNom = 240
            elif CorNom > 291 and CorNom <= 334:
                SecNom = 300
            elif CorNom > 334 and CorNom <= 398:
                SecNom = 400
            elif CorNom > 398 and CorNom <= 456:
                SecNom = 500
            elif CorNom > 456 and CorNom <= 526:
                SecNom = 630
            elif CorNom > 526 and CorNom <= 609:
                SecNom = 800
            elif CorNom > 609 and CorNom <= 698:
                SecNom = 1000
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
            elif CorNom > 39 and CorNom <= 52:
                SecNom = 16
            elif CorNom > 52 and CorNom <= 68:
                SecNom = 25
            elif CorNom > 68 and CorNom <= 83:
                SecNom = 35
            elif CorNom > 83 and CorNom <= 99:
                SecNom = 50
            elif CorNom > 99 and CorNom <= 125:
                SecNom = 70
            elif CorNom > 125 and CorNom <= 150:
                SecNom = 95
            elif CorNom > 150 and CorNom <= 172:
                SecNom = 120
            elif CorNom > 172 and CorNom <= 196:
                SecNom = 150
            elif CorNom > 196 and CorNom <= 223:
                SecNom = 185
            elif CorNom > 223 and CorNom <= 261:
                SecNom = 240
            elif CorNom > 261 and CorNom <= 298:
                SecNom = 300
            elif CorNom > 298 and CorNom <= 355:
                SecNom = 400
            elif CorNom > 355 and CorNom <= 406:
                SecNom = 500
            elif CorNom > 406 and CorNom <= 467:
                SecNom = 630
            elif CorNom > 467 and CorNom <= 540:
                SecNom = 800
            elif CorNom > 540 and CorNom <= 618:
                SecNom = 1000
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
            elif CorNom > 57 and CorNom <= 76:
                SecNom = 16
            elif CorNom > 76 and CorNom <= 101:
                SecNom = 25
            elif CorNom > 101 and CorNom <= 125:
                SecNom = 35
            elif CorNom > 125 and CorNom <= 151:
                SecNom = 50
            elif CorNom > 151 and CorNom <= 192:
                SecNom = 70
            elif CorNom > 192 and CorNom <= 232:
                SecNom = 95
            elif CorNom > 232 and CorNom <= 269:
                SecNom = 120
            elif CorNom > 269 and CorNom <= 309:
                SecNom = 150
            elif CorNom > 309 and CorNom <= 353:
                SecNom = 185
            elif CorNom > 353 and CorNom <= 415:
                SecNom = 240
            elif CorNom > 415 and CorNom <= 477:
                SecNom = 300
            elif CorNom > 477 and CorNom <= 571:
                SecNom = 400
            elif CorNom > 571 and CorNom <= 656:
                SecNom = 500
            elif CorNom > 656 and CorNom <= 758:
                SecNom = 630
            elif CorNom > 758 and CorNom <= 881:
                SecNom = 800
            elif CorNom > 881 and CorNom <= 1012:
                SecNom = 1000
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
            elif CorNom > 50 and CorNom <= 68:
                SecNom = 16
            elif CorNom > 68 and CorNom <= 89:
                SecNom = 25
            elif CorNom > 89 and CorNom <= 110:
                SecNom = 35
            elif CorNom > 110 and CorNom <= 134:
                SecNom = 50
            elif CorNom > 134 and CorNom <= 171:
                SecNom = 70
            elif CorNom > 171 and CorNom <= 207:
                SecNom = 95
            elif CorNom > 207 and CorNom <= 239:
                SecNom = 120
            elif CorNom > 239 and CorNom <= 275:
                SecNom = 150
            elif CorNom > 275 and CorNom <= 314:
                SecNom = 185
            elif CorNom > 314 and CorNom <= 370:
                SecNom = 240
            elif CorNom > 370 and CorNom <= 426:
                SecNom = 300
            elif CorNom > 426 and CorNom <= 510:
                SecNom = 400
            elif CorNom > 510 and CorNom <= 587:
                SecNom = 500
            elif CorNom > 587 and CorNom <= 678:
                SecNom = 630
            elif CorNom > 678 and CorNom <= 788:
                SecNom = 800
            elif CorNom > 788 and CorNom <= 906:
                SecNom = 1000
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
            elif CorNom > 52 and CorNom <= 69:
                SecNom = 16
            elif CorNom > 69 and CorNom <= 90:
                SecNom = 25
            elif CorNom > 90 and CorNom <= 110:
                SecNom = 35
            elif CorNom > 110 and CorNom <= 133:
                SecNom = 50
            elif CorNom > 133 and CorNom <= 168:
                SecNom = 70
            elif CorNom > 168 and CorNom <= 201:
                SecNom = 95
            elif CorNom > 201 and CorNom <= 232:
                SecNom = 120
            elif CorNom > 232 and CorNom <= 265:
                SecNom = 150
            elif CorNom > 265 and CorNom <= 300:
                SecNom = 185
            elif CorNom > 300 and CorNom <= 351:
                SecNom = 240
            elif CorNom > 351 and CorNom <= 401:
                SecNom = 300
            elif CorNom > 401 and CorNom <= 477:
                SecNom = 400
            elif CorNom > 477 and CorNom <= 545:
                SecNom = 500
            elif CorNom > 545 and CorNom <= 626:
                SecNom = 630
            elif CorNom > 626 and CorNom <= 723:
                SecNom = 800
            elif CorNom > 723 and CorNom <= 827:
                SecNom = 1000
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
            elif CorNom > 46 and CorNom <= 62:
                SecNom = 16
            elif CorNom > 62 and CorNom <= 80:
                SecNom = 25
            elif CorNom > 80 and CorNom <= 99:
                SecNom = 35
            elif CorNom > 99 and CorNom <= 118:
                SecNom = 50
            elif CorNom > 118 and CorNom <= 149:
                SecNom = 70
            elif CorNom > 149 and CorNom <= 179:
                SecNom = 95
            elif CorNom > 179 and CorNom <= 206:
                SecNom = 120
            elif CorNom > 206 and CorNom <= 236:
                SecNom = 150
            elif CorNom > 236 and CorNom <= 268:
                SecNom = 185
            elif CorNom > 268 and CorNom <= 313:
                SecNom = 240
            elif CorNom > 313 and CorNom <= 358:
                SecNom = 300
            elif CorNom > 358 and CorNom <= 425:
                SecNom = 400
            elif CorNom > 425 and CorNom <= 486:
                SecNom = 500
            elif CorNom > 486 and CorNom <= 559:
                SecNom = 630
            elif CorNom > 559 and CorNom <= 645:
                SecNom = 800
            elif CorNom > 645 and CorNom <= 738:
                SecNom = 1000
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
            elif CorNom > 63 and CorNom <= 85:
                SecNom = 16
            elif CorNom > 85 and CorNom <= 112:
                SecNom = 25
            elif CorNom > 112 and CorNom <= 138:
                SecNom = 35
            elif CorNom > 138 and CorNom <= 168:
                SecNom = 50
            elif CorNom > 168 and CorNom <= 213:
                SecNom = 70
            elif CorNom > 213 and CorNom <= 258:
                SecNom = 95
            elif CorNom > 258 and CorNom <= 299:
                SecNom = 120
            elif CorNom > 299 and CorNom <= 344:
                SecNom = 150
            elif CorNom > 344 and CorNom <= 392:
                SecNom = 185
            elif CorNom > 392 and CorNom <= 461:
                SecNom = 240
            elif CorNom > 461 and CorNom <= 530:
                SecNom = 300
            elif CorNom > 530 and CorNom <= 634:
                SecNom = 400
            elif CorNom > 634 and CorNom <= 729:
                SecNom = 500
            elif CorNom > 729 and CorNom <= 843:
                SecNom = 630
            elif CorNom > 843 and CorNom <= 978:
                SecNom = 800
            elif CorNom > 978 and CorNom <= 1125:
                SecNom = 1000
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
            elif CorNom > 57 and CorNom <= 76:
                SecNom = 16
            elif CorNom > 76 and CorNom <= 96:
                SecNom = 25
            elif CorNom > 96 and CorNom <= 119:
                SecNom = 35
            elif CorNom > 119 and CorNom <= 144:
                SecNom = 50
            elif CorNom > 144 and CorNom <= 184:
                SecNom = 70
            elif CorNom > 184 and CorNom <= 223:
                SecNom = 95
            elif CorNom > 233 and CorNom <= 259:
                SecNom = 120
            elif CorNom > 259 and CorNom <= 299:
                SecNom = 150
            elif CorNom > 299 and CorNom <= 341:
                SecNom = 185
            elif CorNom > 341 and CorNom <= 403:
                SecNom = 240
            elif CorNom > 403 and CorNom <= 464:
                SecNom = 300
            elif CorNom > 464 and CorNom <= 557:
                SecNom = 400
            elif CorNom > 557 and CorNom <= 642:
                SecNom = 500
            elif CorNom > 642 and CorNom <= 743:
                SecNom = 630
            elif CorNom > 743 and CorNom <= 865:
                SecNom = 800
            elif CorNom > 865 and CorNom <= 996:
                SecNom = 1000
            else:
                SecNom = "Seção Nominal Não Cadastrada"
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
            elif CorNom > 63 and CorNom <= 81:
                SecNom = 16
            elif CorNom > 81 and CorNom <= 104:
                SecNom = 25
            elif CorNom > 104 and CorNom <= 125:
                SecNom = 35
            elif CorNom > 125 and CorNom <= 148:
                SecNom = 50
            elif CorNom > 148 and CorNom <= 183:
                SecNom = 70
            elif CorNom > 183 and CorNom <= 216:
                SecNom = 95
            elif CorNom > 216 and CorNom <= 246:
                SecNom = 120
            elif CorNom > 246 and CorNom <= 278:
                SecNom = 150
            elif CorNom > 278 and CorNom <= 312:
                SecNom = 185
            elif CorNom > 312 and CorNom <= 361:
                SecNom = 240
            elif CorNom > 361 and CorNom <= 408:
                SecNom = 300
            elif CorNom > 408 and CorNom <= 478:
                SecNom = 400
            elif CorNom > 478 and CorNom <= 540:
                SecNom = 500
            elif CorNom > 540 and CorNom <= 614:
                SecNom = 630
            elif CorNom > 614 and CorNom <= 700:
                SecNom = 800
            elif CorNom > 700 and CorNom <= 792:
                SecNom = 1000
            else:
                SecNom = "Seção Nominal Não Cadastrada"
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
            elif CorNom > 52 and CorNom <= 67:
                SecNom = 16
            elif CorNom > 67 and CorNom <= 86:
                SecNom = 25
            elif CorNom > 86 and CorNom <= 103:
                SecNom = 35
            elif CorNom > 103 and CorNom <= 122:
                SecNom = 50
            elif CorNom > 122 and CorNom <= 151:
                SecNom = 70
            elif CorNom > 151 and CorNom <= 179:
                SecNom = 95
            elif CorNom > 179 and CorNom <= 203:
                SecNom = 120
            elif CorNom > 203 and CorNom <= 230:
                SecNom = 150
            elif CorNom > 230 and CorNom <= 258:
                SecNom = 185
            elif CorNom > 258 and CorNom <= 297:
                SecNom = 240
            elif CorNom > 297 and CorNom <= 336:
                SecNom = 300
            elif CorNom > 336 and CorNom <= 394:
                SecNom = 400
            elif CorNom > 394 and CorNom <= 445:
                SecNom = 500
            elif CorNom > 445 and CorNom <= 506:
                SecNom = 630
            elif CorNom > 506 and CorNom <= 577:
                SecNom = 800
            elif CorNom > 577 and CorNom <= 652:
                SecNom = 1000
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

def tab37e39(MetRef, CondCar, CorNom):
    if MetRef == 1:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 10:
                SecNom = 0.5
            elif CorNom > 10 and CorNom <= 12:
                SecNom = 0.75
            elif CorNom > 12 and CorNom <= 15:
                SecNom = 1
            elif CorNom > 15 and CorNom <= 19:
                SecNom = 1.5
            elif CorNom > 19 and CorNom <= 26:
                SecNom = 2.5
            elif CorNom > 26 and CorNom <= 35:
                SecNom = 4
            elif CorNom > 35 and CorNom <= 45:
                SecNom = 6
            elif CorNom > 45 and CorNom <= 61:
                SecNom = 10
            elif CorNom > 61 and CorNom <= 81:
                SecNom = 16
            elif CorNom > 81 and CorNom <= 106:
                SecNom = 25
            elif CorNom > 106 and CorNom <= 131:
                SecNom = 35
            elif CorNom > 131 and CorNom <= 158:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
        else:
            if CorNom <= 9:
                SecNom = 0.5
            elif CorNom > 9 and CorNom <= 11:
                SecNom = 0.75
            elif CorNom > 11 and CorNom <= 13:
                SecNom = 1
            elif CorNom > 13 and CorNom <= 17:
                SecNom = 1.5
            elif CorNom > 17 and CorNom <= 23:
                SecNom = 2.5
            elif CorNom > 23 and CorNom <= 31:
                SecNom = 4
            elif CorNom > 31 and CorNom <= 40:
                SecNom = 6
            elif CorNom > 40 and CorNom <= 54:
                SecNom = 10
            elif CorNom > 54 and CorNom <= 73:
                SecNom = 16
            elif CorNom > 73 and CorNom <= 95:
                SecNom = 25
            elif CorNom > 95 and CorNom <= 117:
                SecNom = 35
            elif CorNom > 117 and CorNom <= 141:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
    elif MetRef == 2:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 10:
                SecNom = 0.5
            elif CorNom > 10 and CorNom <= 12:
                SecNom = 0.75
            elif CorNom > 12 and CorNom <= 14:
                SecNom = 1
            elif CorNom > 14 and CorNom <= 18.5:
                SecNom = 1.5
            elif CorNom > 18.5 and CorNom <= 25:
                SecNom = 2.5
            elif CorNom > 25 and CorNom <= 33:
                SecNom = 4
            elif CorNom > 33 and CorNom <= 42:
                SecNom = 6
            elif CorNom > 42 and CorNom <= 57:
                SecNom = 10
            elif CorNom > 57 and CorNom <= 76:
                SecNom = 16
            elif CorNom > 76 and CorNom <= 99:
                SecNom = 25
            elif CorNom > 99 and CorNom <= 121:
                SecNom = 35
            elif CorNom > 121 and CorNom <= 145:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
        else:
            if CorNom <= 9:
                SecNom = 0.5
            elif CorNom > 9 and CorNom <= 11:
                SecNom = 0.75
            elif CorNom > 11 and CorNom <= 13:
                SecNom = 1
            elif CorNom > 13 and CorNom <= 16.5:
                SecNom = 1.5
            elif CorNom > 16.5 and CorNom <= 22:
                SecNom = 2.5
            elif CorNom > 22 and CorNom <= 30:
                SecNom = 4
            elif CorNom > 30 and CorNom <= 38:
                SecNom = 6
            elif CorNom > 38 and CorNom <= 51:
                SecNom = 10
            elif CorNom > 51 and CorNom <= 68:
                SecNom = 16
            elif CorNom > 68 and CorNom <= 89:
                SecNom = 25
            elif CorNom > 89 and CorNom <= 109:
                SecNom = 35
            elif CorNom > 109 and CorNom <= 130:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
    elif MetRef == 3:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 12:
                SecNom = 0.5
            elif CorNom > 12 and CorNom <= 15:
                SecNom = 0.75
            elif CorNom > 15 and CorNom <= 18:
                SecNom = 1
            elif CorNom > 18 and CorNom <= 23:
                SecNom = 1.5
            elif CorNom > 23 and CorNom <= 31:
                SecNom = 2.5
            elif CorNom > 31 and CorNom <= 42:
                SecNom = 4
            elif CorNom > 42 and CorNom <= 54:
                SecNom = 6
            elif CorNom > 54 and CorNom <= 75:
                SecNom = 10
            elif CorNom > 75 and CorNom <= 100:
                SecNom = 16
            elif CorNom > 100 and CorNom <= 133:
                SecNom = 25
            elif CorNom > 133 and CorNom <= 164:
                SecNom = 35
            elif CorNom > 164 and CorNom <= 198:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
        else:
            if CorNom <= 10:
                SecNom = 0.5
            elif CorNom > 10 and CorNom <= 13:
                SecNom = 0.75
            elif CorNom > 13 and CorNom <= 16:
                SecNom = 1
            elif CorNom > 16 and CorNom <= 20:
                SecNom = 1.5
            elif CorNom > 20 and CorNom <= 28:
                SecNom = 2.5
            elif CorNom > 28 and CorNom <= 37:
                SecNom = 4
            elif CorNom > 37 and CorNom <= 48:
                SecNom = 6
            elif CorNom > 48 and CorNom <= 66:
                SecNom = 10
            elif CorNom > 66 and CorNom <= 88:
                SecNom = 16
            elif CorNom > 88 and CorNom <= 117:
                SecNom = 25
            elif CorNom > 117 and CorNom <= 144:
                SecNom = 35
            elif CorNom > 144 and CorNom <= 175:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
    elif MetRef == 4:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 11:
                SecNom = 0.5
            elif CorNom > 11 and CorNom <= 15:
                SecNom = 0.75
            elif CorNom > 15 and CorNom <= 17:
                SecNom = 1
            elif CorNom > 17 and CorNom <= 22:
                SecNom = 1.5
            elif CorNom > 22 and CorNom <= 30:
                SecNom = 2.5
            elif CorNom > 30 and CorNom <= 40:
                SecNom = 4
            elif CorNom > 40 and CorNom <= 51:
                SecNom = 6
            elif CorNom > 51 and CorNom <= 69:
                SecNom = 10
            elif CorNom > 69 and CorNom <= 91:
                SecNom = 16
            elif CorNom > 91 and CorNom <= 119:
                SecNom = 25
            elif CorNom > 119 and CorNom <= 146:
                SecNom = 35
            elif CorNom > 146 and CorNom <= 175:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
        else:
            if CorNom <= 10:
                SecNom = 0.5
            elif CorNom > 10 and CorNom <= 13:
                SecNom = 0.75
            elif CorNom > 13 and CorNom <= 15:
                SecNom = 1
            elif CorNom > 15 and CorNom <= 19.5:
                SecNom = 1.5
            elif CorNom > 19.5 and CorNom <= 26:
                SecNom = 2.5
            elif CorNom > 26 and CorNom <= 35:
                SecNom = 4
            elif CorNom > 35 and CorNom <= 44:
                SecNom = 6
            elif CorNom > 44 and CorNom <= 60:
                SecNom = 10
            elif CorNom > 60 and CorNom <= 80:
                SecNom = 16
            elif CorNom > 80 and CorNom <= 105:
                SecNom = 25
            elif CorNom > 105 and CorNom <= 128:
                SecNom = 35
            elif CorNom > 128 and CorNom <= 154:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
    elif MetRef == 5:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 12:
                SecNom = 0.5
            elif CorNom > 12 and CorNom <= 16:
                SecNom = 0.75
            elif CorNom > 16 and CorNom <= 19:
                SecNom = 1
            elif CorNom > 19 and CorNom <= 24:
                SecNom = 1.5
            elif CorNom > 24 and CorNom <= 33:
                SecNom = 2.5
            elif CorNom > 33 and CorNom <= 45:
                SecNom = 4
            elif CorNom > 45 and CorNom <= 58:
                SecNom = 6
            elif CorNom > 58 and CorNom <= 80:
                SecNom = 10
            elif CorNom > 80 and CorNom <= 107:
                SecNom = 16
            elif CorNom > 107 and CorNom <= 138:
                SecNom = 25
            elif CorNom > 138 and CorNom <= 171:
                SecNom = 35
            elif CorNom > 171 and CorNom <= 209:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
        else:
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
            elif CorNom > 40 and CorNom <= 52:
                SecNom = 6
            elif CorNom > 52 and CorNom <= 71:
                SecNom = 10
            elif CorNom > 71 and CorNom <= 96:
                SecNom = 16
            elif CorNom > 96 and CorNom <= 119:
                SecNom = 25
            elif CorNom > 119 and CorNom <= 147:
                SecNom = 35
            elif CorNom > 147 and CorNom <= 179:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
    elif MetRef == 6:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 14:
                SecNom = 0.5
            elif CorNom > 14 and CorNom <= 18:
                SecNom = 0.75
            elif CorNom > 18 and CorNom <= 21:
                SecNom = 1
            elif CorNom > 21 and CorNom <= 26:
                SecNom = 1.5
            elif CorNom > 26 and CorNom <= 34:
                SecNom = 2.5
            elif CorNom > 34 and CorNom <= 44:
                SecNom = 4
            elif CorNom > 44 and CorNom <= 56:
                SecNom = 6
            elif CorNom > 56 and CorNom <= 73:
                SecNom = 10
            elif CorNom > 73 and CorNom <= 95:
                SecNom = 16
            elif CorNom > 95 and CorNom <= 121:
                SecNom = 25
            elif CorNom > 121 and CorNom <= 146:
                SecNom = 35
            elif CorNom > 146 and CorNom <= 173:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
        else:
            if CorNom <= 12:
                SecNom = 0.5
            elif CorNom > 12 and CorNom <= 15:
                SecNom = 0.75
            elif CorNom > 15 and CorNom <= 17:
                SecNom = 1
            elif CorNom > 17 and CorNom <= 22:
                SecNom = 1.5
            elif CorNom > 22 and CorNom <= 29:
                SecNom = 2.5
            elif CorNom > 29 and CorNom <= 37:
                SecNom = 4
            elif CorNom > 37 and CorNom <= 46:
                SecNom = 6
            elif CorNom > 46 and CorNom <= 61:
                SecNom = 10
            elif CorNom > 61 and CorNom <= 79:
                SecNom = 16
            elif CorNom > 79 and CorNom <= 101:
                SecNom = 25
            elif CorNom > 101 and CorNom <= 122:
                SecNom = 35
            elif CorNom > 122 and CorNom <= 144:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
    elif MetRef == 7:
        if CondCar == 1 or CondCar == 2 or CondCar == 3:
            if CorNom <= 13:
                SecNom = 0.5
            elif CorNom > 13 and CorNom <= 17:
                SecNom = 0.75
            elif CorNom > 17 and CorNom <= 21:
                SecNom = 1
            elif CorNom > 21 and CorNom <= 26:
                SecNom = 1.5
            elif CorNom > 26 and CorNom <= 36:
                SecNom = 2.5
            elif CorNom > 36 and CorNom <= 49:
                SecNom = 4
            elif CorNom > 49 and CorNom <= 63:
                SecNom = 6
            elif CorNom > 63 and CorNom <= 86:
                SecNom = 10
            elif CorNom > 86 and CorNom <= 115:
                SecNom = 16
            elif CorNom > 115 and CorNom <= 149:
                SecNom = 25
            elif CorNom > 149 and CorNom <= 185:
                SecNom = 35
            elif CorNom > 185 and CorNom <= 225:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
        else:
            if CorNom <= 12:
                SecNom = 0.5
            elif CorNom > 12 and CorNom <= 15:
                SecNom = 0.75
            elif CorNom > 15 and CorNom <= 18:
                SecNom = 1
            elif CorNom > 18 and CorNom <= 23:
                SecNom = 1.5
            elif CorNom > 23 and CorNom <= 32:
                SecNom = 2.5
            elif CorNom > 32 and CorNom <= 42:
                SecNom = 4
            elif CorNom > 42 and CorNom <= 54:
                SecNom = 6
            elif CorNom > 54 and CorNom <= 75:
                SecNom = 10
            elif CorNom > 75 and CorNom <= 100:
                SecNom = 16
            elif CorNom > 100 and CorNom <= 127:
                SecNom = 25
            elif CorNom > 127 and CorNom <= 158:
                SecNom = 35
            elif CorNom > 158 and CorNom <= 192:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
    elif MetRef == 8:
        if CondCar == 1:
            if CorNom <= 13:
                SecNom = 0.5
            elif CorNom > 13 and CorNom <= 17:
                SecNom = 0.75
            elif CorNom > 17 and CorNom <= 21:
                SecNom = 1
            elif CorNom > 21 and CorNom <= 27:
                SecNom = 1.5
            elif CorNom > 26 and CorNom <= 37:
                SecNom = 2.5
            elif CorNom > 36 and CorNom <= 50:
                SecNom = 4
            elif CorNom > 49 and CorNom <= 65:
                SecNom = 6
            elif CorNom > 63 and CorNom <= 90:
                SecNom = 10
            elif CorNom > 86 and CorNom <= 121:
                SecNom = 16
            elif CorNom > 115 and CorNom <= 161:
                SecNom = 25
            elif CorNom > 149 and CorNom <= 200:
                SecNom = 35
            elif CorNom > 185 and CorNom <= 242:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
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
            elif CorNom > 29 and CorNom <= 40:
                SecNom = 4
            elif CorNom > 40 and CorNom <= 53:
                SecNom = 6
            elif CorNom > 53 and CorNom <= 74:
                SecNom = 10
            elif CorNom > 74 and CorNom <= 101:
                SecNom = 16
            elif CorNom > 101 and CorNom <= 135:
                SecNom = 25
            elif CorNom > 135 and CorNom <= 169:
                SecNom = 35
            elif CorNom > 169 and CorNom <= 207:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
        elif CondCar == 3:
            if CorNom <= 10:
                SecNom = 0.5
            elif CorNom > 10 and CorNom <= 14:
                SecNom = 0.75
            elif CorNom > 14 and CorNom <= 17:
                SecNom = 1
            elif CorNom > 17 and CorNom <= 22:
                SecNom = 1.5
            elif CorNom > 22 and CorNom <= 30:
                SecNom = 2.5
            elif CorNom > 30 and CorNom <= 42:
                SecNom = 4
            elif CorNom > 42 and CorNom <= 55:
                SecNom = 6
            elif CorNom > 55 and CorNom <= 77:
                SecNom = 10
            elif CorNom > 77 and CorNom <= 105:
                SecNom = 16
            elif CorNom > 105 and CorNom <= 141:
                SecNom = 25
            elif CorNom > 141 and CorNom <= 176:
                SecNom = 35
            elif CorNom > 176 and CorNom <= 216:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
    elif MetRef == 9:
        if CondCar == 1:
            if CorNom <= 15:
                SecNom = 0.5
            elif CorNom > 15 and CorNom <= 19:
                SecNom = 0.75
            elif CorNom > 19 and CorNom <= 23:
                SecNom = 1
            elif CorNom > 23 and CorNom <= 30:
                SecNom = 1.5
            elif CorNom > 30 and CorNom <= 41:
                SecNom = 2.5
            elif CorNom > 41 and CorNom <= 56:
                SecNom = 4
            elif CorNom > 56 and CorNom <= 73:
                SecNom = 6
            elif CorNom > 73 and CorNom <= 101:
                SecNom = 10
            elif CorNom > 101 and CorNom <= 137:
                SecNom = 16
            elif CorNom > 137 and CorNom <= 182:
                SecNom = 25
            elif CorNom > 182 and CorNom <= 226:
                SecNom = 35
            elif CorNom > 226 and CorNom <= 275:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
        elif CondCar == 2:
            if CorNom <= 12:
                SecNom = 0.5
            elif CorNom > 12 and CorNom <= 16:
                SecNom = 0.75
            elif CorNom > 16 and CorNom <= 19:
                SecNom = 1
            elif CorNom > 19 and CorNom <= 25:
                SecNom = 1.5
            elif CorNom > 25 and CorNom <= 35:
                SecNom = 2.5
            elif CorNom > 35 and CorNom <= 48:
                SecNom = 4
            elif CorNom > 48 and CorNom <= 63:
                SecNom = 6
            elif CorNom > 63 and CorNom <= 88:
                SecNom = 10
            elif CorNom > 88 and CorNom <= 120:
                SecNom = 16
            elif CorNom > 120 and CorNom <= 161:
                SecNom = 25
            elif CorNom > 161 and CorNom <= 201:
                SecNom = 35
            elif CorNom > 201 and CorNom <= 246:
                SecNom = 50
            else:
                SecNom = "Seção Nominal Não Cadastrada"
    return(SecNom)

def tabNeutro(SecNom):
    if SecNom <= 25:
        SecNeutro = SecNom
    elif SecNom > 25 and SecNom <= 50:
        SecNeutro = 25
    elif SecNom > 50 and SecNom <= 70:
        SecNeutro = 35
    elif SecNom > 70 and SecNom <= 95:
        SecNeutro = 50
    elif SecNom > 95 and SecNom <= 150:
        SecNeutro = 70
    elif SecNom > 150 and SecNom <= 185:
        SecNeutro = 95
    elif SecNom > 185 and SecNom <= 240:
        SecNeutro = 120
    elif SecNom > 240 and SecNom <= 300:
        SecNeutro = 150
    elif SecNom > 300 and SecNom <= 500:
        SecNeutro = 185
    else:
        SecNeutro = "Seção Não Cadastrada"
    return(SecNeutro)

def tabProt(SecNom):
    if SecNom <= 16:
        SecProt = SecNom
    elif SecNom > 16 and SecNom <= 35:
        SecProt = 16
    else:
        SecProt = 0.5*SecNom
    return(SecProt)

def tabCorTemp(temp, isol, metInst):
    if isol == 1:
        if metInst == 1:
            if temp <= 10:
                corTemp = 1.22
            elif temp > 10 and temp <= 15:
                corTemp = 1.17
            elif temp > 15 and temp <= 25:
                corTemp = 1.12
            elif temp > 25 and temp <= 30:
                corTemp = 1.06
            elif temp > 30 and temp <= 35:
                corTemp = 0.94
            elif temp > 35 and temp <= 40:
                corTemp = 0.87
            elif temp > 40 and temp <= 45:
                corTemp = 0.79
            elif temp > 45 and temp <= 50:
                corTemp = 0.71
            elif temp > 50 and temp <= 55:
                corTemp = 0.61
            elif temp > 55 and temp <= 60:
                corTemp = 0.50
            else:
                corTemp = "Fator de Correção Não Encontrado"
        else:
            if temp <= 10:
                corTemp = 1.10
            elif temp > 10 and temp <= 15:
                corTemp = 1.05
            elif temp > 15 and temp <= 25:
                corTemp = 0.95
            elif temp > 25 and temp <= 30:
                corTemp = 0.89
            elif temp > 30 and temp <= 35:
                corTemp = 0.84
            elif temp > 35 and temp <= 40:
                corTemp = 0.77
            elif temp > 40 and temp <= 45:
                corTemp = 0.71
            elif temp > 45 and temp <= 50:
                corTemp = 0.63
            elif temp > 50 and temp <= 55:
                corTemp = 0.55
            elif temp > 55 and temp <= 60:
                corTemp = 0.45
            else:
                corTemp = "Fator de Correção Não Encontrado"
    else:
        if metInst == 1:
            if temp <= 10:
                corTemp = 1.15
            elif temp > 10 and temp <= 15:
                corTemp = 1.12
            elif temp > 15 and temp <= 25:
                corTemp = 1.08
            elif temp > 25 and temp <= 30:
                corTemp = 1.04
            elif temp > 30 and temp <= 35:
                corTemp = 0.96
            elif temp > 35 and temp <= 40:
                corTemp = 0.91
            elif temp > 40 and temp <= 45:
                corTemp = 0.87
            elif temp > 45 and temp <= 50:
                corTemp = 0.82
            elif temp > 50 and temp <= 55:
                corTemp = 0.76
            elif temp > 55 and temp <= 60:
                corTemp = 0.71
            elif temp > 60 and temp <= 65:
                corTemp = 0.65
            elif temp > 65 and temp <= 70:
                corTemp = 0.58
            elif temp > 70 and temp <= 75:
                corTemp = 0.50
            elif temp > 75 and temp <= 80:
                corTemp = 0.41
            else:
                corTemp = "Fator de Correção Não Encontrado"
        else:
            if temp <= 10:
                corTemp = 1.07
            elif temp > 10 and temp <= 15:
                corTemp = 1.04
            elif temp > 15 and temp <= 25:
                corTemp = 0.96
            elif temp > 25 and temp <= 30:
                corTemp = 0.93
            elif temp > 30 and temp <= 35:
                corTemp = 0.89
            elif temp > 35 and temp <= 40:
                corTemp = 0.85
            elif temp > 40 and temp <= 45:
                corTemp = 0.80
            elif temp > 45 and temp <= 50:
                corTemp = 0.76
            elif temp > 50 and temp <= 55:
                corTemp = 0.71
            elif temp > 55 and temp <= 60:
                corTemp = 0.65
            elif temp > 60 and temp <= 65:
                corTemp = 0.60
            elif temp > 65 and temp <= 70:
                corTemp = 0.53
            elif temp > 70 and temp <= 75:
                corTemp = 0.46
            elif temp > 75 and temp <= 80:
                corTemp = 0.38
            else:
                corTemp = "Fator de Correção Não Encontrado"
    return(corTemp)

def tabCorAgr(metRef, dispCab, numCirc):
    if metRef >= 1 and metRef < 9:
        if dispCab == 1:
            if numCirc <= 1:
                fatAgr = 1
            elif numCirc > 1 and numCirc <= 2:
                fatAgr = 0.8
            elif numCirc > 2 and numCirc <= 3:
                fatAgr = 0.7
            ########################
    return()


def tab32(ele, quantCab, tam, tip):
##  Eletrodutos Rígidos PVC
    if ele == 1:
        if quantCab == 2:
    ##        Classe A
            if tip == 1:
                if tam <= 37:
                    SecEle = 16
                elif tam > 37 and tam <= 60:
                    SecEle = 20
                elif tam > 60 and tam <= 166:
                    SecEle = 25
                elif tam > 166 and tam <= 170:
                    SecEle = 32
                elif tam > 170 and tam <= 282:
                    SecEle = 40
                elif tam > 282 and tam <= 377:
                    SecEle = 50
                elif tam > 377 and tam <= 603:
                    SecEle = 60
                elif tam > 603 and tam <= 987:
                    SecEle = 75
                elif tam > 987 and tam <= 1318:
                    SecEle = 85
                elif tam > 1318 and tam <= 1396:
                    SecEle = 100
                else:
                    SecEle = "Seção de Eletroduto Não Cadastrado"
            ##        Classe B
            if tip == 2:
                if tam <= 40:
                    SecEle = 16
                elif tam > 40 and tam <= 71:
                    SecEle = 20
                elif tam > 71 and tam <= 113:
                    SecEle = 25
                elif tam > 113 and tam <= 183:
                    SecEle = 32
                elif tam > 183 and tam <= 317:
                    SecEle = 40
                elif tam > 317 and tam <= 417:
                    SecEle = 50
                elif tam > 417 and tam <= 678:
                    SecEle = 60
                elif tam > 678 and tam <= 1096:
                    SecEle = 75
                elif tam > 1096 and tam <= 1443:
                    SecEle = 85
                elif tam > 1443 and tam <= 1542:
                    SecEle = 100
                else:
                    SecEle = "Seção de Eletroduto Não Cadastrado"

        if quantCab == 3:
    ##        Classe A
            if tip == 1:
                if tam <= 48:
                    SecEle = 16
                elif tam > 48 and tam <= 79:
                    SecEle = 20
                elif tam > 79 and tam <= 135:
                    SecEle = 25
                elif tam > 135 and tam <= 221:
                    SecEle = 32
                elif tam > 221 and tam <= 378:
                    SecEle = 40
                elif tam > 378 and tam <= 488:
                    SecEle = 50
                elif tam > 488 and tam <= 779:
                    SecEle = 60
                elif tam > 779 and tam <= 1275:
                    SecEle = 75
                elif tam > 1275 and tam <= 1701:
                    SecEle = 85
                elif tam > 1701 and tam <= 1777:
                    SecEle = 100
                else:
                    SecEle = "Seção de Eletroduto Não Cadastrado"
            ##        Classe B
            if tip == 2:
                if tam <= 52:
                    SecEle = 16
                elif tam > 52 and tam <= 93:
                    SecEle = 20
                elif tam > 93 and tam <= 143:
                    SecEle = 25
                elif tam > 143 and tam <= 238:
                    SecEle = 32
                elif tam > 238 and tam <= 410:
                    SecEle = 40
                elif tam > 410 and tam <= 539:
                    SecEle = 50
                elif tam > 539 and tam <= 876:
                    SecEle = 60
                elif tam > 876 and tam <= 1415:
                    SecEle = 75
                elif tam > 1415 and tam <= 1862:
                    SecEle = 85
                elif tam > 1862 and tam <= 1976:
                    SecEle = 100
                else:
                    SecEle = "Seção de Eletroduto Não Cadastrado"


##  Eletrodutos Rígidos Aço Carbono
    if ele == 2:
        if quantCab == 2:
    ##        Extra
            if tip == 1:
                if tam <= 36:
                    SecEle = 10
                elif tam > 36 and tam <= 60:
                    SecEle = 15
                elif tam > 60 and tam <= 107:
                    SecEle = 20
                elif tam > 107 and tam <= 177:
                    SecEle = 25
                elif tam > 177 and tam <= 300:
                    SecEle = 32
                elif tam > 300 and tam <= 413:
                    SecEle = 40
                elif tam > 413 and tam <= 668:
                    SecEle = 50
                elif tam > 668 and tam <= 997:
                    SecEle = 65
                elif tam > 997 and tam <= 2036:
                    SecEle = 80
                elif tam > 2036 and tam <= 2616:
                    SecEle = 90
                elif tam > 2616 and tam <= 3908:
                    SecEle = 100
                elif tam > 3908 and tam <= 4118:
                    SecEle = 125
                elif tam > 4118 and tam <= 5827:
                    SecEle = 150
                else:
                    SecEle = "Seção de Eletroduto Não Cadastrado"
    ##        Pesada
            if tip == 2:
                if tam <= 40:
                    SecEle = 10
                elif tam > 40 and tam <= 65:
                    SecEle = 15
                elif tam > 65 and tam <= 115:
                    SecEle = 20
                elif tam > 115 and tam <= 187:
                    SecEle = 25
                elif tam > 187 and tam <= 312:
                    SecEle = 32
                elif tam > 312 and tam <= 427:
                    SecEle = 40
                elif tam > 427 and tam <= 689:
                    SecEle = 50
                elif tam > 689 and tam <= 1032:
                    SecEle = 65
                elif tam > 1032 and tam <= 2126:
                    SecEle = 80
                elif tam > 2126 and tam <= 2692:
                    SecEle = 90
                elif tam > 2692 and tam <= 4032:
                    SecEle = 100
                elif tam > 4032 and tam <= 4252:
                    SecEle = 125
                elif tam > 4252 and tam <= 5978:
                    SecEle = 150
                else:
                    SecEle = "Seção de Eletroduto Não Cadastrado"

        if quantCab >= 3:
    ##        Extra
            if tip == 1:
                if tam <= 47:
                    SecEle = 10
                elif tam > 47 and tam <= 77:
                    SecEle = 15
                elif tam > 77 and tam <= 139:
                    SecEle = 20
                elif tam > 139 and tam <= 230:
                    SecEle = 25
                elif tam > 230 and tam <= 388:
                    SecEle = 32
                elif tam > 388 and tam <= 534:
                    SecEle = 40
                elif tam > 534 and tam <= 863:
                    SecEle = 50
                elif tam > 863 and tam <= 1261:
                    SecEle = 65
                elif tam > 1261 and tam <= 2628:
                    SecEle = 80
                elif tam > 2628 and tam <= 3376:
                    SecEle = 90
                elif tam > 3376 and tam <= 5043:
                    SecEle = 100
                elif tam > 5043 and tam <= 5315:
                    SecEle = 125
                elif tam > 5315 and tam <= 7519:
                    SecEle = 150
                else:
                    SecEle = "Seção de Eletroduto Não Cadastrado"
    ##        Pesada
            if tip == 2:
                if tam <= 51:
                    SecEle = 10
                elif tam > 51 and tam <= 85:
                    SecEle = 15
                elif tam > 85 and tam <= 150:
                    SecEle = 20
                elif tam > 150 and tam <= 242:
                    SecEle = 25
                elif tam > 242 and tam <= 403:
                    SecEle = 32
                elif tam > 403 and tam <= 552:
                    SecEle = 40
                elif tam > 552 and tam <= 890:
                    SecEle = 50
                elif tam > 890 and tam <= 1333:
                    SecEle = 65
                elif tam > 1333 and tam <= 2745:
                    SecEle = 80
                elif tam > 2745 and tam <= 3474:
                    SecEle = 90
                elif tam > 3474 and tam <= 5204:
                    SecEle = 100
                elif tam > 5204 and tam <= 5487:
                    SecEle = 125
                elif tam > 5487 and tam <= 7714:
                    SecEle = 150
                else:
                    SecEle = "Seção de Eletroduto Não Cadastrado"
    return(SecEle)


def tab35(tam):
    if tam <= 2000:
        Cal = "50x40"
    elif tam > 2000 and tam <= 4000:
        Cal = "100x40"
    elif tam > 4000 and tam <= 9000:
        Cal = "150x60"
    elif tam > 9000 and tam <= 12000:
        Cal = "200x60"
    elif tam > 12000 and tam <= 22500:
        Cal = "300x75"
    elif tam > 22500 and tam <= 30000:
        Cal = "400x75"
    elif tam > 30000 and tam <= 50000:
        Cal = "500x100"
    elif tam > 50000 and tam <= 60000:
        Cal = "600x100"
    return(Cal)



def tab33(tip, sec):
    if tip == "Condutor":
        if sec == 1.5:
            diam = 1.56
        elif sec == 2.5:
            diam = 2.01
        elif sec == 4:
            diam = 2.55
        elif sec == 6:
            diam = 3
        elif sec == 10:
            diam = 3.12
        elif sec == 16:
            diam = 4.71
        elif sec == 25:
            diam = 5.87
        elif sec == 35:
            diam = 6.95
        elif sec == 50:
            diam = 8.27
        elif sec == 70:
            diam = 9.75
        elif sec == 95:
            diam = 11.42
        elif sec == 120:
            diam = 12.23
        elif sec == 150:
            diam = 14.33
        elif sec == 185:
            diam = 16.05
        elif sec == 240:
            diam = 18.27
        elif sec == 300:
            diam = 20.46
        elif sec == 400:
            diam = 23.65
        elif sec == 500:
            diam = 26.71
        elif sec == 630:
            diam = 29.26
        else:
            diam = "Diâmetro Não Cadastrado"

    if tip == "Cabo Isolado":
        if sec == 1.5:
            diam = 3
        elif sec == 2.5:
            diam = 3.7
        elif sec == 4:
            diam = 4.3
        elif sec == 6:
            diam = 4.9
        elif sec == 10:
            diam = 5.9
        elif sec == 16:
            diam = 6.9
        elif sec == 25:
            diam = 8.5
        elif sec == 35:
            diam = 9.6
        elif sec == 50:
            diam = 11.3
        elif sec == 70:
            diam = 12.9
        elif sec == 95:
            diam = 15.1
        elif sec == 120:
            diam = 16.5
        elif sec == 150:
            diam = 18.5
        elif sec == 185:
            diam = 20.7
        elif sec == 240:
            diam = 23.4
        elif sec == 300:
            diam = 26
        elif sec == 400:
            diam = 29.7
        elif sec == 500:
            diam = 33.3
        elif sec == 630:
            diam = 36.2
        else:
            diam = "Diâmetro Não Cadastrado"


    if tip == "Cabo Unipolar":
        if sec == 1.5:
            diam = 5.5
        elif sec == 2.5:
            diam = 6
        elif sec == 4:
            diam = 6.8
        elif sec == 6:
            diam = 7.3
        elif sec == 10:
            diam = 8
        elif sec == 16:
            diam = 9
        elif sec == 25:
            diam = 10.8
        elif sec == 35:
            diam = 12
        elif sec == 50:
            diam = 13.9
        elif sec == 70:
            diam = 15.5
        elif sec == 95:
            diam = 17.7
        elif sec == 120:
            diam = 19.2
        elif sec == 150:
            diam = 21.4
        elif sec == 185:
            diam = 23.8
        elif sec == 240:
            diam = 26.7
        elif sec == 300:
            diam = 29.5
        elif sec == 400:
            diam = 33.5
        elif sec == 500:
            diam = 37.3
        elif sec == 630:
            diam = 40.25
        else:
            diam = "Diâmetro Não Cadastrado"

    return(diam)
