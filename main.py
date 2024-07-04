import sys
from PyQt5.QtWidgets import QApplication
from viste.VistaHome import HomeView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HomeView()
    main_window.show()
    sys.exit(app.exec_())

# credenziali per l'accesso ai profili di prova
# studente
# email : mario.rossi@studenti.univpm.it
# password : Password1?
# amministratore
# email : luigi.bianchi@univpm.it
# password : Admin2!
