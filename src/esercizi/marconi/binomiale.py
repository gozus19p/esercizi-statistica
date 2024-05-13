from statistica_metodologica import funzioni as f

# ESAME 07/04/23; 13/04/22

if __name__ == "__main__":
    print("""
    Un'impresa che produce tende da campeggio deve verificare a resistenza alla lacerazione del telo 
    principale di 10 tende prese a campione. La probabilità che una determinata tenda resista alla prova è 4/5. Si 
    calcoli la probabilità che 7 delle 10 tende superino la prova con successo.
    """)

    print("""
    Questo è il caso classico di applicazione della distribuzione binomiale di Bernoulli, che si usa in relazione a due
    soli possibili esiti: positivo o negativo. In questo esercizio, i positivi rappresentano le tende che resistono alla
    prova e sono 4/5, mentre i negativi si ottengono per complemento a 1.
    """)
    # "n" è la dimensione del campione
    n = 10

    # "k" è il numero di eventi favorevoli
    k = 7

    # "p" è la probabilità di successo e "q" la probabilità di insuccesso
    p = 4 / 5
    q = 1 - p
    print(f"Risultato: {f.dist_binomial(n, k, p)}")
