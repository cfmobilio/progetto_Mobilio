import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QMessageBox
from datetime import datetime
from funzionalità.menù import Menu


class MenuView(QWidget):
    def __init__(self, sistema_mensa, parent=None):
        super(MenuView, self).__init__(parent)
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Menù del Giorno')
        layout = QVBoxLayout()

        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: normal;
                color: black;
            }
            QListWidget {
                font-size: 16px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        current_date = datetime.now().strftime('%d-%m-%Y')
        self.menu_label = QLabel(f'Menù del giorno {current_date}:')
        layout.addWidget(self.menu_label)

        # Lista per visualizzare i piatti del menu
        self.menu_list = QListWidget()
        layout.addWidget(self.menu_list)

        self.setLayout(layout)
        Menu.update_menu(self)
