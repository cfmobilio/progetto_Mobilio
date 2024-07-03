from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox, QHBoxLayout
from funzionalità.pagamento import Pagamento


class PagamentoView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(PagamentoView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
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
        self.setWindowTitle('MangiAmo')
        layout = QVBoxLayout()

        self.pagamento_label = QLabel('Pagamenti')
        layout.addWidget(self.pagamento_label)

        self.saldo_label = QLabel(f"Saldo borsellino virtuale: {self.studente.get_info()['borsellino']:.2f} €")
        layout.addWidget(self.saldo_label)

        form_layout = QFormLayout()

        self.nome_input = QLineEdit(self.studente.nome)
        self.nome_input.setReadOnly(True)
        form_layout.addRow("Nome:", self.nome_input)

        self.cognome_input = QLineEdit(self.studente.cognome)
        self.cognome_input.setReadOnly(True)
        form_layout.addRow("Cognome:", self.cognome_input)

        self.anno_mese_layout = QHBoxLayout()
        self.mese_scadenza_input = QLineEdit()
        self.mese_scadenza_input.setPlaceholderText("MM")
        self.mese_scadenza_input.setMaximumWidth(50)
        self.anno_mese_layout.addWidget(self.mese_scadenza_input)

        self.anno_scadenza_input = QLineEdit()
        self.anno_scadenza_input.setPlaceholderText("YYYY")
        self.anno_scadenza_input.setMaximumWidth(70)
        self.anno_mese_layout.addWidget(self.anno_scadenza_input)

        form_layout.addRow("Scadenza carta:", self.anno_mese_layout)

        self.numero_carta_input = QLineEdit()
        form_layout.addRow("Numero carta:", self.numero_carta_input)

        self.cvv_input = QLineEdit()
        form_layout.addRow("CVV:", self.cvv_input)

        self.importo_input = QLineEdit()
        form_layout.addRow("Importo:", self.importo_input)

        layout.addLayout(form_layout)

        self.importo_buttons_layout = QHBoxLayout()
        for importo in ["€ 10,00", "€ 20,00", "€ 50,00", "€ 100,00"]:
            button = QPushButton(importo)
            button.clicked.connect(lambda _, imp=importo: self.set_importo(imp))
            self.importo_buttons_layout.addWidget(button)

        layout.addLayout(self.importo_buttons_layout)

        self.paga_button = QPushButton('Paga')
        self.paga_button.clicked.connect(self.process_payment)
        layout.addWidget(self.paga_button)

        self.setLayout(layout)

    def set_importo(self, importo):
        self.importo_input.setText(importo.replace("€", "").replace(",", "."))

    def process_payment(self):
        pagamento = Pagamento(
            self.nome_input.text(),
            self.cognome_input.text(),
            self.numero_carta_input.text(),
            self.mese_scadenza_input.text(),
            self.anno_scadenza_input.text(),
            self.cvv_input.text(),
            self.importo_input.text(),
            self.studente,
            self.sistema_mensa,
            self
        )
        pagamento.effettua_pagamento()
