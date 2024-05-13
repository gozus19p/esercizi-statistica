import math
import scipy.stats as s

from statistica_metodologica import funzioni as f

if __name__ == '__main__':
    print("""
    Il contenuto in litri di 9 contenitori uguali d'acqua è pari rispettivamente a 19.8 — 20,1 — 20,0— 19,
    3- 19,9- 20,4 — 20,3 19,6 - 20,6. Trovare un intervallo di confidenza al 95% per il contenuto medio di questo 
    tipo di contenitori, assumendo che abbia distribuzione approssimativamente normale.
    """)

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
        19.8, 20.1, 20, 19.3, 19.9, 20.4, 20.3, 19.6, 20.6
    ]
    alpha = 0.05

    media_campionaria = f.mean(data)
    dev_std_campionaria = f.stdev(data, population=True)

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
