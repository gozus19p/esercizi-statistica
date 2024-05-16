import math
import funzioni as f
from esercizio import Esercizio, Out


class DueCampioni(Esercizio):

    def __init__(self):
        super() \
            .__init__(
            """Per confrontare 2 tipi di motore A e B, è stato condotto uno studio sui chilometri percorsi con una 
            data quantità di combustibile in litri. Sono stati fatti 60 esperimenti con il motore A, 70 con il motore 
            B. Tipo di combustibile e altre variabili sono considerati costanti. Con il motore A si sono percorsi 
            mediamente 16 chilometri litro, mentre con il motore B se ne sono percorsi 19. Trovare un intervallo di 
            confidenza al 96% per mu_b - mu_a assumendo che la deviazione standard sia 4 per il motore A e 5 per il 
            motore B."""
        )

    def execute(self) -> tuple[float, float]:
        pass
