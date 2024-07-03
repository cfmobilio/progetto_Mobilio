from datetime import datetime, timedelta
# Non importiamo più logging

from funzionalità.menù import Menu
from funzionalità.notifiche import Notifiche
from funzionalità.scorte import Scorte
from utenti.amministratore import Amministratore
from utenti.studente import Studente
from funzionalità.abbonamento import Abbonamento


class SistemaMensa:
    def __init__(self):
        self.utenti = []
        self.menu = Menu()
        self.scorte = Scorte()
        self.prenotazioni = []
        self.pagamenti = []
        self.notifiche = Notifiche()
        self.abbonamenti = []
        self.carica_utenti_da_file()

    def carica_utenti_da_file(self):
        try:
            with open('../utenti.txt', 'r') as file:
                for line in file:
                    fields = line.strip().split(',')
                    if fields[0] == 'Studente':
                        nuovo_utente = Studente(id=None, nome=fields[1], cognome=fields[2], email=fields[3],
                                                password=fields[4], numero_matricola=fields[5],
                                                borsellino=int(fields[6]))
                        self.utenti.append(nuovo_utente)
                    elif fields[0] == 'Amministratore':
                        nuovo_utente = Amministratore(id=None, nome=fields[1], cognome=fields[2], email=fields[3],
                                                      password=fields[4])
                        self.utenti.append(nuovo_utente)
        except FileNotFoundError:
            pass
        except Exception:
            pass

    def esiste_utente(self, email):
        return any(utente.email == email for utente in self.utenti)

    def registra_studente(self, studente):
        if not self.esiste_utente(studente.email):
            self.utenti.append(studente)
            self.aggiorna_utenti_file()

    def registra_amministratore(self, amministratore):
        if not self.esiste_utente(amministratore.email):
            self.utenti.append(amministratore)
            self.aggiorna_utenti_file()

    def aggiorna_utenti_file(self):
        try:
            with open('../utenti.txt', 'w') as file:
                for utente in self.utenti:
                    if isinstance(utente, Studente):
                        file.write(f"Studente,{utente.nome},{utente.cognome},{utente.email},{utente.password},"
                                   f"{utente.numero_matricola},{utente.borsellino}\n")
                    elif isinstance(utente, Amministratore):
                        file.write(f"Amministratore,{utente.nome},{utente.cognome},{utente.email},{utente.password}\n")
        except Exception:
            pass

    def login(self, email, password):
        for utente in self.utenti:
            if utente.email == email and utente.verifica_password(password):
                return utente
        return None

    def effettua_pagamento(self, studente_id, importo):
        studente = self.get_utente_by_id(studente_id)
        if studente:
            studente.effettua_pagamento(importo)
            self.pagamenti.append((studente_id, importo))
            return f"Pagamento di {importo}€ effettuato con successo"
        return "Errore durante il pagamento"

    def sottoscrivi_abbonamento(self, studente, abbonamento):
        studente.sottoscrivi_abbonamento(abbonamento)
        self.abbonamenti.append((studente.id, abbonamento))

    def get_abbonamenti_sottoscritti(self, studente):
        abbonamenti_sottoscritti = []
        for abbonamento in self.abbonamenti:
            if abbonamento[0] == studente.id:
                abbonamenti_sottoscritti.append(abbonamento[1])
        return abbonamenti_sottoscritti

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

    def richiedi_reimpostazione_password(self, email):
        email_lower = email.lower()
        for utente in self.utenti:
            if utente.email.lower() == email_lower:
                try:
                    return "Email di reimpostazione password inviata con successo."
                except Exception:
                    return "Errore durante l'invio dell'email di reimpostazione password."
        return "L'indirizzo email non è registrato."
