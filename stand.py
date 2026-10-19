class Standard:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.codice = codice
        self.superficie = int(superficie)
        self.padiglione = int(padiglione)
        self.prezzo = float(prezzo)
        self.espositore = None

    def __lt__(self, other):
        return self.prezzo < other.prezzo

    def __str__(self):
        if self.espositore is None:
            stato = "Disponibile"
        else:
            stato = "Occupato"
        return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - {stato}"

class Premium(Standard):
    def __init__(self, codice, superficie, padiglione, prezzo, posizione):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.posizione = posizione
        self.prezzo = float(prezzo) * 1.30

    def __str__(self):
        if self.espositore is None:
            stato = "Disponibile"
        else:
            stato = "Occupato"
        return f"{self.codice}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - Posizione {self.posizione} - {stato}"

class Prese(Standard):
    def __init__(self, codice, superficie, padiglione, prezzo, n_prese):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.n_prese = int(n_prese)
        self.prezzo = float(prezzo) * (1 + 0.07 * self.n_prese)

    def __str__(self):
        if self.espositore is None:
            stato = "Disponibile"
        else:
            stato = "Occupato"
        return f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - Numero prese {self.n_prese} - {stato}"


