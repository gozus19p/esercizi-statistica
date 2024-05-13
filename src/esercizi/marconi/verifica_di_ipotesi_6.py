import math
from statistica_metodologica import funzioni as f

if __name__ == "__main__":
    print("""
    Un campione casuale di 200 decessi occorsi quest'anno in Italia ha evidenziato una vita media di 72,4 anni.
    Assumendo una deviazione ‘standard di 9,3 anni, si può concludere che la vita media è maggiore di 69 anni? Adottare
    un livello di significatività pari a 0,05.
    """)
    n = 200
    mu = 69
    dev_std = 9.3
    mu_c = 72.4
    alpha = 0.05

    # H0 -> mu<=69, H1 -> mu > 69

    z = (mu_c - mu) / dev_std * math.sqrt(n)
    cv = f.norm(1 - alpha)
    if 0 <= z <= cv:
        print("Non si rifiuta H0")
    else:
        print("Si rifiuta H0")
    print(z, cv)
