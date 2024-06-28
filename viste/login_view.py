from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox

from utenti.amministratore import Amministratore
from utenti.studente import Studente
from viste.password_view import PasswordDimenticataDialog


class LoginView(QWidget):
    def __init__(self, sistema_mensa, parent=None):
        super(LoginView, self).__init__(parent)
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.email_label = QLabel('Email:')
        layout.addWidget(self.email_label)

        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        self.password_label = QLabel('Password:')
        layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.passwordim_button = QPushButton('Password dimenticata?')
        self.passwordim_button.clicked.connect(self.mostra_password_dimenticata)
        layout.addWidget(self.passwordim_button)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if not email or not password:
            QMessageBox.warning(self, 'Errore di login', 'Inserisci email e password')
            return

        utente = self.sistema_mensa.login(email, password)
        if utente:
            if isinstance(utente, Studente):
                self.parentWidget().setCurrentWidget(self.parentWidget().parentWidget().studente_view)
            elif isinstance(utente, Amministratore):
                self.parentWidget().setCurrentWidget(self.parentWidget().parentWidget().amministratore_view)
        else:
            QMessageBox.warning(self, 'Errore di login', 'Email o password errati')

    def mostra_password_dimenticata(self):
        dialog = PasswordDimenticataDialog(self.sistema_mensa, self)
        dialog.exec_()
