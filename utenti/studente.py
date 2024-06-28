from utenti.utente import Utente
from funzionalità.prenotazione import Prenotazione


class Studente(Utente):
    def __init__(self, id, nome, cognome, email, password, numero_matricola):
        super().__init__(id, nome, cognome, email, password)
        self.notifiche = None
        self.numero_matricola = numero_matricola
        self.prenotazioni = []
        self.abbonamenti = []

    def prenota_pasto(self, pasto):
        prenotazione = Prenotazione(self, pasto)
        self.prenotazioni.append(prenotazione)
        return f"Pasto {pasto.nome} prenotato per {self.nome} {self.cognome}"

    def effettua_pagamento(self, importo):
        return f"Pagamento di {importo} euro effettuato da {self.nome} {self.cognome}"

    def visualizza_notifiche(self):
        return [notifica.get_info() for notifica in self.notifiche]

    def sottoscrivi_abbonamento(self, abbonamento):
        self.abbonamenti.append(abbonamento)
        return f"Abbonamento {abbonamento} sottoscritto"

    def get_info(self):
        # Metodo per ottenere informazioni sullo studente
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "email": self.email,
            "numero_matricola": self.numero_matricola
        }
