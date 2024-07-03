import sys
import os
import pickle
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QMessageBox, QListWidget
from funzionalità.prenotazione import Prenotazione


class PrenotazioneView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(PrenotazioneView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MangiAmo')
        layout = QVBoxLayout()

        self.setStyleSheet("""
                QLabel {
                    font-size: 20px;
                    font-weight: normal;
                    color: black;
                }
                QPushButton {
                    font-size: 16px;
                    padding: 10px 20px;
                    background-color: #FF0000;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    min-width: 150px;
                    min-height: 40px;
                }
                QPushButton:hover {
                    background-color: #c0392b;
                }
                """)

        self.giorno_label = QLabel('Seleziona giorno:')
        layout.addWidget(self.giorno_label)
        self.giorno_combo = QComboBox()
        self.giorno_combo.addItems(["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"])
        layout.addWidget(self.giorno_combo)

        self.mensa_label = QLabel('Seleziona Mensa:')
        layout.addWidget(self.mensa_label)
        self.mensa_combo = QComboBox()
        self.mensa_combo.addItems(["Gusti universitari", "Mensa del sapere",
                                   "Mensa della Conoscenza", "Sapore Accademico"])
        layout.addWidget(self.mensa_combo)

        self.pasto_label = QLabel('Seleziona Pasto:')
        layout.addWidget(self.pasto_label)
        self.pasto_combo = QComboBox()
        self.pasto_combo.addItems(["Pranzo", "Cena"])
        layout.addWidget(self.pasto_combo)

        self.prenota_button = QPushButton('Prenota ora')
        self.prenota_button.clicked.connect(lambda: self.prenota_pasto())
        layout.addWidget(self.prenota_button)

        self.disdici_prenotazione_label = QLabel('Prenotazioni Effettuate:')
        layout.addWidget(self.disdici_prenotazione_label)

        self.prenotazioni_list = QListWidget()
        layout.addWidget(self.prenotazioni_list)

        self.disdici_button = QPushButton('Disdici Prenotazione')
        self.disdici_button.clicked.connect(lambda: self.disdici_prenotazione())
        layout.addWidget(self.disdici_button)

        self.setLayout(layout)
        self.update_prenotazioni_list()

    def prenota_pasto(self):
        giorno = self.giorno_combo.currentText()
        mensa = self.mensa_combo.currentText()
        pasto = self.pasto_combo.currentText()

        nuova_prenotazione = Prenotazione(self.studente, {giorno, mensa, pasto})
        nuova_prenotazione.prenota_pasto(self, pasto, giorno, mensa)

    def disdici_prenotazione(self):
        selected_item = self.prenotazioni_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Errore", "Seleziona una prenotazione da disdire.")
            return

        prenotazione_text = selected_item.text()
        for prenotazione in self.studente.prenotazioni:
            if str(prenotazione) == prenotazione_text:
                prenotazione.disdici_prenotazione(self)
                break

    def update_prenotazioni_list(self):
        self.prenotazioni_list.clear()
        for prenotazione in self.studente.prenotazioni:
            self.prenotazioni_list.addItem(str(prenotazione))
