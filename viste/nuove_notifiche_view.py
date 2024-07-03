from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QFormLayout, QLineEdit, QTextEdit,
                             QPushButton, QMessageBox)
from funzionalità.notifiche import Notifiche

class GestioneNotificheAdmin(QWidget):
    def __init__(self, sistema_mensa, parent=None):
        super(GestioneNotificheAdmin, self).__init__(parent)
        self.sistema_mensa = sistema_mensa
        self.notifiche_window = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Gestione Notifiche Amministratori')
        layout = QFormLayout(self)  # Use QFormLayout here

        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
            }
            QLineEdit {
                font-size: 16px;
                padding: 10px;
                border: 2px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px;
                background-color: #FF0000;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton#forgot_password {
                background-color: transparent;
                color: #e74c3c;
                text-align: left;
            }
        """)

        self.titolo_input = QLineEdit()
        self.messaggio_input = QTextEdit()

        layout.addRow("Titolo:", self.titolo_input)
        layout.addRow("Messaggio:", self.messaggio_input)

        invia_notifiche_button = QPushButton("Invia Notifica")
        invia_notifiche_button.clicked.connect(self.submit_notifica)
        layout.addWidget(invia_notifiche_button)

        self.setLayout(layout)

    def submit_notifica(self):
        titolo = self.titolo_input.text()
        messaggio = self.messaggio_input.toPlainText()

        if titolo and messaggio:
            notifica = f"{titolo}: {messaggio}"
            self.sistema_mensa.aggiungi_notifica_amministratore(notifica)
            QMessageBox.information(self, "Notifiche", "Notifica inviata con successo.")
        else:
            QMessageBox.warning(self, "Errore", "Titolo e messaggio non possono essere vuoti.")

        self.close()

    def show_window(self):
        self.notifiche_window = QWidget()
        self.notifiche_window.setWindowTitle("Aggiungi Notifica")
        self.notifiche_window.setWindowModality(Qt.ApplicationModal)
        self.notifiche_window.setLayout(self.layout())
        self.notifiche_window.show()
