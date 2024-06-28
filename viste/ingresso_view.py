from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt


class WelcomeView(QWidget):
    def __init__(self, parent=None):
        super(WelcomeView, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.welcome_label = QLabel()
        self.welcome_label.setText("Benvenuto alla Mensa Universitaria")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.welcome_label)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.mostra_login)
        layout.addWidget(self.login_button)

        self.registrazione_button = QPushButton('Registrati')
        self.registrazione_button.clicked.connect(self.mostra_registrazione)
        layout.addWidget(self.registrazione_button)

        self.setLayout(layout)

    def mostra_login(self):
        self.parentWidget().setCurrentWidget(self.parentWidget().parentWidget().login_view)

    def mostra_registrazione(self):
        self.parentWidget().setCurrentWidget(self.parentWidget().parentWidget().registrazione_view)
