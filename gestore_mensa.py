import logging
from funzionalità.menù import Menu
from funzionalità.notifiche import Notifiche
from funzionalità.scorte import Scorte


class SistemaMensa:
    def __init__(self):
        logging.debug("Creazione istanza SistemaMensa")
        self.utenti = []
        self.menu = Menu()
        self.scorte = Scorte()
        self.prenotazioni = []
        self.pagamenti = []
        self.notifiche = Notifiche()

    def esiste_utente(self, email):
        logging.debug(f"Verifica esistenza utente per email: {email}")
        for utente in self.utenti:
            if utente.email == email:
                logging.debug(f"Utente trovato per email: {email}")
                return True
        logging.debug(f"Nessun utente trovato per email: {email}")
        return False

    def registra_studente(self, studente):
        logging.debug(f"Registrazione studente: {studente.get_info()}")
        self.utenti.append(studente)

    def registra_amministratore(self, amministratore):
        logging.debug(f"Registrazione amministratore: {amministratore.get_info()}")
        self.utenti.append(amministratore)

    def login(self, email, password):
        logging.debug(f"Tentativo di login per email: {email}")
        for utente in self.utenti:
            if utente.email == email and utente.verifica_password(password):
                logging.debug(f"Login riuscito per email: {email}")
                return utente
        logging.debug(f"Login fallito per email: {email}")
        return None

    def effettua_pagamento(self, studente_id, importo):
        logging.debug(f"Tentativo di pagamento di {importo}€ per studente {studente_id}")
        studente = self.get_utente_by_id(studente_id)
        if studente:
            studente.effettua_pagamento(importo)
            self.pagamenti.append((studente_id, importo))
            logging.debug(f"Pagamento di {importo}€ riuscito per studente {studente_id}")
            return f"Pagamento di {importo}€ effettuato con successo"
        logging.debug(f"Pagamento di {importo}€ fallito per studente {studente_id}")
        return "Errore durante il pagamento"

    def get_utente_by_id(self, utente_id):
        for utente in self.utenti:
            if utente.id == utente_id:
                return utente
        return None

    def get_menu(self):
        return self.menu.get_menu_items()

    def get_scorte(self):
        return self.scorte.get_scorte()

    def get_notifiche(self):
        return self.notifiche
