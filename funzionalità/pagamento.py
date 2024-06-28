class Pagamento:
    def __init__(self, id, studente_id, importo, metodo):
        # Inizializza un'istanza di Pagamento con le informazioni specificate.
        self.id = id
        self.studente_id = studente_id
        self.importo = importo
        self.metodo = metodo

    def get_info(self):
        # Restituisce le informazioni del pagamento come dizionario.
        # Le chiavi sono 'id', 'studente_id', 'importo' e 'metodo'.
        return {
            "id": self.id,
            "studente_id": self.studente_id,
            "importo": self.importo,
            "metodo": self.metodo
        }
