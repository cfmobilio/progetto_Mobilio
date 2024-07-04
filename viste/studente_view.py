from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QMessageBox, QVBoxLayout, QGridLayout, QListWidget,
                             QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from viste.menu_view import MenuView
from viste.prenotazione_view import PrenotazioneView
from viste.pagamento_view import PagamentoView
from viste.abbonamento_view import AbbonamentoView
from viste.notifiche_view import NotificheView


class StudenteView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(StudenteView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MangiAmo')
        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: black;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px 20px;
                background-color: white;
                color: black;
                border: 1px solid #ddd;
                border-radius: 5px;
                min-width: 200px;
                min-height: 40px;
                text-align: left;
                padding-left: 30px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)

        self.layout = QGridLayout()

        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0, 1, 2)

        self.benvenuto_label = QLabel(f"Bentornato, {self.studente.get_info()['nome']}")
        self.layout.addWidget(self.benvenuto_label, 1, 0, 1, 2, alignment=Qt.AlignCenter)

        self.visualizza_menu_button = QPushButton('Menu')
        self.visualizza_menu_button.setIcon(QIcon('icone/menu.png'))
        self.visualizza_menu_button.clicked.connect(self.visualizza_menu)
        self.layout.addWidget(self.visualizza_menu_button, 2, 0, alignment=Qt.AlignCenter)

        self.prenota_pasto_button = QPushButton('Prenotazione')
        self.prenota_pasto_button.clicked.connect(self.prenota_pasto)
        self.prenota_pasto_button.setIcon(QIcon('icone/booking.png'))
        self.layout.addWidget(self.prenota_pasto_button, 3, 0, alignment=Qt.AlignCenter)

        self.effettua_pagamento_button = QPushButton('Pagamento')
        self.effettua_pagamento_button.setIcon(QIcon('icone/credit-card.png'))
        self.effettua_pagamento_button.clicked.connect(self.effettua_pagamento)
        self.layout.addWidget(self.effettua_pagamento_button, 4, 0, alignment=Qt.AlignCenter)

        self.visualizza_notifiche_button = QPushButton('Notifiche')
        self.visualizza_notifiche_button.setIcon(QIcon('icone/bell.png'))
        self.visualizza_notifiche_button.clicked.connect(self.visualizza_notifiche)
        self.layout.addWidget(self.visualizza_notifiche_button, 5, 0, alignment=Qt.AlignCenter)

        self.sottoscrivi_abbonamento_button = QPushButton('Abbonamento')
        self.sottoscrivi_abbonamento_button.setIcon(QIcon('icone/abb.png'))
        self.sottoscrivi_abbonamento_button.clicked.connect(self.sottoscrivi_abbonamento)
        self.layout.addWidget(self.sottoscrivi_abbonamento_button, 6, 0, alignment=Qt.AlignCenter)

        self.logout_button = QPushButton('Logout')
        self.logout_button.setIcon(QIcon('icone/logout.png'))
        self.logout_button.clicked.connect(self.logout)
        self.layout.addWidget(self.logout_button, 7, 0, alignment=Qt.AlignCenter)

        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 8, 0, 1, 2)

        self.setLayout(self.layout)

    def visualizza_menu(self):
        try:
            self.menu_view = MenuView(self.sistema_mensa, self)
            self.layout.addWidget(self.menu_view, 2, 1, 5, 1)
            self.menu_view.show()
        except ImportError:
            pass
        except Exception:
            pass

    def aggiorna_studente(self, studente):
        self.studente = studente
        self.benvenuto_label.setText(f"Bentornato, {self.studente.get_info()['nome']}")

    def prenota_pasto(self):
        try:
            self.prenotazione_view = PrenotazioneView(self.studente, self.sistema_mensa)
            self.prenotazione_view.show()
        except ImportError:
            pass

    def effettua_pagamento(self):
        try:
            self.pagamento_view = PagamentoView(self.studente, self.sistema_mensa)
            self.pagamento_view.show()
        except ImportError:
            pass

    def visualizza_notifiche(self):
        try:
            self.notifica_view = NotificheView(self.studente, self.sistema_mensa)
            self.notifica_view.show()
        except ImportError:
            pass

    def sottoscrivi_abbonamento(self):
        try:
            self.abbonamento_view = AbbonamentoView(self.studente, self.sistema_mensa)
            self.abbonamento_view.show()
        except ImportError:
            pass

    def logout(self):
        reply = QMessageBox.question(self, 'Logout', 'Sei sicuro di voler uscire?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Logout", "Sei stato disconnesso.")
            self.parentWidget().setCurrentIndex(0)
