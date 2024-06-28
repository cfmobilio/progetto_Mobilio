from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QMessageBox


class PrenotazioneView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(PrenotazioneView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.giorno_label = QLabel('Seleziona giorno:')
        layout.addWidget(self.giorno_label)
        self.giorno_combo = QComboBox()
        self.giorno_combo.addItems(["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"])
        layout.addWidget(self.giorno_combo)

        self.mensa_label = QLabel('Seleziona Mensa:')
        layout.addWidget(self.mensa_label)
        self.mensa_combo = QComboBox()
        self.mensa_combo.addItems(["Gusti universitari", "Mensa del sapere", "Mensa della Conoscenza",
                                   "Sapore Accademico"])
        layout.addWidget(self.mensa_combo)

        self.pasto_label = QLabel('Seleziona Pasto:')
        layout.addWidget(self.pasto_label)
        self.pasto_combo = QComboBox()
        self.pasto_combo.addItems(["Pranzo", "Cena"])
        layout.addWidget(self.pasto_combo)

        self.prenota_button = QPushButton('Prenota ora')
        self.prenota_button.clicked.connect(self.prenota_pasto)
        layout.addWidget(self.prenota_button)

        self.setLayout(layout)

    def prenota_pasto(self):
        giorno = self.giorno_combo.currentText()
        mensa = self.mensa_combo.currentText()
        pasto = self.pasto_combo.currentText()

        QMessageBox.information(self, "Prenotazione", f"Prenotazione per {pasto} di {giorno} presso "
                                                      f"{mensa} avvenuta con successo.")
