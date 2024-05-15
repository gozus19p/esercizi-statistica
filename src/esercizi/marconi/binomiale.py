from statistica_metodologica import funzioni as f
from esercizi.esercizio import Esercizio


class Binomiale(Esercizio):

    def __init__(self):
        super() \
            .__init__(
            "ESAME 07/04/23; 13/04/22",
            """Un'impresa che produce tende da campeggio deve verificare a resistenza alla lacerazione del telo 
            principale di 10 tende prese a campione. La probabilità che una determinata tenda resista alla prova è 
            4/5. Si calcoli la probabilità che 7 delle 10 tende superino la prova con successo."""
        )

    def execute(self) -> float:
        n = 10
        p = 4 / 5
        k = 7
        return f.dist_binomial(n, k, p)


class Binomiale2(Esercizio):
    def __init__(self):
        super() \
            .__init__(
            "Secondo esercizio su binomiale (esame Marconi)",
            """Si prenda in considerazione un concorso pubblico e in particolare l'esecuzione della prova 
            preselettiva basata su un test a risposta multipla composto da 200 domande. Per ogni domanda ci sono 4 
            risposte alternative e solo una delle 4 è corretta. Si supponga che il candidato non sia preparato e che 
            pertanto non sappia rispondere al test. Si calcoli la probabilità che, rispondendo casualmente a 80 delle 
            200 domande del test, il candidato riesca a rispondere correttamente ai quesiti compresi in un intorno 
            tra 25 e 30. La probabilità che il candidato individui casualmente la risposta corretta per gli 80 
            quesiti è pari a p=1/4."""
        )

    def execute(self) -> float:
        n = 80
        p = 1/4
        return sum([f.dist_binomial(n, k, p) for k in range(25, 31)])


if __name__ == '__main__':
    print(Binomiale2().execute())