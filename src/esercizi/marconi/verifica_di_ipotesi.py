from esercizi.esercizio import Esercizio
from statistica_metodologica import funzioni as f
import math


class VerificaDiIpotesi(Esercizio):
    def __init__(self):
        super().__init__(
            "VerificaDiIpotesi",
            """Un costruttore asserisce che le pompe di calore vengono installate nel 70% delle case di nuova 
            costruzione nella città di Asti. Sei d'accordo con questa affermazione se, in base a un'indagine campionaria 
            sulle nuove case della città, si evidenzia che 11 su 15 sono dotate di pompe di calore? Imposta un livello di 
            significatività pari a 0,10."""
        )

    # Stampare True se non si rifiuta H0
    def execute(self) -> bool:
        n = 15
        k = 11
        p0 = 0.70

        # Per calcolare il p-value sottraggo a 1 il risultato della binomiale di Bernoulli
        p_value = 1 - f.dist_binomial(n, k, p0)
        print(f"P-value = {p_value}, valore significatività = 0.05")
        alpha = 0.10

        # Se vero, non si rifiuta H0
        return p_value > alpha / 2


class VerificaDiIpotesi_2(Esercizio):
    def __init__(self):
        super().__init__(
            "VerificaDiIpotesi_2",
            """Un costruttore asserisce che le pompe di calore vengono installate nel 75% delle case di nuova 
            costruzione nella città di Grosseto. Sei d’accordo con questa affermazione se in base ad un’indagine 
            campionaria sulle nuove case della città si evidenzia che 10 su 15 sono dotate di pompe di calore? 
            Impostare un livello di significatività pari a 0,10."""
        )

    def execute(self) -> bool:
        p0 = 0.75
        n = 15
        k = 10
        alpha = 0.10

        # Dato che il test è bilaterale (H1 --> !=H0) dividiamo alpha per 2
        alpha /= 2

        # Si effettua un test statistico per la proporzione del campione, calcolando la proporzione campionaria
        p_hat = k / n
        z = (p_hat - p0) / math.sqrt(p0 * (1 - p0) / n)
        cv = f.norm(1 - alpha)
        cv_n = -cv
        return cv_n < z < cv


class VerificaDiIpotesi_3(Esercizio):

    def __init__(self):
        super().__init__(
            "VerificaDiIpotesi_3",
            """
                Un’industria produce blister per la supply-chain farmaceutica e questi blister hanno un peso medio di 6,
                0 grammi. Supponendo che la media della popolazione sia di 6,0 grammi, durante un esperimento vengono estratti 
                casualmente 100 blister dal processo produttivo cui viene poi misurato il peso. La deviazione standard della 
                popolazione è uguale a 0,15 grammi del peso medio campionario è pari a 6,034 grammi. Le informazioni campionarie 
                sostengono o confutano la congettura relativa alla media della popolazione?
                """
        )

    # Stampare True se non si rifiuta H0
    def execute(self) -> bool:
        mu_p = 6
        n = 100
        dev_std = 0.15
        mu_c = 6.034
        alpha = 0.05

        z = (mu_c - mu_p) / dev_std * math.sqrt(n)
        cv = f.norm(1 - alpha / 2)
        return (cv > z >= 0) or (cv < z <= 0)
