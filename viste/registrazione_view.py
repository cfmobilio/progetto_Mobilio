from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
import re
from utenti.amministratore import Amministratore
from utenti.studente import Studente


class RegistrazioneView(QWidget):
    registrazione_completata = pyqtSignal()

    def __init__(self, sistema_mensa, parent=None):
        super().__init__(parent)
        self.sistema_mensa = sistema_mensa
        self.init_ui()
        self.is_registered = False

    def init_ui(self):
        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
            }
            QLineEdit {
                font-size: 16px;
                padding: 10px;
                border: 2px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px;
                background-color: #FF0000;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton#forgot_password {
                background-color: transparent;
                color: #e74c3c;
                text-align: left;
            }
                """)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.setWindowTitle('MangiAmo')
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

        self.torna_button = QPushButton('Torna indietro')
        self.torna_button.clicked.connect(self.torna_indietro)
        layout.addWidget(self.torna_button)

        self.setLayout(layout)

    def valida_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    def valida_password(self, password):
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
        return re.match(pattern, password)

    def registra(self):
        if self.is_registered:
            self.mostra_messaggio("Errore", "Registrazione già effettuata")
            return

        nome = self.nome_input.text()
        cognome = self.cognome_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        tipo_utente = self.tipo_utente_combobox.currentText()
        numero_matricola = self.matricola_input.text() if tipo_utente == 'Studente' else None

        if not nome or not cognome or not email or not password:
            self.mostra_messaggio("Errore", "Tutti i campi sono obbligatori")
            return

        if not self.valida_email(email):
            self.mostra_messaggio("Errore", "Formato email non valido")
            return

        if not self.valida_password(password):
            self.mostra_messaggio("Errore",
                                  "La password deve contenere almeno 8 caratteri, "
                                  "un numero, una lettera maiuscola e un carattere speciale")
            return

        if self.sistema_mensa.esiste_utente(email):
            self.mostra_messaggio("Errore", "L'utente esiste già")
            return

        try:
            if tipo_utente == 'Studente':
                nuovo_utente = Studente(id=None, nome=nome, cognome=cognome, email=email,
                                        password=password, numero_matricola=numero_matricola)
                self.sistema_mensa.registra_studente(nuovo_utente)
            elif tipo_utente == 'Amministratore':
                nuovo_utente = Amministratore(id=None, nome=nome, cognome=cognome, email=email, password=password)
                self.sistema_mensa.registra_amministratore(nuovo_utente)
            else:
                self.mostra_messaggio("Errore", "Tipo utente non valido")
                return

            self.mostra_messaggio("Successo", "Registrazione completata con successo")
            self.registrazione_completata.emit()
            self.is_registered = True
        except Exception as e:
            self.mostra_messaggio("Errore", f"Errore durante la registrazione: {e}")

    def mostra_messaggio(self, titolo, messaggio):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(titolo)
        msg_box.setText(messaggio)
        msg_box.exec_()

    def torna_indietro(self):
        self.parentWidget().setCurrentIndex(0)
