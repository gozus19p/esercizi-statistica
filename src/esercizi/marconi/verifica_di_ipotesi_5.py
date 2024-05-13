import math
from statistica_metodologica import funzioni as f

if __name__ == "__main__":
    print("""
    Si sostiene che un farmaco comunemente prescritto per alleviare la tensione nervosa abbia un'efficacia del 70%. I 
    risultati sperimentali con un nuovo farmaco somministrato ad un campione di 180 adulti che soffrono di tensione 
    nervosa evidenzia che 140 adulti ottengono un beneficio. Da questa evidenza si può concludere che il nuovo farmaco 
    sia più efficace di quello comunemente prescritto? Assumere un livello di significatività pari a 0,01.
    """)
    p = 0.70
    n = 180
    k = 140
    p_hat = k / n
    alpha = 0.01

    # H0 -> p<=0.7, H1 -> p>0.7
    z = (p_hat - p) / math.sqrt(p * (1 - p) / n)
    cv = f.norm(1 - alpha)
    if 0 <= z < cv:
        print(f"Non si rifiuta H0 perché z={z}, cv={cv}")
    else:
        print(f"Si rifiuta H0 perché z={z}, cv={cv}")


