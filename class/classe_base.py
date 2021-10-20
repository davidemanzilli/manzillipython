
import math

# classe calcolo combinatorio
class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        if type(self.__stringa) == str:
            print("si è una stringa")

    def confUtil(self): #verificare se la STRINGA attributo di istanza è presente nel file word.italian.txt 
        print(
        """
        al termine dell'operazione di verifichera otterai il risultato 
        """ 
        ) 
        conta = 0
        f = open("class\words.italian.txt", 'r')
        print(self.__stringa)
        for riga in f:
            righe = f.readline()
            #print(righe)
            #print(self.__stringa)
            if self.__stringa in righe:
                conta  += 1
                break
        f.close()
        if conta == 0:
            print("la parola non è presente nel dizionario")
        else: 
            print("la parola è contenuta nel dizionario ")

    
    # PERMUTAZIONI

    def nPermutSenzaRip(self):

        n = len(self.__stringa)

        permutazioni = math.factorial(n)

        print("il numero di permutazioni è", permutazioni)

    def nPermutConRip(self):
        '''
        restituire il numero di permutazioni CON ripetizione
        '''
        return 0

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        return 0

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self, k):
        
        n = len(self.__stringa)

        if n >= k:    
            disp=math.factorial(n)/(math.factorial(n-k))
            print("il numero di disposizioni semplici è", disp)
        else:
            print("k non puo essere maggiore di n nelle disposizione semplici")

    def nDispSemplConRip(self, k):
        n = len(self.__stringa)
        disp=n**k
        print("il numero di disposizioni con ripetizione è",disp)

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self, k):
        n = len(self.__stringa)
        combsemplici = math.factorial(n) / (math.factorial(k) * (math.factorial(n-k)))
        print("il numero di combinazioni semplici è ",combsemplici)

    def nCombSemplConRip(self, k):
        
        n = len(self.__stringa)

        comb = math.factorial(n+k-1) / (math.factorial(k) * (math.factorial(n-1)))

        print("il numero di combinazioni con ripetizione è ",comb)

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0

prova = calcComb("prova")

prova.nCombSemplConRip(4)
