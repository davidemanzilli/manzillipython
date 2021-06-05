try:
        giorni = int(input("per quanti giorni vuoi noleggiare lo scooter?"))
        giorno1 = 45
        euro = 40
        if giorni == 1:
                print(giorno1)
        elif giorni > 1:
	        print("sono",euro*giorni)
except ValueError:
        print("solo numeri grazie")
        


