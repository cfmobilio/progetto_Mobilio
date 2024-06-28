class Pasto:
    def __init__(self, id, nome, descrizione, prezzo):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.prezzo = prezzo

    # Metodo per ottenere le informazioni del pasto
    def get_info(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descrizione": self.descrizione,
            "prezzo": self.prezzo
        }

    # Metodo per rappresenrazione testuale
    def __str__(self):
        return f"{self.nome} - {self.descrizione} ({self.prezzo}€)"
