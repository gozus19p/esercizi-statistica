from statistica_metodologica import funzioni as f

if __name__ == "__main__":
    print("""
    Un costruttore asserisce che le pompe di calore vengono installate nel 75% delle case di nuova 
    costruzione nella città di Grosseto. Sei d’accordo con questa affermazione se in base ad un’indagine campionaria 
    sulle nuove case della città si evidenzia che 10 su 15 sono dotate di pompe di calore? Impostare un livello di 
    significatività pari a 0,10.
    """)
    n = 15
    k = 10
    ls = 0.10
    p = 0.75
    alpha = ls / 2 # Test bilaterale

    binomiale = f.binomial_coefficient(n, k) * pow(p, k) * pow(1 - p, n - k)
    p_value = 1 - binomiale
    print(f"Binomiale: {binomiale}, p-value: {p_value}")
    if p_value < ls:
        print("Si rifiuta H0 in favore di H1")
    else:
        print("Non si rifiuta H0")