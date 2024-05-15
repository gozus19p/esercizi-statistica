import math
from statistica_metodologica import funzioni as f
from esercizi.marconi.due_campioni import DueCampioni


def soluzione() -> tuple[float, float]:
    print("""
    Per confrontare 2 tipi di motore A e B, è stato condotto uno studio sui chilometri percorsi con una data quantità di
    combustibile in litri. Sono stati fatti 60 esperimenti con il motore A, 70 con il motore B. Tipo di combustibile e
    altre variabili sono considerati costanti. Con il motore A si sono percorsi mediamente 16 chilometri litro, mentre
    con il motore B se ne sono percorsi 19. Trovare un intervallo di confidenza al 96% per mu_b - mu_a assumendo che la
    deviazione standard sia 4 per il motore A e 5 per il motore B.
    """)

    n_a = 60
    n_b = 70
    mu_a = 16
    mu_b = 19
    alpha = 0.04 / 2
    dev_a = 4
    dev_b = 5
    variance_a = pow(dev_a, 2)
    variance_b = pow(dev_b, 2)

    z = f.norm(1 - alpha)
    r = z * math.sqrt(variance_a / n_a + variance_b / n_b)

    upper = mu_b - mu_a + r
    lower = mu_b - mu_a - r
    return lower, upper


def test_due_campioni():
    lower, upper = DueCampioni().execute()
    lower_e, upper_e = soluzione()
    assert lower == lower_e
    assert upper == upper_e
