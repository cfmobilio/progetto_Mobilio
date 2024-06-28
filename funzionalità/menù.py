import os
import pickle


class Menu:
    def __init__(self):
        self.menu = []
        self.carica_menu_da_file()

    # Carica il menu da un file
    def carica_menu_da_file(self, nome_file="menu.txt"):
        if os.path.isfile(nome_file):
            with open(nome_file, 'r') as f:
                categoria_attuale = None
                for line in f:
                    line = line.strip()
                    if line:
                        if line.endswith(':'):
                            categoria_attuale = line[:-1]  # Rimuove i due punti alla fine della categoria
                        else:
                            if categoria_attuale:
                                # Aggiunge il pasto alla categoria corrente
                                self.aggiungi_pasto({
                                    'categoria': categoria_attuale,
                                    'nome': line
                                })

    # Aggiunge un pasto al menu
    def aggiungi_pasto(self, pasto):
        self.menu.append(pasto)
        self.salva_menu()

    # Salva il menu su file
    def salva_menu(self, nome_file="menu.pickle"):
        with open(nome_file, 'wb') as f:
            pickle.dump(self.menu, f)

    # Restituisce gli elementi del menu
    def get_menu_items(self):
        return self.menu
