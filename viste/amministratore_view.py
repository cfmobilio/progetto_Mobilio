from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel,
                             QPushButton, QMessageBox, QGridLayout,
                             QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from viste.scorte_view import ScorteView
from viste.aggiorna_menù_view import MenuManager
from viste.report_view import ReportViewer
from viste.nuove_notifiche_view import GestioneNotificheAdmin


class AmministratoreView(QWidget):
    def __init__(self, amministratore, sistema_mensa, parent=None):
        super(AmministratoreView, self).__init__(parent)
        self.amministratore = amministratore
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MangiAmo')
        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: black;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px 20px;
                background-color: white;
                color: black;
                border: 1px solid #ddd;
                border-radius: 5px;
                min-width: 200px;
                min-height: 40px;
                text-align: left;
                padding-left: 30px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)

        self.layout = QGridLayout()

        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0, 1, 2)

        self.benvenuto_label = QLabel(f"Bentornato, {self.amministratore.get_info()['nome']}")
        self.layout.addWidget(self.benvenuto_label, 1, 0, 1, 2, alignment=Qt.AlignCenter)

        self.gestisci_menu_button = QPushButton('Modifica Menu')
        self.gestisci_menu_button.clicked.connect(self.show_menu_manager)
        self.layout.addWidget(self.gestisci_menu_button)

        self.aggiorna_scorte_button = QPushButton('Aggiorna Scorte')
        self.aggiorna_scorte_button.clicked.connect(self.aggiorna_scorte)
        self.layout.addWidget(self.aggiorna_scorte_button)

        self.visualizza_report_button = QPushButton('Visualizza Report')
        self.visualizza_report_button.clicked.connect(self.show_report_viewer)
        self.layout.addWidget(self.visualizza_report_button)

        self.invia_notifiche_button = QPushButton('Invia Notifiche')
        self.invia_notifiche_button.clicked.connect(self.invia_notifiche)
        self.layout.addWidget(self.invia_notifiche_button)

        self.logout_button = QPushButton('Logout')
        self.logout_button.clicked.connect(self.logout)
        self.layout.addWidget(self.logout_button, 7, 0, alignment=Qt.AlignCenter)

        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 8, 0, 1, 2)

        self.setLayout(self.layout)

    def show_menu_manager(self):
        try:
            self.menu_manager = MenuManager(self.sistema_mensa)
            self.menu_manager.show()
        except Exception as e:
            print(f"Errore durante l'apertura del MenuManager: {e}")

    def aggiorna_scorte(self):
        self.scorte_view = ScorteView(self.amministratore, self.sistema_mensa)
        self.scorte_view.show()

    def show_report_viewer(self):
        self.report_viewer = ReportViewer(self.amministratore)
        self.report_viewer.show()

    def invia_notifiche(self):
        self.invia_notifiche = GestioneNotificheAdmin(self.sistema_mensa)
        self.invia_notifiche.show()

    def logout(self):
        reply = QMessageBox.question(self, 'Logout', 'Sei sicuro di voler uscire?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Logout", "Sei stato disconnesso.")
            self.parentWidget().setCurrentIndex(0)
