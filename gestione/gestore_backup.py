import threading
import schedule
import time


class GestoreBackup:
    def __init__(self, sistema_mensa, backup_time="23:30"):
        self.sistema_mensa = sistema_mensa
        self.backup_time = backup_time
        self.thread = threading.Thread(target=self.run_scheduler, daemon=True)
        self.thread.start()

    def run_scheduler(self):
        schedule.every().day.at(self.backup_time).do(self.effettua_backup)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def effettua_backup(self):
        success = all([
            self.copia_dati_abbonamento(),
            self.copia_dati_prenotazione(),
            self.copia_dati_menu(),
            self.copia_dati_notifiche(),
            self.copia_dati_pagamenti(),
            self.copia_dati_pasti(),
            self.copia_dati_scorte()
        ])
        if success:
            print("Backup completato con successo.")
        else:
            print("Backup fallito.")

    def copia_dati_abbonamento(self):
        try:
            abbonamenti = self.sistema_mensa.get_abbonamenti()
            with open("backup_abbonamenti.txt", "w") as file:
                for abbonamento in abbonamenti:
                    file.write(f"{abbonamento}\n")
            return True
        except Exception as e:
            print(f"Errore nel copiare i dati degli abbonamenti: {e}")
            return False

    def copia_dati_prenotazione(self):
        try:
            prenotazioni = self.sistema_mensa.get_prenotazioni()
            with open("backup_prenotazioni.txt", "w") as file:
                for prenotazione in prenotazioni:
                    file.write(f"{prenotazione}\n")
            return True
        except Exception as e:
            print(f"Errore nel copiare i dati delle prenotazioni: {e}")
            return False

    def copia_dati_menu(self):
        try:
            menu = self.sistema_mensa.get_menu()
            with open("backup_menu.txt", "w") as file:
                for elemento in menu:
                    file.write(f"{elemento}\n")
            return True
        except Exception as e:
            print(f"Errore nel copiare i dati dei menu: {e}")
            return False

    def copia_dati_notifiche(self):
        try:
            notifiche = self.sistema_mensa.get_notifiche()
            with open("backup_notifiche.txt", "w") as file:
                for notifica in notifiche:
                    file.write(f"{notifica}\n")
            return True
        except Exception as e:
            print(f"Errore nel copiare i dati delle notifiche: {e}")
            return False

    def copia_dati_pagamenti(self):
        try:
            pagamenti = self.sistema_mensa.get_pagamenti()
            with open("backup_pagamenti.txt", "w") as file:
                for pagamento in pagamenti:
                    file.write(f"{pagamento}\n")
            return True
        except Exception as e:
            print(f"Errore nel copiare i dati dei pagamenti: {e}")
            return False

    def copia_dati_pasti(self):
        try:
            pasti = self.sistema_mensa.get_pasti()
            with open("backup_pasti.txt", "w") as file:
                for pasto in pasti:
                    file.write(f"{pasto}\n")
            return True
        except Exception as e:
            print(f"Errore nel copiare i dati dei pasti: {e}")
            return False

    def copia_dati_scorte(self):
        try:
            scorte = self.sistema_mensa.get_scorte()
            with open("backup_scorte.txt", "w") as file:
                for scorta in scorte:
                    file.write(f"{scorta}\n")
            return True
        except Exception as e:
            print(f"Errore nel copiare i dati delle scorte: {e}")
            return False
