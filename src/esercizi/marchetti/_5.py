import math
from statistica_metodologica import funzioni as f

"""
5) Eserciziario su variabili casuali discrete.

1. Funzione di probabilità
2. Funzione di ripartizione
3. Valore atteso
4. Varianza
5. Binomiale
"""


def separa():
    print("================================================================================")


def esercizio_5_3():
    global data
    print("""
    >>> 5.3
    
    Il numero di volte che uno studente ripete l’esame di statistica è una variabile casuale X con distribuzione
    x, P(x)
    1, 0.5
    2, 0.25
    3, 0.15
    4, 0.1
    
    Calcolare la probabilità che uno studente:
    a) ripeta l’esame più di una volta.
    b) ripeta l’esame almeno 2 volte.
    c) ripeta l’esame al massimo 2 volte.
    """)
    # Si definisce la tabella dei dati composta dalle x e dalle P(x)
    data = [
        [1, 0.5],
        [2, 0.25],
        [3, 0.15],
        [4, 0.1]
    ]
    # Si calcola la sommatoria della probabilità per cui X>1
    p_gt1 = sum([y for x, y in data if x > 1])
    print(f"La probabilità che ripeta l'esame più di una volta è data da P(X>1):        {p_gt1}")

    # Si calcola la sommatoria della probabilità per cui X>=2
    p_gte2 = sum([y for x, y in data if x >= 2])
    print(f"La probabilità che ripeta l'esame almeno due volte è data da P(X>=2):       {p_gte2}")

    # Si calcola la sommatoria della probabilità per cui X<=2
    p_lte2 = sum([y for x, y in data if x <= 2])
    print(f"La probabilità che ripeta l'esame al massimo due volte è data da P(X<=2):   {p_lte2}")
    separa()


def esercizio_5_4():
    print("""
    >>> 5.4
    
    Calcolare il valore atteso e la deviazione standard di X (rif. 5.3).
    """)
    data_5_4 = [
        [1, 0.5],
        [2, 0.25],
        [3, 0.15],
        [4, 0.1]
    ]
    # Il valore atteso è dato dalla sommatoria di tutte le x*y, dove x, ricordiamo, rappresenta il numero di ripetizioni
    # dell'esame e y la probabilità che ciò succeda. Così facendo, viene fuori E(X)
    e_x_ = sum([x * y for x, y in data_5_4])
    print(f"E(X) = {e_x_}")

    # Per calcolare la varianza e la conseguente deviazione standard si ricorre alla formula E(X^2) - E(X)^2
    # E(X^2) è dato da una formula simile alla precedente, con la differenza che si eleva al quadrato x
    e_x2_ = sum([pow(x, 2) * y for x, y in data_5_4])
    print(f"E(X)^2 = {e_x2_}")

    varianza_ = e_x2_ - pow(e_x_, 2)
    print(f"Varianza = {varianza_}")
    print(f"Dev.std = {math.sqrt(varianza_)}")
    separa()


def esercizio_5_5():
    global data
    print("""
    >>> 5.5
    
    Supponi di avere un urna con i numeri {1, 2, 3} e di pescarne 2 SENZA ripetizione. Descrivi lo spazio
    campionario che contiene tutti i campioni di due elementi senza ripetizione.
    """)
    data_5_5 = [1, 2, 3]
    print(f"{data_5_5[0]}, {data_5_5[1]}")
    print(f"{data_5_5[1]}, {data_5_5[2]}")
    print(f"{data_5_5[0]}, {data_5_5[2]}")
    separa()


def esercizio_5_6():
    print("""
    >>> 5.6
    
    Considera ora la variabile casuale X = somma dei numeri estratti (rif.5.5). Determina la sua distribuzione di
    probabilità e calcolane il valore atteso.
    """)
    data_5_6 = [
        [3, 1 / 3],
        [4, 1 / 3],
        [5, 1 / 3]
    ]
    print(f"La distribuzione di probabilità è: {data_5_6}")
    print(f"Il valore atteso è dato dalla somma di tutti gli x*y: {sum([x * y for x, y in data_5_6])}")
    print()
    separa()


def esercizio_5_7():
    print("""
    >>> 5.7
    
    Si tirano 4 monete. Qual è la probabilità che escano tutte teste?
    """)
    p_testa = 0.5
    print(f"La probabilità è data da P^4 (4 lanci indipendenti con 4 successi): {pow(p_testa, 4)}")
    print()
    separa()


