from PyQt5.QtWidgets import QDialog, QFormLayout, QPushButton, QLineEdit, QMessageBox
import re


class PasswordDimenticataDialog(QDialog):
    def __init__(self, sistema_mensa, parent=None):
        super(PasswordDimenticataDialog, self).__init__(parent)
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Password dimenticata')
        layout = QFormLayout()

        self.email_input = QLineEdit()
        layout.addRow('Email:', self.email_input)

        self.submit_button = QPushButton('Invia')
        self.submit_button.clicked.connect(self.invia_richiesta)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def invia_richiesta(self):
        email = self.email_input.text().strip()
        if not email:
            QMessageBox.warning(self, 'Errore', 'Inserisci un indirizzo email')
            return

        if not self.valida_email(email):
            QMessageBox.warning(self, 'Errore', 'Inserisci un indirizzo email valido')
            return

        risultato = self.sistema_mensa.richiedi_reimpostazione_password(email)
        QMessageBox.information(self, 'Richiesta inviata', risultato)
        self.accept()

    def valida_email(self, email):
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(regex, email) is not None
