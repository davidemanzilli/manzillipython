import statistics as sts

italiano = []
latino = []
matematica = []
scienze = []
fisica = []
arte = []
motorie = []
storia = []
filosofia = []
inglese = []
civica = []
try:
    while True:
        scelta = input("vuoi inserire i voti di italiano? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di italiano vuoi inserire?"))):
                italiano.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        scelta = input("vuoi inserire i voti di matematica? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di matematica vuoi inserire?"))):
                matematica.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        scelta = input("vuoi inserire i voti di latino? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di latino vuoi inserire?"))):
                latino.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        scelta = input("vuoi inserire i voti di fisica? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di fisica vuoi inserire?"))):
                fisica.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        scelta = input("vuoi inserire i voti di arte? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di arte vuoi inserire?"))):
                arte.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        scelta = input("vuoi inserire i voti di motorie? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di motorie vuoi inserire?"))):
                motorie.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        scelta = input("vuoi inserire i voti di storia? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di storia vuoi inserire?"))):
                storia.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        scelta = input("vuoi inserire i voti di filosofia? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di filosofia vuoi inserire?"))):
                filosofia.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        scelta = input("vuoi inserire i voti di inglese? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di inglese vuoi inserire?"))):
                inglese.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        scelta = input("vuoi inserire i voti di civica? digita si o no ")
        if scelta == "si":
            for i in range(int(input("quanti voti di civica vuoi inserire?"))):
                civica.append(int(input("inserisci un voto")))
        scelta = input("vuoi inserire i voti di altre materie? digita si o no ")
        if scelta == "no":
            break
        break

    while True:
        scelta = input("vuoi la media di una materia o di tutte? digita singola o tutte |ATTENZIONE DEVI AVER INSERITO I VOTI A TUTTE LE MATERIE PER VISUALIZZARLE TUTTE INSIEME| ")
        if scelta == "tutte":
            print(sts.mean(italiano))
            print(sts.mean(matematica))
            print(sts.mean(scienze))
            print(sts.mean(latino))
            print(sts.mean(fisica))
            print(sts.mean(inglese))
            print(sts.mean(motorie))
            print(sts.mean(civica))
            print(sts.mean(filosofia))
            print(sts.mean(storia))
            print(sts.mean(arte))
        elif scelta == "singola":
            scelta = input("Di quale materia vuoi la media? digitane una in minuscolo ")
            if scelta == "italiano":
                print(sts.mean(italiano))
            elif scelta == "matematica":
                print(sts.mean(matematica))
            elif scelta == "latino":
                print(sts.mean(latino))
            elif scelta == "scienze":
                print(sts.mean(scienze))
            elif scelta == "fisica":
                print(sts.mean(fisica))
            elif scelta == "inglese":
                print(sts.mean(inglese))
            elif scelta == "motorie":
                print(sts.mean(motorie))
            elif scelta == "civica":
                print(sts.mean(civica))
            elif scelta == "filosofia":
                print(sts.mean(filosofia))
            elif scelta == "storia":
                print(sts.mean(storia))
            elif scelta == "arte":
                print(sts.mean(arte))
        break
except ValueError:
    print("devi inserire dei numeri ")

