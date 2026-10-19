import csv
from stand import Standard, Premium, Prese
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.lista_e = []
        self.lista_s = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def __str__(self):
        return f"{self.__nome}, {self.lista_e}, {self.lista_s}"

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            for riga in csv_reader:
                if not riga:
                    continue
                if riga[0][0] == "S":
                    if len(riga) == 4:
                        s=Standard(riga[0],riga[1],riga[2],riga[3])
                    else:
                        if riga[4].isdigit():
                            s = Prese(riga[0],riga[1],riga[2],riga[3],riga[4])
                        else:
                            s=Premium(riga[0],riga[1],riga[2],riga[3],riga[4])
                    self.lista_s.append(s)
                else:
                    e = Espositore(riga[0],riga[1], riga[2])
                    self.lista_e.append(e)


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_selezionato = None
        for s in self.lista_s:
            if s.codice==codice_stand:
                stand_selezionato = s
                break
        esp_selezionato = None
        for e in self.lista_e:
            if e.codice==codice_espositore:
                esp_selezionato = e
                break
        if stand_selezionato is None or esp_selezionato is None:
            raise ValueError("Stand o espositore non esistente.")
        if stand_selezionato.espositore is not None:
            raise ValueError("Lo stand e gia occupato.")
        if esp_selezionato.stand is not None:
            raise ValueError("L'espositore ha gia uno stand assegnato.")
        else:
            stand_selezionato.espositore = esp_selezionato
            esp_selezionato.stand = stand_selezionato

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for e in self.lista_e:
            print(e)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.lista_s)
