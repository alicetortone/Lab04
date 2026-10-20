class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.stand = None

    def __eq__(self, other):
        if isinstance(other, Espositore):
            return self.codice == other.codice
        return False

    def __str__(self):
        if self.stand is not None:
            stand_info = self.stand.codice
        else:
            stand_info = "Nessuno"
        return f"{self.codice}: {self.nome} {self.cognome} - Stand: {stand_info}"
