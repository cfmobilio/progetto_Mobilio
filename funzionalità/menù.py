from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QScrollArea,
                             QComboBox, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy, QDialog,
                             QListWidget, QListWidgetItem)
from PyQt5.QtGui import QIcon
import os
import pickle


class Menu:
    def __init__(self):
        self.menu = []
        self.carica_menu_da_file()
        self.menu_list = None  # Assicurati che questa sia inizializzata correttamente da qualche parte

    def carica_menu_da_file(self, nome_file="menu.txt"):
        if os.path.isfile(nome_file):
            with open(nome_file, 'r') as f:
                categoria_attuale = None
                for line in f:
                    line = line.strip()
                    if line:
                        if line.endswith(':'):
                            categoria_attuale = line[:-1]
                        else:
                            if categoria_attuale:
                                self.aggiungi_pasto({
                                    'categoria': categoria_attuale,
                                    'nome': line
                                })

    def aggiungi_pasto(self, pasto):
        self.menu.append(pasto)
        self.salva_menu()

    def salva_menu(self, nome_file="menu.pickle"):
        with open(nome_file, 'wb') as f:
            pickle.dump(self.menu, f)

    def update_menu(self):
        self.menu_list.clear()
        try:
            with open("menu.txt", "r") as file:
                menu_lines = file.readlines()
                for line in menu_lines:
                    if line.strip():
                        item = QListWidgetItem(line.strip())
                        self.menu_list.addItem(item)
        except FileNotFoundError:
            QMessageBox.critical(None, "Errore", "Il file menu.txt non è stato trovato.")
        except Exception as e:
            QMessageBox.critical(None, "Errore", f"Si è verificato un errore: {str(e)}")
