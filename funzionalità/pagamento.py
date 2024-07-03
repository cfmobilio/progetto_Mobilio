from PyQt5.QtWidgets import QMessageBox
from datetime import datetime


class Pagamento:
    def __init__(self, nome, cognome, numero_carta, mese_scadenza, anno_scadenza,
                 cvv, importo, studente, sistema_mensa, view):
        self.nome = nome
        self.cognome = cognome
        self.numero_carta = numero_carta
        self.mese_scadenza = mese_scadenza
        self.anno_scadenza = anno_scadenza
        self.cvv = cvv
        self.importo = importo
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.view = view

    def effettua_pagamento(self):
        if self.validate_inputs():
            try:
                importo_float = float(self.importo)
                # Simulazione del pagamento (qui sostituire con la logica reale)
                self.studente.ricarica_borsellino(importo_float)
                self.sistema_mensa.effettua_pagamento(self.studente, importo_float)
                QMessageBox.information(self.view, "Pagamento", f"Pagamento effettuato con successo!")
                self.view.saldo_label.setText(f"Saldo borsellino virtuale: {self.studente.get_info()['borsellino']} €")
            except ValueError as ve:
                self.show_error("Errore", f"Importo non valido: {str(ve)}")
            except Exception as e:
                self.show_error("Errore", f"Errore durante il pagamento: {str(e)}")
        else:
            self.show_error("Errore", "Per favore, completa tutti i campi correttamente.")

    def validate_inputs(self):
        if (not self.nome or not self.cognome or not self.numero_carta
                or not self.mese_scadenza or not self.anno_scadenza
                or not self.cvv or not self.importo):
            return False

        if not self.valida_carta_credito():
            return False

        if not self.valida_data_scadenza():
            return False

        if not self.valida_cvv():
            return False

        try:
            float(self.importo)
        except ValueError:
            return False

        return True

    def valida_carta_credito(self):
        if not self.numero_carta.isdigit() or len(self.numero_carta) != 16:
            self.show_error("Errore", "Il numero di carta deve essere composto da 16 cifre.")
            return False
        return True

    def valida_data_scadenza(self):
        try:
            mese_int = int(self.mese_scadenza)
            anno_int = int(self.anno_scadenza)
            oggi = datetime.now()
            scadenza = datetime(year=anno_int, month=mese_int, day=1)
            if scadenza <= oggi:
                self.show_error("Errore", "La carta è scaduta.")
                return False
            return True
        except ValueError:
            self.show_error("Errore", "La data di scadenza della carta non è valida.")
            return False

    def valida_cvv(self):
        if not self.cvv.isdigit() or not (len(self.cvv) == 3 or len(self.cvv) == 4):
            self.show_error("Errore", "Il CVV deve essere composto da 3 o 4 cifre.")
            return False
        return True

    def show_error(self, title, message):
        QMessageBox.warning(self.view, title, message)
