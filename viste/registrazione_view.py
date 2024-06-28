import logging
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtCore import pyqtSignal

from utenti.amministratore import Amministratore
from utenti.studente import Studente


class RegistrazioneView(QWidget):
    registrazione_completata = pyqtSignal()

    def __init__(self, sistema_mensa, parent=None):
        super().__init__(parent)
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.nome_label = QLabel('Nome:')
        layout.addWidget(self.nome_label)
        self.nome_input = QLineEdit()
        layout.addWidget(self.nome_input)

        self.cognome_label = QLabel('Cognome:')
        layout.addWidget(self.cognome_label)
        self.cognome_input = QLineEdit()
        layout.addWidget(self.cognome_input)

        self.email_label = QLabel('Email:')
        layout.addWidget(self.email_label)
        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        self.password_label = QLabel('Password:')
        layout.addWidget(self.password_label)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.tipo_utente_label = QLabel('Tipo Utente:')
        layout.addWidget(self.tipo_utente_label)
        self.tipo_utente_combobox = QComboBox()
        self.tipo_utente_combobox.addItems(["Studente", "Amministratore"])
        layout.addWidget(self.tipo_utente_combobox)

        self.matricola_label = QLabel('Numero Matricola:')
        layout.addWidget(self.matricola_label)
        self.matricola_input = QLineEdit()
        layout.addWidget(self.matricola_input)

        self.registra_button = QPushButton('Registra')
        self.registra_button.clicked.connect(self.registra)
        layout.addWidget(self.registra_button)

        self.setLayout(layout)

    def registra(self):
        nome = self.nome_input.text()
        cognome = self.cognome_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        tipo_utente = self.tipo_utente_combobox.currentText()
        numero_matricola = self.matricola_input.text() if tipo_utente == 'Studente' else None

        logging.debug(f"Registrazione tentata: {nome} {cognome} ({email}), Tipo: {tipo_utente}")

        if not nome or not cognome or not email or not password:
            logging.warning("Errore di registrazione: campi non completi")
            return "Errore: tutti i campi sono obbligatori"

        if self.sistema_mensa.esiste_utente(email):
            logging.warning(f"Errore di registrazione: utente già esistente per email {email}")
            return "Errore: l'utente esiste già"

        try:
            if tipo_utente == 'Studente':
                logging.debug("Creazione di un nuovo studente")
                nuovo_utente = Studente(id=None, nome=nome, cognome=cognome, email=email,
                                        password=password, numero_matricola=numero_matricola)
                self.sistema_mensa.registra_studente(nuovo_utente)
            elif tipo_utente == 'Amministratore':
                logging.debug("Creazione di un nuovo amministratore")
                nuovo_utente = Amministratore(id=None, nome=nome, cognome=cognome, email=email, password=password)
                self.sistema_mensa.registra_amministratore(nuovo_utente)
            else:
                logging.warning(f"Errore di registrazione: tipo utente non valido {tipo_utente}")
                return "Errore: tipo utente non valido"

            logging.debug(f"Registrazione completata per {tipo_utente} {nome} {cognome} ({email})")
            self.registrazione_completata.emit()
            return "Registrazione completata con successo"
        except Exception as e:
            logging.error(f"Errore durante la registrazione: {e}")
            return "Errore durante la registrazione"
