from esercizio import Esercizio
import funzioni as f
import scipy.stats as s
import math


class VerificaDiIpotesi(Esercizio):
    def __init__(self):
        super().__init__(
            """Un costruttore asserisce che le pompe di calore vengono installate nel 70% delle case di nuova 
            costruzione nella città di Asti. Sei d'accordo con questa affermazione se, in base a un'indagine campionaria 
            sulle nuove case della città, si evidenzia che 11 su 15 sono dotate di pompe di calore? Imposta un livello di 
            significatività pari a 0,10."""
        )

    # Stampare True se non si rifiuta H0
    def execute(self) -> bool:
        pass


class VerificaDiIpotesi_2(Esercizio):
    def __init__(self):
        super().__init__(
            """Un costruttore asserisce che le pompe di calore vengono installate nel 75% delle case di nuova 
            costruzione nella città di Grosseto. Sei d’accordo con questa affermazione se in base ad un’indagine 
            campionaria sulle nuove case della città si evidenzia che 10 su 15 sono dotate di pompe di calore? 
            Impostare un livello di significatività pari a 0,10."""
        )

    # Stampare True se non si rifiuta H0
    def execute(self) -> bool:
        pass


class VerificaDiIpotesi_3(Esercizio):

    def __init__(self):
        super().__init__(
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
        pass


class VerificaDiIpotesi_4(Esercizio):
    def __init__(self):
        super().__init__(
            """
            Un produttore di attrezzature sportive ha sviluppato un nuovo tipo di lenza che si sostiene abbia un carico
            a rottura medio di 9 chili, con una deviazione standard pari a 0,8 chili. Viene testato un campione casuale di 60
    lenze, e viene calcolato un carico a rottura medio di 8,4 chili. Verificare l'ipotesi mu=9 chili contro l'ipotesi 
    alternativa mu!=9 chili. Adottare un livello di significatività 0,01."""
        )

    # Stampare True se non si rifiuta H0
    def execute(self) -> bool:
        pass


class VerificaDiIpotesi_5(Esercizio):
    def __init__(self):
        super().__init__(
            """Si sostiene che un farmaco comunemente prescritto per alleviare la tensione nervosa abbia un'efficacia 
            del 70%. I risultati sperimentali con un nuovo farmaco somministrato ad un campione di 180 adulti che 
            soffrono di tensione nervosa evidenzia che 140 adulti ottengono un beneficio. Da questa evidenza si può 
            concludere che il nuovo farmaco sia più efficace di quello comunemente prescritto? Assumere un livello di 
            significatività pari a 0,01."""
        )

    # Stampare True se non si rifiuta H0
    def execute(self) -> bool:
        pass


class VerificaDiIpotesi_6(Esercizio):
    def __init__(self):
        super().__init__(
            """Un campione casuale di 200 decessi occorsi quest'anno in Italia ha evidenziato una vita media di 72,
            4 anni. Assumendo una deviazione ‘standard di 9,3 anni, si può concludere che la vita media è maggiore di 
            69 anni? Adottare un livello di significatività pari a 0,05."""
        )

    # Stampare True se non si rifiuta H0
    def execute(self) -> bool:
        pass


class VerificaDiIpotesi_7(Esercizio):
    def __init__(self):
        super().__init__(
            """Il contenuto in litri di 9 contenitori uguali d'acqua è pari rispettivamente a 19.8 — 20,1 — 20,0— 19, 
            3- 19,9- 20,4 — 20,3 19,6 - 20,6. Trovare un intervallo di confidenza al 95% per il contenuto medio di 
            questo tipo di contenitori, assumendo che abbia distribuzione approssimativamente normale."""
        )

    # Restituire, in tupla, l'intervallo inferiore e superiore nell'ordine com'è scritto [inf, sup]
    def execute(self) -> tuple[float, float]:
        pass
