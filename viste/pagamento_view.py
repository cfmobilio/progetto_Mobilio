from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox, QHBoxLayout


class PagamentoView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(PagamentoView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.pagamento_label = QLabel('Pagamenti')
        layout.addWidget(self.pagamento_label)

        self.saldo_label = QLabel('Saldo borsellino virtuale: € 7,00')
        layout.addWidget(self.saldo_label)

        form_layout = QFormLayout()

        self.nome_input = QLineEdit()
        self.cognome_input = QLineEdit()
        self.numero_carta_input = QLineEdit()
        self.mese_scadenza_input = QLineEdit()
        self.anno_scadenza_input = QLineEdit()
        self.cvv_input = QLineEdit()

        form_layout.addRow("Nome:", self.nome_input)
        form_layout.addRow("Cognome:", self.cognome_input)
        form_layout.addRow("Numero carta:", self.numero_carta_input)
        form_layout.addRow("Mese scadenza:", self.mese_scadenza_input)
        form_layout.addRow("Anno scadenza:", self.anno_scadenza_input)
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
        self.paga_button.clicked.connect(self.effettua_pagamento)
        layout.addWidget(self.paga_button)

        self.setLayout(layout)

    def set_importo(self, importo):
        self.importo_input.setText(importo.replace("€", "").replace(",", "."))

    def effettua_pagamento(self):
        nome = self.nome_input.text()
        cognome = self.cognome_input.text()
        numero_carta = self.numero_carta_input.text()
        mese_scadenza = self.mese_scadenza_input.text()
        anno_scadenza = self.anno_scadenza_input.text()
        cvv = self.cvv_input.text()
        importo = self.importo_input.text()

        # Logica per effettuare il pagamento
        if self.validate_inputs(nome, cognome, numero_carta, mese_scadenza, anno_scadenza, cvv, importo):
            risultato = self.studente.effettua_pagamento(float(importo))
            QMessageBox.information(self, "Pagamento", risultato)
        else:
            QMessageBox.warning(self, "Errore", "Per favore, completa tutti i campi correttamente.")

    def validate_inputs(self, nome, cognome, numero_carta, mese_scadenza, anno_scadenza, cvv, importo):
        if (not nome or not cognome or not numero_carta or not mese_scadenza or not anno_scadenza
                or not cvv or not importo):
            return False
        try:
            float(importo)
        except ValueError:
            return False
        return True
