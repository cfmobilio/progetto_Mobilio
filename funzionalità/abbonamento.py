import os
import pickle
from datetime import datetime


class Abbonamento:
    def __init__(self, codice=None, data_inizio=None, data_rilascio=None, data_scadenza=None, stagionale=None):
        self.codice = codice
        self.data_inizio = data_inizio
        self.data_rilascio = data_rilascio
        self.data_scadenza = data_scadenza
        self.stagionale = stagionale

    # Carica la lista degli abbonamenti salvati
    def carica_abbonamenti_salvati(self):
        lista_abbonamenti_salvata = []
        if os.path.isfile('Dati/abbonamenti.pickle'):
            with open('Dati/abbonamenti.pickle', 'rb') as f:
                lista_abbonamenti_salvata = pickle.load(f)
        return lista_abbonamenti_salvata

    # Salva la lista degli abbonamenti su file
    def salva_abbonamenti(self, lista):
        with open('Dati/abbonamenti.pickle', 'wb') as f:
            pickle.dump(lista, f)

    # Aggiunge un nuovo abbonamento
    def aggiungi_abbonamento(self, codice, data_inizio, data_rilascio, data_scadenza, stagionale):
        self.codice = codice
        self.data_inizio = data_inizio
        self.data_rilascio = data_rilascio
        self.data_scadenza = data_scadenza
        self.stagionale = stagionale

        lista_abbonamenti_salvata = self.carica_abbonamenti_salvati()
        lista_abbonamenti_salvata.append(self.get_info_abbonamento())
        self.salva_abbonamenti(lista_abbonamenti_salvata)

    # Restituisce le informazioni dell'abbonamento corrente
    def get_info_abbonamento(self):
        return {
            "codice": self.codice,
            "data_inizio": self.data_inizio,
            "data_rilascio": self.data_rilascio,
            "data_scadenza": self.data_scadenza,
            "stagionale": self.stagionale
        }

    # Crea un oggetto Abbonamento da un dizionario
    def da_dict(self, dizionario_abbonamento):
        return Abbonamento(dizionario_abbonamento["codice"],
                           dizionario_abbonamento["data_inizio"],
                           dizionario_abbonamento["data_rilascio"],
                           dizionario_abbonamento["data_scadenza"],
                           dizionario_abbonamento["stagionale"])

    # Ricerca un abbonamento per codice
    def ricerca_abbonamento(self, codice):
        lista_abbonamenti_salvata = self.carica_abbonamenti_salvati()
        for abbonamento in lista_abbonamenti_salvata:
            if abbonamento["codice"] == codice:
                return self.da_dict(abbonamento)
        return None

    # Rimuove l'abbonamento corrente
    def rimuovi_abbonamento(self):
        lista_abbonamenti_salvata = self.carica_abbonamenti_salvati()
        for abbonamento in lista_abbonamenti_salvata:
            if abbonamento["codice"] == self.codice:
                lista_abbonamenti_salvata.remove(abbonamento)
                break
        self.salva_abbonamenti(lista_abbonamenti_salvata)
        self.codice = None
        self.data_inizio = None
        self.data_rilascio = None
        self.data_scadenza = None
        self.stagionale = None
        del self

    # Verifica se l'abbonamento è scaduto
    def verifica_scaduto(self):
        return datetime.now() > self.data_scadenza
