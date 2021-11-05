
import math

"""classe calcolo combinatorio"""
class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self, str):
        self.__stringa = str
        self.__N = len(str)
        self.__listStringa = list(str)

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
            return False
        else: 
            return True   # in questo modo però restituisci true anche se la parola è una sottostringa. se cerci "pop" restiuisce vero perchè: POPolazione lo contiene


    def charRipetuti(self):
        ripetizioni = {}
        for carattere in range(self.__N):
            if self.__stringa[carattere] not in ripetizioni.keys():
                ripetizioni.setdefault(self.__stringa[carattere], 1)
            else:
                ripetizioni[self.__stringa[carattere]] += 1
        ndiripetizioni = 1
        for values in ripetizioni.values():
            if values > 1:
                ndiripetizioni *= math.factorial(values)
        return ndiripetizioni

    """PERMUTAZIONI"""

    def nPermutSenzaRip(self):

        return math.factorial(self.__N)

    def nPermutConRip(self): #ho reinserito qui il codice per facilitare il lavoro evitando di dover andare a richiamare la definizione
        return (math.factorial(self.__N))/calcComb.charRipetuti(self)

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

    """DISPOSIZIONI"""

    def nDispSemplSenzaRip(self, k):
        
        n = len(self.__stringa)

        if n >= k:    
            return math.factorial(self.__N)/(math.factorial(self.__N-k))
        else:
            print("k non puo essere maggiore di n nelle disposizione semplici")

    def nDispSemplConRip(self, k):
        return self.__N**k

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

    """COMBINAZIONI"""

    def nCombSemplSenzaRip(self, k):
        
        return math.factorial(self.__N) / (math.factorial(k) * (math.factorial(self.__N-k)))

    def nCombSemplConRip(self, k):

        return math.factorial(self.__N+k-1) / (math.factorial(k) * (math.factorial(self.__N-1)))

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

prova = calcComb("matematica")
prova.nPermutConRip()
print(prova.nPermutConRip())
