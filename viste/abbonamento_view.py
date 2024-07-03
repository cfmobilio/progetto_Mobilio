import traceback
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QTextEdit
from datetime import datetime, timedelta
from funzionalità.abbonamento import Abbonamento


class AbbonamentoView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(AbbonamentoView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MangiAmo')
        layout = QVBoxLayout()
        self.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: normal;
                color: black;
            }
            QPushButton {
            font-size: 16px;
            padding: 10px 20px;
            background-color: #FF0000;
            color: white;
            border: none;
            border-radius: 5px;
            min-width: 150px;
            min-height: 40px;
            }
            QPushButton:hover {
            background-color: #c0392b;
            }
            """)

        self.abbonamento_label = QLabel(f'Abbonamenti di {self.studente.get_info()["nome"]} '
                                        f'{self.studente.get_info()["cognome"]}')
        self.abbonamento_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.abbonamento_label)

        self.abbonamenti_sottoscritti_label = QLabel('Abbonamenti Sottoscritti:')
        layout.addWidget(self.abbonamenti_sottoscritti_label)

        self.abbonamenti_sottoscritti_text = QTextEdit()
        self.abbonamenti_sottoscritti_text.setReadOnly(True)
        layout.addWidget(self.abbonamenti_sottoscritti_text)

        self.abbonamento_15_label = QLabel('Abbonamento 15 pasti')
        self.abbonamento_15_button = QPushButton('€ 70,00')
        self.abbonamento_15_button.clicked.connect(
            lambda: Abbonamento.acquista_abbonamento(self, self.studente, self.sistema_mensa, "15 pasti", 70)
        )
        layout.addWidget(self.abbonamento_15_label)
        layout.addWidget(self.abbonamento_15_button)

        self.abbonamento_mensile_label = QLabel('Abbonamento mensile')
        self.abbonamento_mensile_button = QPushButton('€ 135,00')
        self.abbonamento_mensile_button.clicked.connect(
            lambda: Abbonamento.acquista_abbonamento(self, self.studente, self.sistema_mensa, "mensile", 135)
        )
        layout.addWidget(self.abbonamento_mensile_label)
        layout.addWidget(self.abbonamento_mensile_button)

        self.setLayout(layout)

        Abbonamento.update_abbonamenti_view(self, self.studente)
