import unittest
from unittest.mock import MagicMock, patch, mock_open
from datetime import datetime, timedelta
import pickle
import os
from io import BytesIO
import sys
# Import delle classi dal tuo progetto
from funzionalità.pagamento import Pagamento
from funzionalità.abbonamento import Abbonamento
from funzionalità.menù import Menu
from funzionalità.notifiche import Notifiche
from funzionalità.pagamento import Pagamento
from funzionalità.prenotazione import Prenotazione
from funzionalità.scorte import Scorte
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


class TestSistemaMensa(unittest.TestCase):

    # Test per la classe Abbonamento
    @patch('funzionalità.abbonamento.pickle.load')
    @patch('funzionalità.abbonamento.open', new_callable=mock_open, read_data=pickle.dumps([]))
    def test_carica_abbonamenti_salvati(self, mock_open, mock_pickle_load):
        mock_pickle_load.return_value = []
        abbonamenti = Abbonamento.carica_abbonamenti_salvati()
        self.assertIsInstance(abbonamenti, list)

    @patch('funzionalità.abbonamento.pickle.dump')
    @patch('funzionalità.abbonamento.open', new_callable=mock_open)
    def test_salva_abbonamenti(self, mock_open, mock_pickle_dump):
        Abbonamento.salva_abbonamenti([])
        mock_pickle_dump.assert_called_once_with([], mock_open().__enter__())

    def test_aggiungi_abbonamento(self):
        abbonamento = Abbonamento()
        data_inizio = datetime.now()
        data_scadenza = data_inizio + timedelta(days=30)
        abbonamento.aggiungi_abbonamento("codice123", data_inizio, data_inizio, data_scadenza)
        self.assertEqual(abbonamento.codice, "codice123")
        self.assertEqual(abbonamento.data_inizio, data_inizio)
        self.assertEqual(abbonamento.data_rilascio, data_inizio)
        self.assertEqual(abbonamento.data_scadenza, data_scadenza)

    def test_verifica_scaduto(self):
        abbonamento = Abbonamento(data_scadenza=datetime.now() - timedelta(days=1))
        self.assertTrue(abbonamento.verifica_scaduto())

    def test_aggiungi_pasto(self):
        menu = Menu()
        pasto = {'categoria': 'Categoria1', 'nome': 'Pasto1'}
        menu.aggiungi_pasto(pasto)
        self.assertIn(pasto, menu.menu)

    # Test per la classe Notifiche
    @patch('funzionalità.notifiche.open', new_callable=mock_open, read_data="Notifica1\nNotifica2\n")
    def test_carica_notifiche_da_file(self, mock_open):
        notifiche = Notifiche()
        notifiche.carica_notifiche_da_file()
        self.assertEqual(len(notifiche.get_notifiche()), 2)

    def test_aggiungi_notifica(self):
        notifiche = Notifiche()
        notifiche.aggiungi_notifica("Nuova Notifica")
        self.assertIn("Nuova Notifica", notifiche.get_notifiche())

    # Test per la classe Pagamento
    def setUp(self):
        self.studente_mock = MagicMock()
        self.sistema_mensa_mock = MagicMock()
        self.view_mock = MagicMock()
        self.pagamento = Pagamento(
            "Mario", "Rossi", "1234567812345678", "12", "2024", "123",
            10, self.studente_mock, self.sistema_mensa_mock, self.view_mock
        )

    def test_valida_carta_credito(self):
        self.assertTrue(self.pagamento.valida_carta_credito())

    def test_valida_data_scadenza(self):
        self.assertTrue(self.pagamento.valida_data_scadenza())

    def test_valida_cvv(self):
        self.assertTrue(self.pagamento.valida_cvv())

    # Test per la classe Prenotazione
    def test_prenotazione_get_info(self):
        self.studente_mock = MagicMock()
        pasto = "Pasta"
        prenotazione = Prenotazione(self.studente_mock, pasto)
        info = prenotazione.get_info()
        self.assertEqual(info['pasto'], "Pasta")

    # Test per la classe Scorte
    @patch('funzionalità.scorte.open', new_callable=mock_open)
    @patch('funzionalità.scorte.pickle.load')
    def test_carica_scorte_da_file(self, mock_pickle_load, mock_open):
        mock_pickle_load.return_value = []
        scorte = Scorte()
        with patch('builtins.open', new_callable=lambda: mock_open(read_data=BytesIO(pickle.dumps([])).getvalue())):
            scorte.carica_scorte_da_file()
        self.assertIsInstance(scorte.get_scorte(), list)

    def test_aggiungi_scorta(self):
        scorte = Scorte()
        scorte.aggiungi_scorta("Ingrediente1", 10)
        self.assertIn({'ingrediente': 'Ingrediente1', 'quantita': 10}, scorte.get_scorte())


if __name__ == '__main__':
    unittest.main()
