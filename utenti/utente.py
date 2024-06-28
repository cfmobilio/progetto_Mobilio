class Utente:
    def __init__(self, id, nome, cognome, email, password):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.password = password

    def get_info(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "email": self.email,
        }

    def verifica_password(self, password):
        return self.password == password
