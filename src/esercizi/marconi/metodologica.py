from statistica_metodologica import funzioni as f


def esercizio_1():
    print("""Data la serie riportata, relativa al carattere X afferente ai giudizi riportati da 8 studenti ad un 
   compito di matematica, determinarne: a) la media aritmetica; b) la mediana; c) la moda.""")
    data = [
        [1, "ottimo"],
        [2, "ottimo"],
        [3, "pessimo"],
        [4, "mediocre"],
        [5, "sufficiente"],
        [6, "buono"],
        [7, "buono"],
        [8, "distinto"]
    ]
    # Per prima cosa occorre "discretizzare" e assegnare un valore numerico a ognuna delle categoriche
    mappa = {
        "ottimo": 10,
        "pessimo": 4,
        "mediocre": 5,
        "sufficiente": 6,
        "buono": 7,
        "distinto": 8
    }
    data = list(map(lambda x: mappa[x[1]], data))
    mean = f.mean(data)
    median = f.median(data)
    mode = f.mode(data)
    print(f"Mean = {mean}, Median = {median}, Mode = {mode}")


def esercizio_2():
    print("""
    Calcolare la media e la mediana della seguente distribuzione di frequenze: F(1-9)>.1 F(10-20)—>1 F(21:31)—> 100
    """)
    data = [
        ["1-9", 1],
        ["10-20", 1],
        ["21-31", 100]
    ]
    for d in data:
        interval = d[0].split("-")
        lower, upper = int(interval[0]), int(interval[1])
        midpoint = (lower + upper) / 2
        d.append(midpoint)
        d.append(midpoint * d[1])
    mean = sum(list(map(lambda x: float(x[3]), data))) / sum(list(map(lambda x: float(x[1]), data)))
    print(f"Mean = {mean}")

    cumulatives, total = [], 0
    for d in data:
        total = total + d[1]
        cumulatives.append(total)
    print(f"Cumulatives = {cumulatives}")
    print(f"Total = {total}")

    middle_position = (total if total % 2 == 1 else total + 1) / 2
    print(f"Middle position = {middle_position}")
    m = middle_position
    for i, d in enumerate(data):
        if m - d[1] > middle_position:
            print(f"Median = {data[i][0]}")
            break
    print(f"Median = {data[-1][0]}")


if __name__ == "__main__":
    esercizio_2()
