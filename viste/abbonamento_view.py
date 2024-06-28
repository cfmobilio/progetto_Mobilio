from datetime import datetime, timedelta
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout
from funzionalità.abbonamento import Abbonamento


class AbbonamentoView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(AbbonamentoView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.abbonamento_label = QLabel(f'{self.studente.get_info()["nome"]} {self.studente.get_info()["email"]}')
        self.abbonamento_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.abbonamento_label)

        # 15 meals subscription
        self.abbonamento_15_label = QLabel('Abbonamento 15 pasti')
        self.abbonamento_15_button = QPushButton('€ 70,00')
        self.abbonamento_15_button.clicked.connect(lambda: self.acquista_abbonamento(15, 70))
        layout.addWidget(self.abbonamento_15_label)
        layout.addWidget(self.abbonamento_15_button)

        # Monthly subscription
        self.abbonamento_mensile_label = QLabel('Abbonamento mensile valido dal 01/08/2023 al 31/08/2023')
        self.abbonamento_mensile_button = QPushButton('€ 135,00')
        self.abbonamento_mensile_button.clicked.connect(lambda: self.acquista_abbonamento(30, 135))
        layout.addWidget(self.abbonamento_mensile_label)
        layout.addWidget(self.abbonamento_mensile_button)

        # Pulsante acquista e costo totale
        self.costo_totale_label = QLabel('Costo Totale: €0,00')
        self.acquista_layout = QHBoxLayout()
        self.acquista_button = QPushButton('Acquista')
        self.acquista_button.setStyleSheet("background-color: gray; color: white;")
        self.acquista_button.clicked.connect(self.effettua_acquisto)
        self.acquista_layout.addWidget(self.acquista_button)
        self.acquista_layout.addWidget(self.costo_totale_label)
        layout.addLayout(self.acquista_layout)

        self.setLayout(layout)

    def acquista_abbonamento(self, giorni, costo):
        # Logica per acquistare un abbonamento
        data_inizio = datetime.now()
        data_scadenza = data_inizio + timedelta(days=giorni)
        codice = f"{self.studente.get_info()['codice']}_{data_inizio.strftime('%Y%m%d')}"
        abbonamento = Abbonamento(codice, data_inizio, data_inizio, data_scadenza, giorni == 30)

        try:
            self.sistema_mensa.aggiungi_abbonamento(abbonamento)
            QMessageBox.information(self, "Transazione Riuscita",
                                    f'Abbonamento di {giorni} giorni acquistato per {costo}€')
        except Exception as e:
            QMessageBox.critical(self, "Transazione Fallita", f'Errore durante l\'acquisto dell\'abbonamento: {str(e)}')

    def effettua_acquisto(self):
        # Logica per completare l'acquisto e aggiornare il costo totale
        QMessageBox.information(self, "Acquisto", "Acquisto completato!")