def esercizio_5_9():
    print("""
    >>> 5.9
    
    Per andare da Piazza del Popolo a Piazza Italia ci sono 4 semafori indipendenti ognuno dei quali è verde con
    probabilità 0.3. Qual è la probabilità che guidando da PP a PI non si trovi mai un semaforo verde?
    """)
    p_5_9 = 0.3
    q_5_9 = 1 - p_5_9
    print(f"La probabilità è data da q^4: {pow(q_5_9, 4)}")
    print()
    separa()


def esercizio_5_10():
    global tentativi, data, e_x, e_x2, varianza
    print(f"""
    >>> 5.10
    
    Si lancia 2 volte una moneta truccata per cui P (T ) = 0.2 e P (C) = 0.8. Considerate la variabile casuale
    X = numero di teste. Definite la sua distribuzione di probabilità e calcolate il valore atteso E(X) e la varianza.
    """)
    p_t, p_c = 0.2, 0.8
    tentativi = 2
    data = [
        [0, pow(p_c, tentativi)],
        [1, p_c * p_t * tentativi],
        [2, pow(p_t, tentativi)],
    ]
    print(f"La distribuzione è: {data}")
    e_x = sum([x * y for x, y in data])
    e_x2 = sum([pow(x, 2) * y for x, y in data])
    print(f"Il valore atteso è: {e_x}")
    varianza = e_x2 - pow(e_x, 2)
    print(f"La varianza è data da: {varianza}")
    separa()


def esercizio_5_11():
    global n, p, q
    print(f"""
    >>> 5.11
    
    Sia X una variabile casuale binomiale con n = 12 e p = 0.4. Allora
    A) La X ha due mode in X = 5 e X = 4.
    B) La X ha due mode in X = 5 e X = 6.
    C) La X ha una moda in X = 5.
    D) La X ha una moda in X = 6.
    """)
    print("A e B sono false perché è sempre unimodale la binomiale.")
    n = 12
    p = 0.4
    q = 1 - p
    k1, k2 = 5, 6
    p_x5 = f.binomial_coefficient(n, k1) * pow(p, k1) * pow(q, n - k1)
    p_x6 = f.binomial_coefficient(n, k2) * pow(p, k2) * pow(q, n - k2)
    if p_x5 > p_x6:
        print(f"""C è vera perché il coefficiente binomiale per X=5, {p_x5}, è maggiore del coefficiente binomiale per 
X=6, {p_x6}.""")
        print("D è falsa di conseguenza.")
    else:
        print(f"""C è falsa perché il coefficiente binomiale per X=5, {p_x5}, è minore del coefficiente binomiale per
X=6, {p_x6}.""")
        print("D è vera di conseguenza.")
    separa()


def esercizio_5_12():
    print(f"""
    >>> 5.12
    
    Una squadra di operai edili deve essere composta da due muratori e da quattro manovali, scelti da un totale
    di cinque muratori e di sei manovali. Le selezioni dei muratori e dei manovali sono indipendenti. Quante
    diverse combinazioni sono possibili?
    """)
    n_muratori, tot_muratori = 2, 5
    n_manovali, tot_manovali = 4, 6
    comb_muratori = f.binomial_coefficient(tot_muratori, n_muratori)
    comb_manovali = f.binomial_coefficient(tot_manovali, n_manovali)
    print(f"Le combinazioni sono {comb_muratori * comb_manovali}.")
    separa()


def esercizio_5_13():
    global combinazioni_totali
    print(f"""
    >>> 5.13
    
    In una scatola contenente 16 cioccolatini, 4 sono con ripieno al cocco. Qual è la probabilità che scegliendo 4
    cioccolatini, nessuno sia con ripieno al cocco?
    A) 0.272
    B) 0.264
    C) 0.248 
    D) 0.236
    """)
    population = 16
    cocco = 4
    combinazioni_totali = f.binomial_coefficient(population, cocco)
    combinazioni_per_cui_no_cocco = f.binomial_coefficient(population - cocco, cocco)
    nessuno_con_cocco = combinazioni_per_cui_no_cocco / combinazioni_totali
    print(f"La probabilità che nessuno sia al cocco è {nessuno_con_cocco}, di conseguenza è vera la A).")
    separa()


