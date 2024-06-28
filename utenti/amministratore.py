from utenti.utente import Utente


class Amministratore(Utente):

    def __init__(self, id, nome, cognome, email, password):
        super().__init__(id, nome, cognome, email, password)
        self.menu = []
        self.scorte = {}
        self.prenotazioni = []
        self.abbonamenti = []

    def gestisci_menu(self, nuovo_menu):
        # Logica per gestire il menu
        self.menu = nuovo_menu
        return "Menu aggiornato"

    def aggiorna_scorte(self, ingrediente, quantita):
        # Logica per aggiornare le scorte
        if ingrediente in self.scorte:
            self.scorte[ingrediente] += quantita
        else:
            self.scorte[ingrediente] = quantita
        return f"Scorte di {ingrediente} aggiornate a {self.scorte[ingrediente]}"

    def visualizza_report(self):
        # Logica per generare e visualizzare report generico
        report = {
            "prenotazioni_totali": len(self.prenotazioni),
            "scorte": self.scorte,
            "abbonamenti_attivi": len([abb for abb in self.abbonamenti if not abb.verifica_scaduto()])
        }
        return report

    def visualizza_report_prenotazioni(self):
        prenotazioni_totali = len(self.prenotazioni)
        return {
            "prenotazioni_totali": prenotazioni_totali
        }

    def visualizza_report_scorte(self):
        scorte = self.scorte
        return {
            "scorte": scorte
        }

    # Metodo per visualizzare i report
    def visualizza_report_abbonamenti(self):
        abbonamenti_attivi = len([abb for abb in self.abbonamenti if not abb.verifica_scaduto()])
        return {
            "abbonamenti_attivi": abbonamenti_attivi
        }

    # Metodo per inviare le notifiche a chi specificato
    def invia_notifiche(self, messaggio, destinatari):
        for destinatario in destinatari:
            destinatario.ricevi_notifica(messaggio)
        # Salva il messaggio nel file delle notifiche
        with open("notifiche.txt", "a") as file:
            file.write(f"{messaggio}\n")

    # Metodo per ottenere informazioni sull'amministratore
    def get_info(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "email": self.email
        }
