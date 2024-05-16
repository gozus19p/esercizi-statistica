from esercizio import Esercizio, Out
import funzioni as f


class Threshold:
    lower_bound: float
    upper_bound: float

    def __init__(self, lower_bound: float, upper_bound: float):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return f"[{self.lower_bound}, {self.upper_bound})"


class Metodologica_1(Esercizio):

    def __init__(self):
        super().__init__("""Data la serie riportata, relativa al carattere X afferente ai giudizi riportati da 8 
        studenti ad un compito di matematica, determinarne: a) la media aritmetica; b) la mediana; c) la moda.""")

    # Restituire media, mediana e moda
    def execute(self) -> tuple[float, float, float]:
        pass


class Metodologica_2(Esercizio):
    def __init__(self):
        super().__init__("""Calcolare la media e la mediana della seguente distribuzione di frequenze: F(1-9)>.1 F(
        10-20)—>1 F(21:31)—> 10""")

    def execute(self) -> tuple[float, float]:
        pass


class Metodologica_3(Esercizio):
    def __init__(self):
        super().__init__("""Data la distribuzione di frequenze a seguire, relativa ad un carattere quantitativo 
        discreto X raggruppato in classi, determinarne: a) la media aritmetica e b) la mediana.

        | Altezza in cm | Frequenze assolute | Frequenze relative | Frequenze cumulate         |
        |---------------|--------------------|--------------------|----------------------------|
        | fino a 160    | 3                  |                    |                            |
        | 160 --- 170   | 3                  |                    |                            |
        | 170 --- 180   | 6                  |                    |                            |
        | 180 --- 190   | 4                  |                    |                            |
        | 190 --- 200   | 2                  |                    |                            |
        | oltre 200     | 4                  |                    |                            |
        | TOTALE        | 22                 |                    |                            |""")

    def execute(self) -> tuple[float, float]:
        pass

