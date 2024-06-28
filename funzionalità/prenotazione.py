import datetime


class Prenotazione:
    def __init__(self, studente, pasto):
        self.studente = studente
        self.pasto = pasto
        self.data_prenotazione = datetime.datetime.now()

    # Restituisce le informazioni della prenotazione
    def get_info(self):
        return {
            "studente": self.studente.get_info(),
            "pasto": self.pasto.get_info(),
            "data_prenotazione": self.data_prenotazione.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return (f"Prenotazione di {self.pasto.nome} "
                f"per lo studente {self.studente.nome} {self.studente.cognome} il {self.data_prenotazione}")
