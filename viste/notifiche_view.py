import logging
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget

class NotificheView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(NotificheView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.notifiche_list = QListWidget(self)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.notifiche_list)
        self.setLayout(layout)
        logging.debug("UI delle notifiche inizializzata")
        self.update_notifiche()

    def update_notifiche(self):
        self.notifiche_list.clear()
        logging.debug("Lista delle notifiche ripulita")
        try:
            notifiche = self.sistema_mensa.notifiche.get_notifiche()  # Cambiato da leggi_notifiche a get_notifiche
            logging.debug(f"Notifiche lette: {notifiche}")
            for line in notifiche:
                self.notifiche_list.addItem(line.strip())
                logging.debug(f"Notifica aggiunta: {line.strip()}")
        except Exception as e:
            logging.error(f"Errore durante l'aggiornamento delle notifiche: {e}")
