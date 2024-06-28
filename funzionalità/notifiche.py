import os


class Notifiche:
    def __init__(self):
        self.notifiche = []
        self.carica_notifiche_da_file()

    def carica_notifiche_da_file(self, nome_file="notifiche.txt"):
        if os.path.isfile(nome_file):
            with open(nome_file, 'r') as f:
                self.notifiche = [line.strip() for line in f if line.strip()]

    def aggiungi_notifica(self, messaggio):
        self.notifiche.append(messaggio)
        with open("notifiche.txt", "a") as file:
            file.write(f"{messaggio}\n")

    def get_notifiche(self):
        return self.notifiche
