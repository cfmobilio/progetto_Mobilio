from PyQt5.QtWidgets import (QPushButton, QLabel, QFormLayout, QWidget,
                             QVBoxLayout, QMessageBox, QLineEdit, QTextEdit,
                             QComboBox, QHBoxLayout, QScrollArea)
import logging

# Configura il logger
logging.basicConfig(level=logging.DEBUG)


class AmministratoreView(QWidget):
    def __init__(self, amministratore, sistema_mensa, parent=None):
        super(AmministratoreView, self).__init__(parent)
        self.amministratore = amministratore
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.benvenuto_label = QLabel(f"Benvenuto, {self.amministratore.get_info()['nome']}")
        layout.addWidget(self.benvenuto_label)

        self.gestisci_menu_button = QPushButton('Modifica Menu')
        self.gestisci_menu_button.clicked.connect(self.gestisci_menu)
        layout.addWidget(self.gestisci_menu_button)

        self.aggiorna_scorte_button = QPushButton('Aggiorna Scorte')
        self.aggiorna_scorte_button.clicked.connect(self.aggiorna_scorte)
        layout.addWidget(self.aggiorna_scorte_button)

        self.visualizza_report_button = QPushButton('Visualizza Report')
        self.visualizza_report_button.clicked.connect(self.visualizza_report)
        layout.addWidget(self.visualizza_report_button)

        self.invia_notifiche_button = QPushButton('Invia Notifiche')
        self.invia_notifiche_button.clicked.connect(self.invia_notifiche)
        layout.addWidget(self.invia_notifiche_button)

        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def gestisci_menu(self):
        self.menu_window = QWidget()
        self.menu_window.setWindowTitle("Gestisci Menu")
        layout = QVBoxLayout()

        self.pasti_layout = QVBoxLayout()
        self.add_pasto()

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_widget.setLayout(self.pasti_layout)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(200)

        layout.addWidget(scroll_area)

        self.add_pasto_button = QPushButton("Aggiungi Piatto")
        self.add_pasto_button.clicked.connect(self.add_pasto)
        layout.addWidget(self.add_pasto_button)

        self.submit_menu_button = QPushButton("Aggiorna Menu")
        self.submit_menu_button.clicked.connect(self.submit_menu)
        layout.addWidget(self.submit_menu_button)

        self.menu_window.setLayout(layout)
        self.menu_window.show()

    def add_pasto(self):
        pasto_layout = QHBoxLayout()

        tipo_pasto_combo = QComboBox()
        tipo_pasto_combo.addItems(["Primo", "Secondo", "Contorno"])
        pasto_layout.addWidget(tipo_pasto_combo)

        nome_pasto_input = QLineEdit()
        pasto_layout.addWidget(nome_pasto_input)

        self.pasti_layout.addLayout(pasto_layout)

    def submit_menu(self):
        logging.debug("Inizio submit_menu")
        pasti = []
        for i in range(self.pasti_layout.count()):
            pasto_layout = self.pasti_layout.itemAt(i).layout()
            tipo_pasto_combo = pasto_layout.itemAt(0).widget()
            nome_pasto_input = pasto_layout.itemAt(1).widget()
            tipo_pasto = tipo_pasto_combo.currentText()
            nome_pasto = nome_pasto_input.text()
            if nome_pasto:
                logging.debug(f"Pasto aggiunto: {tipo_pasto}, {nome_pasto}")
                pasti.append((tipo_pasto, nome_pasto))

        for tipo_pasto, nome_pasto in pasti:
            logging.debug(f"Chiamata a gestisci_menu con: {tipo_pasto}, {nome_pasto}")
            risultato = self.amministratore.gestisci_menu(tipo_pasto, nome_pasto)
            if risultato:
                QMessageBox.information(self, "Menu", risultato)
                self.sistema_mensa.menu.aggiungi_pasto(nome_pasto)
                QMessageBox.information(self, "Notifiche", "Notifica inviata con successo.")
            else:
                QMessageBox.warning(self, "Errore", f"Errore nell'aggiunta del pasto: {nome_pasto}")

        self.menu_window.close()
        logging.debug("Fine submit_menu")

    def aggiorna_scorte(self):
        self.scorte_window = QWidget()
        self.scorte_window.setWindowTitle("Aggiorna Scorte")
        layout = QFormLayout()

        self.ingrediente_input = QLineEdit()
        layout.addRow("Ingrediente:", self.ingrediente_input)

        self.quantita_input = QLineEdit()
        layout.addRow("Quantità:", self.quantita_input)

        self.submit_scorte_button = QPushButton("Aggiorna Scorte")
        self.submit_scorte_button.clicked.connect(self.submit_scorte)
        layout.addWidget(self.submit_scorte_button)

        self.scorte_window.setLayout(layout)
        self.scorte_window.show()

    def submit_scorte(self):
        ingrediente = self.ingrediente_input.text()
        quantita = int(self.quantita_input.text())
        risultato = self.amministratore.aggiorna_scorte(ingrediente, quantita)
        QMessageBox.information(self, "Scorte", risultato)
        self.scorte_window.close()

    def visualizza_report(self):
        self.report_window = QWidget()
        self.report_window.setWindowTitle("Visualizza Report")
        layout = QVBoxLayout()

        self.tipo_report_combo = QComboBox()
        self.tipo_report_combo.addItems(["Report Prenotazioni", "Report Scorte", "Report Abbonamenti"])
        layout.addWidget(self.tipo_report_combo)

        self.visualizza_report_button = QPushButton("Visualizza")
        self.visualizza_report_button.clicked.connect(self.mostra_report)
        layout.addWidget(self.visualizza_report_button)

        self.report_window.setLayout(layout)
        self.report_window.show()

    def mostra_report(self):
        tipo_report = self.tipo_report_combo.currentText()

        if tipo_report == "Report Prenotazioni":
            report = self.amministratore.visualizza_report_prenotazioni()
            report_text = f"Prenotazioni Totali: {report['prenotazioni_totali']}\n"
        elif tipo_report == "Report Scorte":
            report = self.amministratore.visualizza_report_scorte()
            report_text = f"Scorte: {report['scorte']}\n"
        elif tipo_report == "Report Abbonamenti":
            report = self.amministratore.visualizza_report_abbonamenti()
            report_text = f"Abbonamenti Attivi: {report['abbonamenti_attivi']}"

        QMessageBox.information(self, "Report", report_text)
        self.report_window.close()

    def invia_notifiche(self):
        self.notifiche_window = QWidget()
        self.notifiche_window.setWindowTitle("Aggiungere il contenuto")
        layout = QFormLayout()

        self.titolo_input = QLineEdit()
        layout.addRow("Titolo:", self.titolo_input)

        self.messaggio_input = QTextEdit()
        layout.addRow("Messaggio:", self.messaggio_input)

        self.submit_notifiche_button = QPushButton("Invia Notifiche")
        self.submit_notifiche_button.clicked.connect(self.submit_notifiche)
        layout.addWidget(self.submit_notifiche_button)

        self.notifiche_window.setLayout(layout)
        self.notifiche_window.show()

    def submit_notifiche(self):
        titolo = self.titolo_input.text()
        messaggio = self.messaggio_input.toPlainText()
        if titolo and messaggio:
            notifica = f"{titolo}: {messaggio}"
            self.sistema_mensa.notifiche.aggiungi_notifica(notifica)
            QMessageBox.information(self, "Notifiche", "Notifica inviata con successo.")
        else:
            QMessageBox.warning(self, "Errore", "Titolo e messaggio non possono essere vuoti.")
        self.notifiche_window.close()

    def logout(self):
        reply = QMessageBox.question(self, 'Logout', 'Sei sicuro di voler uscire?',
                                     QMessageBox.Yes,QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Logout", "Sei stato disconnesso.")
            self.close()
