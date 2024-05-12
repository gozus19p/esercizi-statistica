import math
from statistica_metodologica import funzioni as f


def esercizio():

    # H0 asserisce che p sia esattamente uguale a 0.70, H1 asserisce che sia diverso da 0.70 (test bilaterale)
    p0 = 0.70

    # Occorre determinare la dimensione campionaria su una popolazione di 15 case, di cui 11 risultano dotate di pompe
    n = 15
    X = 11
    p_hat = X / n
    print(f"p_hat = {p_hat}")

    # Calcolo della statistica z
    z = (p_hat - p0) / math.sqrt((p0 * (1 - p0)) / n)

    # Dalle tavole, risulta che per alpha = 0,05 (essendo bilaterale, divido in 2 il valore 0,10) il valore critico sia
    # pari a 1.64
    alpha_abs = 1.64
    if z < alpha_abs:
        print(f"Non si rifiuta H0, perché z={z} è minore del valore critico a={alpha_abs}")
    else:
        print(f"Si rifiuta H0, perché z={z} è maggiore o uguale del valore critico a={alpha_abs}")


def esercizio_con_binomiale():
    n = 15
    k = 11
    p0 = 0.70
    q = 1 - p0

    p_value = 1 - (f.binomial_coefficient(n, k) * pow(p0, k) * pow(q, n - k))
    print(f"P-value = {p_value}, valore significatività = 0.05")
    if p_value < 0.05:
        print(f"Si rifiuta H0 in favore di H1 perché p-value={p_value} < 0.05")
    else:
        print(f"Non si rifiuta H0 perché p-value={p_value} >= 0.05")


if __name__ == '__main__':

    print(f""" Un costruttore asserisce che le pompe di calore vengono installate nel 70% delle case di nuova 
    costruzione nella città di Asti. Sei d'accordo con questa affermazione se, in base a un'indagine campionaria 
    sulle nuove case della città, si evidenzia che 11 su 15 sono dotate di pompe di calore? Imposta un livello di 
    significatività pari a 0,10. """)
    print("===== SVOLGIMENTO CON TAVOLE Z")
    esercizio()
    print("===== SVOLGIMENTO CON BINOMIALE")
    esercizio_con_binomiale()
