from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QSpacerItem, QSizePolicy
from funzionalità.notifiche import Notifiche


class NotificheView(QWidget):
    def __init__(self, studente, sistema_mensa, parent=None):
        super(NotificheView, self).__init__(parent)
        self.studente = studente
        self.sistema_mensa = sistema_mensa
        self.notifiche_list = QListWidget(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MangiAmo')
        layout = QVBoxLayout(self)

        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: black;
            }
            QListWidget {
                font-size: 16px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        self.title_label = QLabel('Notifiche')
        layout.addWidget(self.title_label)

        self.notifiche_list = QListWidget()
        layout.addWidget(self.notifiche_list)

        self.setLayout(layout)
        Notifiche.update_notifiche(self)
