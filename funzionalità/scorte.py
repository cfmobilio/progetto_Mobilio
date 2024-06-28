import os
import pickle
import logging


class Scorte:
    def __init__(self):
        self.scorte = []
        self.carica_scorte_da_file()

    # Carica le scorte da un file
    def carica_scorte_da_file(self, nome_file="scorte.pickle"):
        if os.path.isfile(nome_file):
            with open(nome_file, 'rb') as f:
                self.scorte = pickle.load(f)
            logging.debug(f"Loaded scorte from file: {self.scorte}")
        else:
            logging.debug(f"File {nome_file} does not exist. No scorte loaded.")

    # Salva le scorte su file
    def salva_scorte(self, nome_file="scorte.pickle"):
        with open(nome_file, 'wb') as f:
            pickle.dump(self.scorte, f)

    # Aggiunge una scorta
    def aggiungi_scorta(self, ingrediente, quantita):
        scorta = {'ingrediente': ingrediente, 'quantita': quantita}
        self.scorte.append(scorta)
        self.salva_scorte()

    # Restituisce le scorte
    def get_scorte(self):
        return self.scorte