def esercizio_5_14():
    global tentativi, combinazioni_totali
    print(f"""
    >>> 5.14
    
    Un test a risposta multipla ha 5 domande, ognuna con 5 possibili risposte. Se rispondi sempre a caso, qual
    è la probabilità di rispondere correttamente a esattamente 3 domande?
    A) 0.00032
    B) 0.008
    C) 0.0512
    D) 0.0016""")
    n_domande = risposte_possibili_per_domanda = 5
    tentativi = 3
    probabilita_successi = 1 / 5
    probabilita_insuccessi = 1 - probabilita_successi
    combinazioni_totali = f.binomial_coefficient(n_domande, tentativi)
    print(
        combinazioni_totali * pow(probabilita_successi, tentativi) * pow(probabilita_insuccessi, n_domande - tentativi))
    separa()


def esercizio_5_15():
    global p, q, n, k, res
    print(f"""
    >>> 5.15
    
    La probabilità che una persona prenda il raffreddore durante l’inverno è 0.4. Si selezionano a caso 10 persone.
    Qual è la probabilità che esattamente 4 di loro prenderanno il raffreddore?""")
    p = 0.4
    q = 1 - p
    n = 10
    k = 4
    res = f.binomial_coefficient(n, k) * pow(p, k) * pow(q, n - k)
    print(res)
    separa()


def esercizio_5_16():
    global N, n, k, res
    print(f"""
    >>> 5.16
    
    In un laghetto ci sono 10 pesci di cui 2 sono rossi. Peschi a caso senza ripetizione 5 pesci. Qual è la probabilità
    di pescare 1 pesce rosso?""")
    N = 10
    K = 2
    n = 5
    k = 1
    res = (f.binomial_coefficient(K, k) * f.binomial_coefficient(N - K, n - k)) / f.binomial_coefficient(N, n)
    print(res)
    separa()


def esercizio_5_17():
    global N, p, n, k, res
    print(f"""
    >>> 5.17
    
    In un laghetto ci sono 10 pesci di cui 2 sono rossi. Peschi a caso con ripetizione 5 pesci. Qual è la probabilità
    di pescare 1 pesce rosso?""")
    N = 10
    p = 2 / 10
    n = 5
    k = 1
    res = f.binomial_coefficient(n, k) * pow(p, k) * pow(1 - p, n - k)
    print(res)
    separa()


def esercizio_5_18():
    global p, q, n, k, res
    print(f"""
    >>> 5.18
    
    Una macchina produce pezzi difettosi con probabilità 0.2. Prendi un lotto di 5 pezzi: qual è la probabilità
    di trovare 1 pezzo difettoso?
    """)
    p = 0.2
    q = 1 - p
    n = 5
    k = 1
    res = f.binomial_coefficient(n, k) * pow(p, k) * pow(q, n - k)
    print(res)
    separa()


def esercizio_5_19():
    global n, p
    print(f"""
    >>> 5.19
    
    Tiro 3 dadi. Qual è la probabilità che la somma sia 3? Qual è la probabilità di ottenere tre volte 1?""")
    n = 3
    p = 1 / (pow(6, 3))
    print(p)
    separa()


def esercizio_5_20():
    global n, p, q, k, res
    print(f"""
    >>> 5.20
    
    Estraggo un campione casuale senza ripetizione di 100 elettori da una popolazione in cui vi è il 30% di
    favorevoli a Renzi. Qual è la probabilità che il campione contenga 35 persone favorevoli a Renzi?
    """)
    n = 100
    p = 0.30
    q = 1 - p
    k = 35
    res = f.binomial_coefficient(n, k) * pow(p, k) * pow(q, n - k)
    print(res)
    separa()


def esercizio_5_21():
    print(f"""
    >>> 5.21
    
    Quale dei seguenti è un esempio di variabile casuale discreta?
    A) L’ammontantare di pioggia che cade in un intervallo temporale di 24 ore.
    B) Il peso di un pacco all’ufficio postale.
    C) La distanza che puoi percorrere con un pieno di benzina.
    D) Il numero di vacche in una fattoria.""")
    print("La risposta giusta è la D, il numero di vacche in una fattoria. Le prime tre voci, di fatto, sono misure e "
          "pertanto sono affette da continuità")


if __name__ == "__main__":
    esercizio_5_3()
    esercizio_5_4()
    esercizio_5_5()
    esercizio_5_6()
    esercizio_5_7()
    esercizio_5_9()
    esercizio_5_10()
    esercizio_5_11()
    esercizio_5_12()
    esercizio_5_13()
    esercizio_5_14()
    esercizio_5_15()
    esercizio_5_16()
    esercizio_5_17()
    esercizio_5_18()
    esercizio_5_19()
    esercizio_5_20()
    esercizio_5_21()
