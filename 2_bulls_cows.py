import random

def bulls_cows(cisla):

    print('''
    Vítám tě v této hře BULLS and COWS
    mám vygenerovaná náhodná 4 čísla
    a musíš je uhodnout, max počet typů 
    máš 20, poté hra končí.

    HODNĚ ŠTĚSTÍ!
    ''')

    ODELOVAC = '-' * 30
    print(ODELOVAC)

    # VYGENEROVANI NAHODNOHO CISLA POCITACEM
    konec = True

    while konec:
        cislo_a = random.choice(cisla)
        cisla.remove(cislo_a)
        cislo_b = random.choice(cisla)
        cisla.remove(cislo_b)
        cislo_c = random.choice(cisla)
        cisla.remove(cislo_c)
        cislo_d = random.choice(cisla)
        # print(cislo_a, cislo_b, cislo_c, cislo_d)

        vygener_cisla = [cislo_a, cislo_b, cislo_c, cislo_d]

        pocet_typu = 0

        # ZADANI TYPOVANEHO CISLA
        while konec:
            typ = input('zadej cislo: ')
            print(ODELOVAC)

            if not typ.isnumeric() or int(typ) > 9999 or int(typ) <= 999:
                print('spatne zadane cislo')
                print(ODELOVAC)
                continue

            prvni_cislo = int(typ[0])
            druhy_cislo = int(typ[1])
            treti_cislo = int(typ[2])
            ctvrty_cislo = int(typ[3])

            bulls = 0
            cows = 0

            # POROVNANI TYPOVANEHO CISLA
            while prvni_cislo in vygener_cisla:
                if prvni_cislo == cislo_a:
                    bulls += 1
                else:
                    cows += 1
                break

            while druhy_cislo in vygener_cisla:
                if druhy_cislo == cislo_b:
                    bulls += 1
                else:
                    cows += 1
                break

            while treti_cislo in vygener_cisla:
                if treti_cislo == cislo_c:
                    bulls += 1
                else:
                    cows += 1
                break

            while ctvrty_cislo in vygener_cisla:
                if ctvrty_cislo == cislo_d:
                    bulls += 1
                else:
                    cows += 1
                break

            # VYPIS VYSLEDKU
            if bulls == 4 or pocet_typu == 20:
                if pocet_typu < 4:
                    print(f'GRATULUJI JSI EXPERT!')
                    print(ODELOVAC)
                elif pocet_typu < 9:
                    print(f'GRATULUJI JSI DOBRÝ!')
                    print(ODELOVAC)
                elif pocet_typu < 20:
                    print(f'NIC MOC, ZKUS TO ZNOVA! :-)')
                    print(ODELOVAC)

                konec = False

            pocet_typu += 1

            print(f'{bulls} bulls, {cows} cows, {pocet_typu} pocet typu')
            print(ODELOVAC)

bulls_cows(list(range(1, 10)))