from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from gestione.gestore_mensa import SistemaMensa
from gestione.gestore_backup import GestoreBackup
from utenti.amministratore import Amministratore
from utenti.studente import Studente
from viste.abbonamento_view import AbbonamentoView
from viste.amministratore_view import AmministratoreView
from viste.ingresso_view import WelcomeView
from viste.login_view import LoginView
from viste.menu_view import MenuView
from viste.notifiche_view import NotificheView
from viste.pagamento_view import PagamentoView
from viste.prenotazione_view import PrenotazioneView
from viste.registrazione_view import RegistrazioneView
from viste.scorte_view import ScorteView
from viste.studente_view import StudenteView


class HomeView(QMainWindow):
    def __init__(self):
        super(HomeView, self).__init__()

        self.sistema_mensa = SistemaMensa()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.init_ui()
        self.gestore_backup = GestoreBackup(self.sistema_mensa)

    def init_ui(self):
        self.setWindowTitle('MangiAmo')
        self.welcome_view = WelcomeView()
        self.stacked_widget.addWidget(self.welcome_view)

        self.login_view = LoginView(self.sistema_mensa, self)
        self.login_view.login_success.connect(self.on_login_success)
        self.stacked_widget.addWidget(self.login_view)

        self.registrazione_view = RegistrazioneView(self.sistema_mensa, self)
        self.registrazione_view.registrazione_completata.connect(self.show_login_view)
        self.stacked_widget.addWidget(self.registrazione_view)

        # Example student and administrator registration
        studente = Studente(id=1, nome="Mario", cognome="Rossi", email="mario.rossi@studenti.univpm.it",
                            password="Password1?", numero_matricola="123456")
        self.sistema_mensa.registra_studente(studente)

        amministratore = Amministratore(id=2, nome="Luigi", cognome="Bianchi", email="luigi.bianchi@univpm.it",
                                        password="Admin2!")
        self.sistema_mensa.registra_amministratore(amministratore)

        self.menu = self.sistema_mensa.menu.carica_menu_da_file('menu.txt')
        self.notifiche = self.sistema_mensa.notifiche.carica_notifiche_da_file('notifiche.txt')

        self.studente_view = StudenteView(studente, self.sistema_mensa, self)
        self.stacked_widget.addWidget(self.studente_view)

        self.amministratore_view = AmministratoreView(amministratore, self.sistema_mensa, self)
        self.stacked_widget.addWidget(self.amministratore_view)

        self.menu_view = MenuView(self.sistema_mensa)
        self.stacked_widget.addWidget(self.menu_view)

        self.prenotazione_view = PrenotazioneView(studente, self.sistema_mensa, self)
        self.stacked_widget.addWidget(self.prenotazione_view)

        self.scorte_view = ScorteView(amministratore, self.sistema_mensa, self)
        self.stacked_widget.addWidget(self.scorte_view)

        self.pagamento_view = PagamentoView(studente, self.sistema_mensa, self)
        self.stacked_widget.addWidget(self.pagamento_view)

        self.notifiche_view = NotificheView(studente, self.sistema_mensa, self)
        self.stacked_widget.addWidget(self.notifiche_view)

        self.abbonamento_view = AbbonamentoView(studente, self.sistema_mensa)
        self.stacked_widget.addWidget(self.abbonamento_view)

        # Setting the welcome view at startup
        self.stacked_widget.setCurrentWidget(self.welcome_view)

    def on_login_success(self, utente):
        if isinstance(utente, Studente):
            self.studente_view.aggiorna_studente(utente)
            self.stacked_widget.setCurrentWidget(self.studente_view)
        elif isinstance(utente, Amministratore):
            self.amministratore_view.amministratore = utente
            self.stacked_widget.setCurrentWidget(self.amministratore_view)

    def show_login_view(self):
        self.stacked_widget.setCurrentWidget(self.login_view)
