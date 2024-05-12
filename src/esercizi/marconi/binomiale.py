from statistica_metodologica import funzioni as f

if __name__ == "__main__":
    print("""
    Un'impresa che produce tende da campeggio deve verificare a resistenza alla lacerazione del telo 
    principale di 10 tende prese a campione. La probabilità che una determinata tenda resista alla prova è 4/5. Si 
    calcoli la probabilità che 7 delle 10 tende superino la prova con successo.
    """)

    # Caso classico di impiego di una binomiale
    n = 10
    k = 7
    p = 4 / 5
    q = 1 - p
    print(f"Risultato: {(f.binomial_coefficient(n, k) * pow(p, k) * pow(q, n - k) * 100):.2f} %")
