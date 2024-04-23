import copy

from database import meteo_dao
from datetime import datetime

class Model:
    def __init__(self):
        self.percorsi=[]
        pass


    def calcola_um_media(self,mese):
        risultato={}

        situazioni = meteo_dao.MeteoDao().get_all_situazioni()

        for i in situazioni:

            if i.data.month == mese:

                if risultato.__contains__(i.localita):
                    a=risultato[i.localita][0]
                    a += i.umidita
                    risultato[i.localita][0]=a

                    b = risultato[i.localita][1]
                    b += 1
                    risultato[i.localita][1] = b

                else:
                    risultato[i.localita]=[i.umidita,1]

        return risultato

    def calcola_percorso(self,mese):
        situazioni = meteo_dao.MeteoDao().get_all_situazioni()

        for i in situazioni:
            if i.data.day>15 or i.data.month!=mese:
                situazioni.remove(i)
        self.ricorsione([],situazioni)
        a=0
        return a


    def ricorsione(self,percorso,situazioni_rimanenti):
        if len(situazioni_rimanenti)==0 or len(percorso)==15:
            self.percorsi.append(copy.deepcopy(percorso))



        for i in range(len(situazioni_rimanenti)):
            percorso.append(situazioni_rimanenti[i])
            nuove_situazioni_rimanenti = situazioni_rimanenti[:i]+situazioni_rimanenti[i+1:]
            self.ricorsione(percorso,nuove_situazioni_rimanenti)
            percorso.pop()






