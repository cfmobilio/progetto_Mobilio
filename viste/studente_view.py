import logging

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox, QVBoxLayout, QListWidget


class StudenteView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(StudenteView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.benvenuto_label = QLabel(f"Benvenuto, {self.studente.get_info()['nome']}")
        layout.addWidget(self.benvenuto_label)

        self.visualizza_menu_button = QPushButton('Visualizza Menu')
        self.visualizza_menu_button.clicked.connect(self.visualizza_menu)
        layout.addWidget(self.visualizza_menu_button)

        self.prenota_pasto_button = QPushButton('Prenota Pasto')
        self.prenota_pasto_button.clicked.connect(self.prenota_pasto)
        layout.addWidget(self.prenota_pasto_button)

        self.effettua_pagamento_button = QPushButton('Effettua Pagamento')
        self.effettua_pagamento_button.clicked.connect(self.effettua_pagamento)
        layout.addWidget(self.effettua_pagamento_button)

        self.visualizza_notifiche_button = QPushButton('Visualizza Notifiche')
        self.visualizza_notifiche_button.clicked.connect(self.visualizza_notifiche)
        layout.addWidget(self.visualizza_notifiche_button)

        self.sottoscrivi_abbonamento_button = QPushButton('Sottoscrivi Abbonamento')
        self.sottoscrivi_abbonamento_button.clicked.connect(self.sottoscrivi_abbonamento)
        layout.addWidget(self.sottoscrivi_abbonamento_button)

        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def visualizza_menu(self):
        try:
            from viste.menu_view import MenuView  # Importazione ritardata per evitare importazione circolare
            self.menu_view = MenuView(self.sistema_mensa, self)  # Creazione di un'istanza di MenuView
            self.layout().addWidget(self.menu_view)  # Aggiungi MenuView al layout corrente
            self.menu_view.show()  # Mostra MenuView
        except ImportError as e:
            logging.error(f"Errore durante l'importazione di MenuView: {e}")

    def prenota_pasto(self):
        try:
            from viste.prenotazione_view import PrenotazioneView
            # Importazione ritardata per evitare importazione circolare
            self.prenotazione_view = PrenotazioneView(self.studente, self.sistema_mensa)
            self.prenotazione_view.show()
        except ImportError as e:
            logging.error(f"Errore durante l'importazione di PrenotazioneView: {e}")

    def effettua_pagamento(self):
        try:
            from viste.pagamento_view import PagamentoView
            self.pagamento_view = PagamentoView(self.studente, self.sistema_mensa)
            self.pagamento_view.show()
        except ImportError as e:
            logging.error(f"Errore durante l'importazione di PagamentoView: {e}")

    def submit_pagamento(self):
        importo = float(self.importo_input.text())
        risultato = self.studente.effettua_pagamento(importo)
        QMessageBox.information(self, "Pagamento", risultato)
        self.pagamento_window.close()

    def visualizza_notifiche(self):
        self.notifiche_window = QWidget()
        self.notifiche_window.setWindowTitle("Notifiche")
        layout = QVBoxLayout()

        self.notifiche_list = QListWidget()
        layout.addWidget(self.notifiche_list)

        self.update_notifiche()  # Aggiorna le notifiche solo dopo aver creato la lista delle notifiche

        self.notifiche_window.setLayout(layout)
        self.notifiche_window.show()

    def update_notifiche(self):
        try:
            notifiche = self.sistema_mensa.notifiche.get_notifiche()
            self.notifiche_list.clear()
            for notifica in notifiche:
                self.notifiche_list.addItem(notifica)
        except AttributeError as e:
            logging.error(f"Errore durante l'aggiornamento delle notifiche: {e}")
        except Exception as e:
            logging.error(f"Errore generico durante l'aggiornamento delle notifiche: {e}")

    def sottoscrivi_abbonamento(self):
        try:
            from viste.abbonamento_view import AbbonamentoView
            self.abbonamento_view = AbbonamentoView(self.studente, self.sistema_mensa)
            self.abbonamento_view.show()
        except ImportError as e:
            logging.error(f"Errore durante l'importazione di AbbonamentoView: {e}")

    def submit_abbonamento(self):
        abbonamento = self.abbonamento_input.text()
        risultato = self.studente.sottoscrivi_abbonamento(abbonamento)
        QMessageBox.information(self, "Abbonamento", risultato)
        self.abbonamento_window.close()

    def logout(self):
        reply = QMessageBox.question(self, 'Logout', 'Sei sicuro di voler uscire?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Logout", "Sei stato disconnesso.")
            self.close()  # Close the main window import os
