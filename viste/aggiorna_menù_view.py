from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel,
                             QPushButton, QMessageBox, QScrollArea,
                             QComboBox, QLineEdit, QHBoxLayout,
                             QSpacerItem, QSizePolicy, QDialog, QListWidget, QListWidgetItem)
from PyQt5.QtGui import QIcon
from funzionalità.menù import Menu


class MenuManager(QWidget):
    def __init__(self, sistema_mensa):
        super(MenuManager, self).__init__()
        self.sistema_mensa = sistema_mensa
        self.menu = Menu()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MangiAmo - Amministratore')
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
        layout = QVBoxLayout()

        spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_top)

        self.menu_list = QListWidget()
        layout.addWidget(self.menu_list)

        self.update_menu_list()

        self.add_pasto_button = QPushButton("Aggiungi Piatto")
        self.add_pasto_button.clicked.connect(self.show_add_pasto_dialog)
        layout.addWidget(self.add_pasto_button)

        self.setLayout(layout)

    def update_menu_list(self):
        self.menu_list.clear()
        try:
            with open("menu.txt", "r") as file:
                menu_lines = file.readlines()
                for line in menu_lines:
                    if line.strip():
                        item = QListWidgetItem(line.strip())
                        self.menu_list.addItem(item)
        except FileNotFoundError:
            QMessageBox.critical(self, "Errore", "Il file menu.txt non è stato trovato.")
        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Si è verificato un errore: {str(e)}")

    def show_add_pasto_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Aggiungi Piatto")

        layout = QVBoxLayout(dialog)
        self.pasti_layout = QVBoxLayout()

        self.add_pasto(self.pasti_layout)

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_widget.setLayout(self.pasti_layout)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(200)

        layout.addWidget(scroll_area)

        self.add_pasto_button = QPushButton("Aggiungi Piatto")
        self.add_pasto_button.clicked.connect(lambda: self.add_pasto(self.pasti_layout))
        layout.addWidget(self.add_pasto_button)

        self.submit_menu_button = QPushButton("Aggiorna Menu")
        self.submit_menu_button.clicked.connect(lambda: self.submit_menu(dialog, self.pasti_layout))
        layout.addWidget(self.submit_menu_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def add_pasto(self, pasti_layout):
        pasto_layout = QHBoxLayout()

        tipo_pasto_combo = QComboBox()
        tipo_pasto_combo.addItems(["Primo", "Secondo", "Contorno"])
        pasto_layout.addWidget(tipo_pasto_combo)

        nome_pasto_input = QLineEdit()
        pasto_layout.addWidget(nome_pasto_input)

        pasti_layout.addLayout(pasto_layout)

    def submit_menu(self, dialog, pasti_layout):
        try:
            with open("menu.txt", "a") as file:
                for i in range(pasti_layout.count()):
                    pasto_layout = pasti_layout.itemAt(i).layout()
                    tipo_pasto_combo = pasto_layout.itemAt(0).widget()
                    nome_pasto_input = pasto_layout.itemAt(1).widget()
                    tipo_pasto = tipo_pasto_combo.currentText()
                    nome_pasto = nome_pasto_input.text()
                    if nome_pasto:
                        file.write(f"{tipo_pasto}: {nome_pasto}\n")
            self.update_menu_list()
            dialog.accept()
        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Si è verificato un errore: {e}")
