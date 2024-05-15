import math
from statistica_metodologica import funzioni as f
import esercizi.marconi.verifica_di_ipotesi as vi


def test_verifica_di_ipotesi():
    # Con N non significativamente grande (regola empirica N < 30), si può svolgere l'esercizio anche con una binomiale
    n = 15
    k = 11
    p0 = 0.70

    # Per calcolare il p-value sottraggo a 1 il risultato della binomiale di Bernoulli
    p_value = 1 - f.dist_binomial(n, k, p0)
    alpha = 0.10

    # Divido alpha per 2 perché il test è a due code, vogliamo assumere H1 = p0 != 0.7
    alpha /= 2

    # Se vero, non si rifiuta H0
    expected = p_value > alpha / 2
    assert vi.VerificaDiIpotesi().execute() == expected


def test_verifica_di_ipotesi_2():
    p0 = 0.75
    n = 15
    k = 10
    alpha = 0.10

    # Dato che il test è bilaterale (H1 --> !=H0) dividiamo alpha per 2
    alpha /= 2

    # Si effettua un test statistico per la proporzione del campione, calcolando la proporzione campionaria
    p_hat = k / n
    z = (p_hat - p0) / math.sqrt(p0 * (1 - p0) / n)
    cv = f.norm(1 - alpha)
    cv_n = -cv
    expected = cv_n < z < cv
    assert vi.VerificaDiIpotesi_2().execute() == expected


def test_verifica_di_ipotesi_3():
    # In questo caso, occorre calcolare la distribuzione z con al numeratore la differenza delle due medie (campionaria
    # e della popolazione) e al denominatore la dev.std per la radice di n
    mu_p = 6
    n = 100
    dev_std = 0.15
    mu_c = 6.034

    # Non essendo stato specificato il livello di significatività, lo definiamo a 0.05
    alpha = 0.05

    # Lo si divide in 2 perché il test è bilaterale, ha due code
    alpha /= 2

    z = (mu_c - mu_p) / dev_std * math.sqrt(n)
    cv = f.norm(1 - alpha)
    expected = (cv > z >= 0) or (cv < z <= 0)
    assert vi.VerificaDiIpotesi_3().execute() == expected
