import math
import funzioni as f
import marconi.verifica_di_ipotesi as vi
from scipy import stats as s


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
    # e della popolazione) e al denominatore la dev.std diviso la radice di n
    mu_p = 6
    n = 100
    dev_std = 0.15
    mu_c = 6.034

    # Non essendo stato specificato il livello di significatività, lo definiamo a 0.05
    alpha = 0.05

    z = (mu_c - mu_p) / dev_std / math.sqrt(n)

    # Il calcolo del p-value calcola il doppio del risultato del valore critico di z perché il test in questione è
    # bilaterale
    p_value = 2 * f.norm(1 - z)
    expected = p_value < alpha
    assert vi.VerificaDiIpotesi_3().execute() == expected


def test_verifica_di_ipotesi_4():
    mu = 9
    dev_std = 0.8
    n = 60
    mu_c = 8.4
    alpha = 0.01

    z = (mu_c - mu) / dev_std * math.sqrt(n)
    cv = f.norm((alpha / 2))
    expected = (cv > z >= 0) or (cv < z <= 0)
    assert vi.VerificaDiIpotesi_4().execute() == expected


def test_verifica_di_ipotesi_5():
    p = 0.70
    n = 180
    k = 140
    p_hat = k / n
    alpha = 0.01

    # H0 -> p<=0.7, H1 -> p>0.7
    z = (p_hat - p) / math.sqrt(p * (1 - p) / n)

    # Valore massimo per cui l'ipotesi nulla risulta falsa, se calcolo il complemento a 1 sto calcolando il valore
    # massimo per cui non rifiuto l'ipotesi nulla (l'inverso)
    cv = f.norm(1 - alpha)
    expected = (cv > z >= 0) or (cv < z <= 0)
    assert vi.VerificaDiIpotesi_5().execute() == expected


def test_verifica_di_ipotesi_6():
    n = 200
    mu = 69
    dev_std = 9.3
    mu_c = 72.4
    alpha = 0.05

    # H0 -> mu<=69, H1 -> mu > 69

    z = (mu_c - mu) / dev_std / math.sqrt(n)
    p_value = 1 - f.norm(z)
    expected = p_value < alpha
    assert vi.VerificaDiIpotesi_6().execute() == expected


def test_verifica_di_ipotesi_7():
    print("""
    In questo caso si usa la T di Student. I passaggi da fare sono:
    1) Calcolare la media campionaria.
    2) Calcolare la deviazione standard campionaria.
    3) Calcolare l'errore standard (dev.std. diviso radq(n)).
    4) Tramite la T di Student trovare il valore critico per 1 - alpha/2 (divido per due perché con la T ho due code, è
       simmetrica).
    5) Calcolo il margine d'errore facendo il prodotto tra errore standard e valore critico.
    6) Alla media campionaria aggiungo e tolgo il margine d'errore, individuando l'intervallo desiderato.
    """)
    data = [
        19.8, 20.1, 20.0, 19.3, 19.9, 20.4, 20.3, 19.6, 20.6
    ]
    alpha = 0.05

    media_campionaria = f.mean(data)
    dev_std_campionaria = f.stdev(data, population=False)

    n = len(data)
    errore_standard = dev_std_campionaria / math.sqrt(n)
    cv = s.t.ppf(1 - (alpha / 2), df=n - 1)
    print(f"Il valore critico è:                        {cv}")

    margine_errore = errore_standard * cv
    print(f"Il margine d'errore è:                      {margine_errore}")
    superiore = media_campionaria + margine_errore
    inferiore = media_campionaria - margine_errore
    print(f"La media campionaria è:                     {media_campionaria}")
    print(f"Gli intervalli inferiore e superiore sono:  {inferiore} e {superiore}")
    inferiore_r, superiore_r = vi.VerificaDiIpotesi_7().execute()
    assert inferiore == inferiore_r
    assert superiore == superiore_r
