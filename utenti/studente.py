from utenti.utente import Utente  # Assumo che Utente sia definito in utenti/utente.py
from funzionalità.prenotazione import Prenotazione


class Studente(Utente):
    def __init__(self, id, nome, cognome, email, password, numero_matricola, borsellino=0):
        super().__init__(id, nome, cognome, email, password)
        self.notifiche = []
        self.numero_matricola = numero_matricola
        self.prenotazioni = []
        self.abbonamenti = []
        self.borsellino = borsellino

    def prenota_pasto(self, pasto):
        prenotazione = Prenotazione(self, pasto)
        self.aggiungi_prenotazione(prenotazione)  # Chiamiamo il metodo aggiungi_prenotazione
        return f"Pasto {pasto.nome} prenotato per {self.nome} {self.cognome}"

    def aggiungi_prenotazione(self, prenotazione):
        self.prenotazioni.append(prenotazione)

    def rimuovi_prenotazione(self, prenotazione):
        if prenotazione in self.prenotazioni:
            self.prenotazioni.remove(prenotazione)
        else:
            raise ValueError("La prenotazione specificata non è presente nelle prenotazioni dello studente.")

    def effettua_pagamento(self, importo):
        if self.borsellino >= importo:
            self.borsellino -= importo
            return f"Pagamento di {importo} euro effettuato da {self.nome} {self.cognome}"
        else:
            return "Saldo insufficiente"

    def ricarica_borsellino(self, importo):
        self.borsellino += importo
        return f"Borsellino ricaricato di {importo} euro. Saldo attuale: {self.borsellino} euro"

    def visualizza_notifiche(self):
        return [notifica.get_info() for notifica in self.notifiche]

    def sottoscrivi_abbonamento(self, abbonamento):
        self.abbonamenti.append(abbonamento)
        return f"Abbonamento {abbonamento} sottoscritto"

    def get_info(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "email": self.email,
            "numero_matricola": self.numero_matricola,
            "borsellino": self.borsellino
        }
