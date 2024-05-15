import math
from statistica_metodologica import funzioni as f
from esercizi.esercizio import Esercizio, Out


class DueCampioni(Esercizio):

    def __init__(self):
        super() \
            .__init__(
            "Esercizio su stima media di due campioni",
            """Per confrontare 2 tipi di motore A e B, è stato condotto uno studio sui chilometri percorsi con una 
            data quantità di combustibile in litri. Sono stati fatti 60 esperimenti con il motore A, 70 con il motore 
            B. Tipo di combustibile e altre variabili sono considerati costanti. Con il motore A si sono percorsi 
            mediamente 16 chilometri litro, mentre con il motore B se ne sono percorsi 19. Trovare un intervallo di 
            confidenza al 96% per mu_b - mu_a assumendo che la deviazione standard sia 4 per il motore A e 5 per il 
            motore B."""
        )

    def execute(self) -> tuple[float, float]:
        n_a = 60
        n_b = 70
        mu_a = 16
        mu_b = 19
        alpha = 0.04 / 2
        dev_std_a = 4
        dev_std_b = 5
        z = f.norm(1 - alpha)
        conf = z * math.sqrt((pow(dev_std_a, 2) / n_a) + (pow(dev_std_b, 2) / n_b))
        return (mu_b - mu_a) - conf, (mu_b - mu_a) + conf
