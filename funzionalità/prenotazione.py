from PyQt5.QtWidgets import QMessageBox
from datetime import datetime


class Prenotazione:
    def __init__(self, studente, pasto, data_prenotazione=None):
        self.studente = studente
        self.pasto = pasto
        self.data_prenotazione = data_prenotazione if data_prenotazione else datetime.now()

    def get_info(self):
        return {
            "studente": self.studente.get_info(),
            "pasto": self.pasto,
            "data_prenotazione": self.data_prenotazione.strftime("%Y-%m-%d %H:%M:%S")
        }

    def prenota_pasto(self, view, pasto, giorno, mensa):
        try:
            self.studente.aggiungi_prenotazione(self)
            QMessageBox.information(view, "Prenotazione", f"Prenotazione per {pasto} di {giorno} "
                                                          f"presso {mensa} avvenuta con successo.")
            view.update_prenotazioni_list()
        except Exception as e:
            print(f"Errore durante la prenotazione pasto: {str(e)}")
            QMessageBox.critical(view, "Errore", f"Errore durante la prenotazione pasto: {str(e)}")

    def disdici_prenotazione(self, view):
        try:
            self.studente.rimuovi_prenotazione(self)
            QMessageBox.information(view, "Prenotazione Disdetta", "Prenotazione disdetta con successo.")
            view.update_prenotazioni_list()
        except Exception as e:
            print(f"Errore durante la disdetta della prenotazione: {str(e)}")
            QMessageBox.critical(view, "Errore", f"Errore durante la disdetta della prenotazione: {str(e)}")

    def __str__(self):
        return f"Prenotazione per {self.pasto} effettuata il {self.data_prenotazione.strftime('%Y-%m-%d %H:%M:%S')}"
