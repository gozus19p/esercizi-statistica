import funzioni as f
from marconi import probabilita


def test_binomiale():
    n = 10
    k = 7
    p = 4 / 5

    binomial = f.binomial_coefficient(n, k) * (p ** k) * ((1 - p) ** (n - k))
    assert probabilita.Binomiale().execute() == binomial


def test_binomiale_2():
    print("""
        Si prenda in considerazione un concorso pubblico e in particolare l'esecuzione della prova preselettiva basata su un
        test a risposta multipla composto da 200 domande. Per ogni domanda ci sono 4 risposte alternative e solo una delle 4
        è corretta. Si supponga che il candidato non sia preparato e che pertanto non sappia rispondere al test. Si calcoli
        la probabilità che, rispondendo casualmente a 80 delle 200 domande del test, il candidato riesca a rispondere
        correttamente ai quesiti compresi in un intorno tra 25 e 30. La probabilità che il candidato individui casualmente
        la risposta corretta per gli 80 quesiti è pari a p=1/4.
        """)

    print("""
        In questo caso, occorre calcolare la binomiale in tutti i discreti compresi tra 25 e 30 e sommare la relativa
        probabilità.
        """)

    n = 80
    p = 1 / 4
    binomial = 0.0
    for k in range(25, 31):
        res = f.dist_binomial(n, k, p)
        print(f"Binomiale per n={n}, k={k}, p={p}: {res}")
        binomial += res
    assert probabilita.Binomiale2().execute() == binomial
