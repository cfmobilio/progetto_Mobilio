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
        self.menu_list = None

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
        try:
            with open("menu.txt", "r") as file:
                menu_lines = file.readlines()
        except FileNotFoundError:
            QMessageBox.critical(self, "Errore", "Il file menu.txt non è stato trovato.")
            return
        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Si è verificato un errore: {str(e)}")
            return

        # Pulisce la lista del menu prima di aggiungere i nuovi piatti
        self.menu_list.clear()

        # Conteggio per i vari tipi di piatti
        count_per_type = {'Primo': 0, 'Secondo': 0, 'Contorno': 0}
        pasto_type = None

        for line in menu_lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith("Primo piatto:"):
                pasto_type = "Primo"
                if count_per_type[pasto_type] == 0:
                    self.menu_list.addItem("Primo piatto:")
            elif line.startswith("Secondo piatto:"):
                pasto_type = "Secondo"
                if count_per_type[pasto_type] == 0:
                    self.menu_list.addItem("Secondo piatto:")
            elif line.startswith("Contorno:"):
                pasto_type = "Contorno"
                if count_per_type[pasto_type] == 0:
                    self.menu_list.addItem("Contorno:")
            elif pasto_type in count_per_type:
                if count_per_type[pasto_type] < 2:
                    self.menu_list.addItem(line)
                    count_per_type[pasto_type] += 1

        # Controllo di sicurezza per assicurarsi che tutti i tipi di pasto siano stati gestiti
        if pasto_type not in count_per_type:
            QMessageBox.critical(self, "Errore", f"Tipo di pasto sconosciuto: {pasto_type}")
            return
