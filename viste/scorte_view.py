from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
import logging


class ScorteView(QWidget):
    def __init__(self, amministratore, sistema_mensa, parent=None):
        super(ScorteView, self).__init__(parent)
        self.amministratore = amministratore
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.scorte_label = QLabel('Scorte disponibili:')
        layout.addWidget(self.scorte_label)

        self.scorte_list = QListWidget()
        self.update_scorte()
        layout.addWidget(self.scorte_list)

        self.setLayout(layout)

    def update_scorte(self):
        scorte = self.sistema_mensa.get_scorte()  # Questo dovrebbe restituire una lista di scorte
        logging.debug(f"Scorte data: {scorte}")
        self.scorte_list.clear()
        for scorta in scorte:
            try:
                self.scorte_list.addItem(f"{scorta['ingrediente']} - {scorta['quantita']} unità")
            except KeyError as e:
                logging.error(f"KeyError: {e} in scorta: {scorta}")
