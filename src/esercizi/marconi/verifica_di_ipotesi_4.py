import math

from statistica_metodologica import funzioni as f

if __name__ == "__main__":
    print("""
    Un produttore di attrezzature sportive ha sviluppato un nuovo tipo di lenza che si sostiene abbia un carico a 
    rottura medio di 9 chili, con una deviazione standard pari a 0,8 chili. Viene testato un campione casuale di 60
    lenze, e viene calcolato un carico a rottura medio di 8,4 chili. Verificare l'ipotesi mu=9 chili contro l'ipotesi 
    alternativa mu!=9 chili. Adottare un livello di significatività 0,01.
    """)
    mu = 9
    dev_std = 0.8
    n = 60
    mu_c = 8.4
    alpha = 0.01

    z = (mu_c - mu) / dev_std * math.sqrt(n)
    cv = f.norm((alpha / 2))
    if z < cv:
        print(f"Si rifiuta H0 perché z={z} < cv={cv}")
    else:
        print(f"Non si rifiuta H0 perché z={z} >= cv={cv}")
