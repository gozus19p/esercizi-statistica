from statistica_metodologica import funzioni as f


# ESAME 06/02/23; 26/03/24

def esercizio():
    # H0 asserisce che p sia esattamente uguale a 0.70, H1 asserisce che sia diverso da 0.70 (test bilaterale)
    p0 = 0.70

    # Occorre determinare la dimensione campionaria su una popolazione di 15 case, di cui 11 risultano dotate di pompe
    n = 15
    X = 11

    # Calcolo della statistica z sulla distribuzione normale
    z = f.test_z_normale(n, X, p0)

    # Calcolo il valore critico per alpha = 0,05 (essendo bilaterale, divido in 2 il valore 0,10)
    alpha = 0.10
    cv = f.norm(1 - alpha / 2)
    if z < cv:
        print(f"Non si rifiuta H0, perché z={z} è minore del valore critico a={cv}")
    else:
        print(f"Si rifiuta H0, perché z={z} è maggiore o uguale del valore critico a={cv}")


def esercizio_con_binomiale():
    n = 15
    k = 11
    p0 = 0.70

    # Per calcolare il p-value sottraggo a 1 il risultato della binomiale di Bernoulli
    p_value = 1 - f.dist_binomial(n, k, p0)
    print(f"P-value = {p_value}, valore significatività = 0.05")
    alpha = 0.10
    if p_value < alpha / 2:
        print(f"Si rifiuta H0 in favore di H1 perché p-value={p_value} < 0.05")
    else:
        print(f"Non si rifiuta H0 perché p-value={p_value} >= 0.05")


if __name__ == '__main__':
    print(f""" Un costruttore asserisce che le pompe di calore vengono installate nel 70% delle case di nuova 
    costruzione nella città di Asti. Sei d'accordo con questa affermazione se, in base a un'indagine campionaria 
    sulle nuove case della città, si evidenzia che 11 su 15 sono dotate di pompe di calore? Imposta un livello di 
    significatività pari a 0,10. """)

    print("""
    Con N non sufficientemente grande, si può svolgere l'esercizio anche con la binomiale. A titolo didattico, si
    riportano entrambi gli svolgimenti""")

    print("===== SVOLGIMENTO CON TAVOLE Z")
    esercizio()
    print("===== SVOLGIMENTO CON BINOMIALE")
    esercizio_con_binomiale()
