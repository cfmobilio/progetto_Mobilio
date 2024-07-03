from PyQt5.QtWidgets import QMessageBox
from datetime import datetime, timedelta
import os
import pickle
from funzionalità.pagamento import Pagamento


class Abbonamento:
    def __init__(self, codice=None, data_inizio=None, data_rilascio=None, data_scadenza=None):
        self.codice = codice
        self.data_inizio = data_inizio
        self.data_rilascio = data_rilascio
        self.data_scadenza = data_scadenza

    @staticmethod
    def carica_abbonamenti_salvati():
        lista_abbonamenti_salvata = []
        if os.path.isfile('Dati/abbonamenti.pickle'):
            with open('Dati/abbonamenti.pickle', 'rb') as f:
                lista_abbonamenti_salvata = pickle.load(f)
        return lista_abbonamenti_salvata

    @staticmethod
    def salva_abbonamenti(lista):
        with open('Dati/abbonamenti.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def aggiungi_abbonamento(self, codice, data_inizio, data_rilascio, data_scadenza):
        self.codice = codice
        self.data_inizio = data_inizio
        self.data_rilascio = data_rilascio
        self.data_scadenza = data_scadenza

        lista_abbonamenti_salvata = Abbonamento.carica_abbonamenti_salvati()
        lista_abbonamenti_salvata.append(self.get_info())
        Abbonamento.salva_abbonamenti(lista_abbonamenti_salvata)

    def verifica_scaduto(self):
        return datetime.now() > self.data_scadenza

    @staticmethod
    def acquista_abbonamento(view, studente, sistema_mensa, tipo_abbonamento, costo):
        try:
            saldo_borsellino = studente.get_info()["borsellino"]

            if saldo_borsellino < costo:
                QMessageBox.critical(view, "Saldo Insufficiente",
                                     f"Saldo insufficiente per acquistare l'abbonamento {tipo_abbonamento}.")
                return

            data_inizio = datetime.now()
            data_scadenza = data_inizio + timedelta(days=30)  # Per il mensile, impostiamo 30 giorni di validità
            codice = f"{tipo_abbonamento}_{studente.get_info()['id']}_{data_inizio.strftime('%Y%m%d')}"
            abbonamento = Abbonamento(codice, data_inizio, data_inizio, data_scadenza)

            pagamento = Pagamento(studente.get_info()['nome'], studente.get_info()['cognome'],
                                  '1234567812345678', '12', '2024', '123', costo,
                                  studente, sistema_mensa, view)
            pagamento.effettua_pagamento()

            sistema_mensa.sottoscrivi_abbonamento(studente, abbonamento)

            if tipo_abbonamento == 'mensile':
                message = 'Abbonamento mensile acquistato valido per 30 giorni'
            else:
                message = f'Abbonamento {tipo_abbonamento} acquistato'

            QMessageBox.information(view, "Transazione Riuscita", message)
            Abbonamento.update_abbonamenti_view(view, studente)
        except Exception as e:
            print(f"Errore durante l'acquisto dell'abbonamento: {str(e)}")
            QMessageBox.critical(view, "Transazione Fallita", f'Errore durante l\'acquisto dell\'abbonamento: {str(e)}')

    @staticmethod
    def update_abbonamenti_view(view, studente):
        abbonamenti = studente.abbonamenti
        if abbonamenti:
            abbonamenti_info = "\n\n".join([abbonamento.get_info() for abbonamento in abbonamenti])
            view.abbonamenti_sottoscritti_text.setPlainText(abbonamenti_info)
        else:
            view.abbonamenti_sottoscritti_text.setPlainText("Nessun abbonamento sottoscritto")

    def get_info(self):
        if self.codice.startswith("15 pasti"):
            return f"Abbonamento per 15 pasti emesso il {self.data_rilascio.strftime('%d/%m/%Y')}"
        elif self.codice.startswith("mensile"):
            return (f"Abbonamento mensile valido dal {self.data_inizio.strftime('%d/%m/%Y')} "
                    f"al {self.data_scadenza.strftime('%d/%m/%Y')}")
        else:
            return "Descrizione non disponibile"
