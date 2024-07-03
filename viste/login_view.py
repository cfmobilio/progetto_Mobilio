import re
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from utenti.amministratore import Amministratore
from utenti.studente import Studente
from viste.password_view import PasswordDimenticataDialog


class LoginView(QWidget):
    login_success = pyqtSignal(object)

    def __init__(self, sistema_mensa, parent=None):
        super(LoginView, self).__init__(parent)
        self.sistema_mensa = sistema_mensa
        self.init_ui()

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

        # Email field
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        # Password field
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Forgot password button
        self.passwordim_button = QPushButton('Password dimenticata?', self)
        self.passwordim_button.setObjectName('forgot_password')
        self.passwordim_button.clicked.connect(self.mostra_password_dimenticata)
        layout.addWidget(self.passwordim_button)

        # Login button
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.torna_button = QPushButton('Torna indietro')
        self.torna_button.clicked.connect(self.torna_indietro)
        layout.addWidget(self.torna_button)

        self.setLayout(layout)

    def valida_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if not email or not password:
            QMessageBox.warning(self, 'Errore di login', 'Inserisci email e password')
            return

        if not self.valida_email(email):
            QMessageBox.warning(self, 'Errore di login', 'Formato email non valido')
            return

        utente = self.sistema_mensa.login(email, password)
        if utente:
            self.login_success.emit(utente)
        else:
            QMessageBox.warning(self, 'Errore di login', 'Email o password errati')

    def mostra_password_dimenticata(self):
        dialog = PasswordDimenticataDialog(self.sistema_mensa, self)
        dialog.exec_()

    def torna_indietro(self):
        self.parentWidget().setCurrentIndex(0)
