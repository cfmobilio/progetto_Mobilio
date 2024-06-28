import os
import pickle
import unittest
from datetime import datetime, timedelta
from funzionalità.abbonamento import Abbonamento
from funzionalità.menù import Menu
from funzionalità.notifiche import Notifiche
from funzionalità.pagamento import Pagamento
from funzionalità.pasto import Pasto
from funzionalità.prenotazione import Prenotazione
from funzionalità.scorte import Scorte
from utenti.amministratore import Amministratore
from utenti.utente import Utente


class TestAbbonamento(unittest.TestCase):

    def setUp(self):
        # Create the directory if it doesn't exist
        if not os.path.exists('Dati'):
            os.makedirs('Dati')

        # Initialize the abbonamento instance
        self.abbonamento = Abbonamento("123", datetime.now(), datetime.now(), datetime.now() + timedelta(days=30), True)

        # Ensure the file is empty for a fresh start
        with open('Dati/abbonamenti.pickle', 'wb') as f:
            pickle.dump([], f)

    def tearDown(self):
        # Clean up the directory after tests
        if os.path.exists('Dati/abbonamenti.pickle'):
            os.remove('Dati/abbonamenti.pickle')
        if os.path.exists('Dati'):
            os.rmdir('Dati')

    def test_aggiungi_abbonamento(self):
        self.abbonamento.aggiungi_abbonamento("123", datetime.now(),
                                              datetime.now(), datetime.now() + timedelta(days=30), True)
        abbonamenti = self.abbonamento.carica_abbonamenti_salvati()
        self.assertEqual(len(abbonamenti), 1)
        self.assertEqual(abbonamenti[0]["codice"], "123")

    def test_verifica_scaduto(self):
        self.assertFalse(self.abbonamento.verifica_scaduto())
        abbonamento_scaduto = Abbonamento("124", datetime.now() - timedelta(days=60),
                                          datetime.now() - timedelta(days=60),
                                          datetime.now() - timedelta(days=30), True)
        self.assertTrue(abbonamento_scaduto.verifica_scaduto())


class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.menu.menu = []  # Resetta il menu per ogni test

    def test_aggiungi_pasto(self):
        pasto = {"categoria": "Primi", "nome": "Spaghetti"}
        self.menu.aggiungi_pasto(pasto)
        self.assertIn(pasto, self.menu.get_menu_items())

    def test_carica_menu_da_file(self):
        with open("menu.txt", "w") as f:
            f.write("Primi:\nSpaghetti\n")
        self.menu.carica_menu_da_file("menu.txt")
        self.assertEqual(len(self.menu.get_menu_items()), 1)
        self.assertEqual(self.menu.get_menu_items()[0]['nome'], "Spaghetti")
        os.remove("menu.txt")


class TestNotifiche(unittest.TestCase):

    def setUp(self):
        self.notifiche = Notifiche()

    def test_aggiungi_notifica(self):
        self.notifiche.aggiungi_notifica("Nuova notifica")
        self.assertIn("Nuova notifica", self.notifiche.get_notifiche())


class TestPagamento(unittest.TestCase):

    def setUp(self):
        self.pagamento = Pagamento(1, 101, 50, "carta")

    def test_get_info(self):
        info = self.pagamento.get_info()
        self.assertEqual(info["id"], 1)
        self.assertEqual(info["importo"], 50)


class TestPasto(unittest.TestCase):

    def setUp(self):
        self.pasto = Pasto(1, "Pizza", "Pizza Margherita", 8.50)

    def test_get_info(self):
        info = self.pasto.get_info()
        self.assertEqual(info["nome"], "Pizza")
        self.assertEqual(info["prezzo"], 8.50)


class TestPrenotazione(unittest.TestCase):

    def setUp(self):
        self.studente = Utente(1, "Mario", "Rossi", "mario.rossi@example.com", "password")
        self.pasto = Pasto(1, "Pizza", "Pizza Margherita", 8.50)
        self.prenotazione = Prenotazione(self.studente, self.pasto)

    def test_get_info(self):
        info = self.prenotazione.get_info()
        self.assertEqual(info["pasto"]["nome"], "Pizza")
        self.assertEqual(info["studente"]["nome"], "Mario")


class TestScorte(unittest.TestCase):

    def setUp(self):
        self.scorte = Scorte()

    def test_aggiungi_scorta(self):
        self.scorte.aggiungi_scorta("Pomodoro", 10)
        self.assertIn({"ingrediente": "Pomodoro", "quantita": 10}, self.scorte.get_scorte())


class TestAmministratore(unittest.TestCase):

    def setUp(self):
        self.amministratore = Amministratore(1, "Luca", "Bianchi", "luca.bianchi@example.com", "password")

    def test_gestisci_menu(self):
        nuovo_menu = [{"categoria": "Primi", "nome": "Pasta"}]
        result = self.amministratore.gestisci_menu(nuovo_menu)
        self.assertEqual(result, "Menu aggiornato")
        self.assertEqual(self.amministratore.menu, nuovo_menu)

    def test_aggiorna_scorte(self):
        result = self.amministratore.aggiorna_scorte("Pomodoro", 10)
        self.assertEqual(result, "Scorte di Pomodoro aggiornate a 10")
        self.assertEqual(self.amministratore.scorte["Pomodoro"], 10)


if __name__ == '__main__':
    unittest.main()
