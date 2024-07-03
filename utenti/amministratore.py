from utenti.utente import Utente  # Assumo che Utente sia definito in utenti/utente.py
from funzionalità.menù import Menu
from funzionalità.prenotazione import Prenotazione


class Amministratore(Utente):
    def __init__(self, id, nome, cognome, email, password):
        super().__init__(id, nome, cognome, email, password)
        self.menu = Menu()  # Utilizza la classe Menu per gestire il menu
        self.scorte = {}
        self.prenotazioni = []
        self.abbonamenti = []

    def aggiorna_scorte(self, ingrediente, quantita, unita):
        if ingrediente in self.scorte:
            self.scorte[ingrediente]['quantita'] += quantita
        else:
            self.scorte[ingrediente] = {'quantita': quantita, 'unita': unita}
        return f"Scorte di {ingrediente} aggiornate a {self.scorte[ingrediente]['quantita']} {unita}"

    def gestisci_menu(self, nuovo_menu):
        for pasto in nuovo_menu:
            self.menu.aggiungi_pasto(pasto)
        return f"Menu aggiornato con {len(nuovo_menu)} piatti."

    def visualizza_report(self):
        return {
            "prenotazioni_totali": len(self.prenotazioni),
            "scorte": self.visualizza_report_scorte(),
            "abbonamenti_attivi": self.visualizza_report_abbonamenti()
        }

    def visualizza_report_prenotazioni(self):
        return {"prenotazioni_totali": len(self.prenotazioni)}

    def visualizza_report_scorte(self):
        return {ingrediente: f"{dati['quantita']} {dati['unita']}" for ingrediente, dati in self.scorte.items()}

    def visualizza_report_abbonamenti(self):
        return {"abbonamenti_attivi": len([abb for abb in self.abbonamenti if not abb.verifica_scaduto()])}

    def invia_notifiche(self, messaggio, destinatari):
        for destinatario in destinatari:
            destinatario.ricevi_notifica(messaggio)
        with open("notifiche.txt", "a") as file:
            file.write(f"{messaggio}\n")

    def get_info(self):
        return {"id": self.id, "nome": self.nome, "cognome": self.cognome, "email": self.email}
