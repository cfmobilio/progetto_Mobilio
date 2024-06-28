from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QMessageBox

from viste.studente_view import StudenteView


class MenuView(QWidget):
    def __init__(self, sistema_mensa, parent=None):
        super(MenuView, self).__init__(parent)
        self.sistema_mensa = sistema_mensa
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.menu_label = QLabel('Menu del giorno:')
        layout.addWidget(self.menu_label)

        self.menu_list = QListWidget()
        layout.addWidget(self.menu_list)

        self.setLayout(layout)
        self.update_menu()  # Sposta qui la chiamata per mantenere pulita la funzione init_ui

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

        self.menu_list.clear()
        pasto_type = None
        count_per_type = {'primo': 0, 'secondo': 0, 'contorno': 0}
        for line in menu_lines:
            if line.startswith("Primo piatto:"):
                pasto_type = "primo"
                count_per_type['primo'] = 0
                self.menu_list.addItem("Primo piatto:")
            elif line.startswith("Secondo piatto:"):
                pasto_type = "secondo"
                count_per_type['secondo'] = 0
                self.menu_list.addItem("Secondo piatto:")
            elif line.startswith("Contorno:"):
                pasto_type = "contorno"
                count_per_type['contorno'] = 0
                self.menu_list.addItem("Contorno:")
            elif line.strip() and count_per_type[pasto_type] < 2:
                # Mostriamo solo le prime due opzioni per ogni tipo di portata
                self.menu_list.addItem(line.strip())
                count_per_type[pasto_type] += 1

    def show_studente_view(self, studente):
        self.studente_view = StudenteView(studente, self.sistema_mensa)
        self.studente_view.show()
