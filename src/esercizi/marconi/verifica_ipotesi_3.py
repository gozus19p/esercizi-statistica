import math

from statistica_metodologica import funzioni as f

if __name__ == '__main__':
    print("""
    Un’industria produce blister per la supply-chain farmaceutica e questi blister hanno un peso medio di 6,
    0 grammi. Supponendo che la media della popolazione sia di 6,0 grammi, durante un esperimento vengono estratti 
    casualmente 100 blister dal processo produttivo cui viene poi misurato il peso. La deviazione standard della 
    popolazione è uguale a 0,15 grammi del peso medio campionario è pari a 6,034 grammi. Le informazioni campionarie 
    sostengono o confutano la congettura relativa alla media della popolazione?
    """)

    print("""
    In questo caso, si procede utilizzando un test Z normale calcolando al numeratore la differenza tra la media
    campionaria con la media della popolazione (h0) e al denominatore la dev.std. per la radice di n.
    """)
    mu = 6.0
    mu_c = 6.034
    sigma = 0.15
    n = 100

    # Livello di significatività
    ls = 0.10

    # H0 -> la media è 6.0, H1 -> la media NON è 6.0

    z = (mu_c - mu) / sigma * math.sqrt(n)
    # Diviso 2 perché test bilaterale
    cv = f.norm(1 - (ls / 2))
    if z < cv:
        print(f"Non si rifiuta H0. cv={cv}, z={z}")
    else:
        print(f"Si rifiuta H0. cv={cv}, z={z}")
