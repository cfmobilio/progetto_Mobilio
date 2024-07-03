from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox,
    QMessageBox, QFormLayout, QLineEdit
)
from funzionalità.scorte import Scorte


class ScorteView(QWidget):
    def __init__(self, amministratore, sistema_mensa, parent=None):
        super(ScorteView, self).__init__(parent)
        self.amministratore = amministratore
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

        self.setWindowTitle("Aggiorna Scorte")

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.ingrediente_input = QLineEdit()
        form_layout.addRow("Ingrediente:", self.ingrediente_input)

        self.quantita_input = QLineEdit()
        form_layout.addRow("Quantità:", self.quantita_input)

        self.unita_input = QComboBox()
        self.unita_input.addItems(["kg", "litri", "g", "ml", "unità"])
        form_layout.addRow("Unità di Misura:", self.unita_input)

        self.submit_scorte_button = QPushButton("Aggiorna Scorte")
        self.submit_scorte_button.clicked.connect(self.submit_scorte)
        form_layout.addRow("", self.submit_scorte_button)

        layout.addLayout(form_layout)

    def submit_scorte(self):
        ingrediente = self.ingrediente_input.text()
        quantita = self.quantita_input.text()

        try:
            quantita = float(quantita)
            unita = self.unita_input.currentText()

            risultato = self.amministratore.aggiorna_scorte(ingrediente, quantita, unita)
            QMessageBox.information(self, "Scorte", risultato)
            self.close()

        except ValueError:
            QMessageBox.warning(self, "Errore", "La quantità deve essere un numero.")

        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Si è verificato un errore: {e}")
