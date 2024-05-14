

if __name__ == '__main__':

    print("""
    Calcolare la media e la mediana della seguente distribuzione di frequenze: F(1-9)>1 F(10-20)—>1 F(21:31)—> 100
    """)
    data = [
        ["1-9", 1],
        ["10-20", 1],
        ["21-31", 100],
    ]

    total = sum([d[1] for d in data])

    # Calcolo i mid point
    cumulated = 0
    for d in data:
        interval = d[0].split("-")
        lower, upper = int(interval[0]), int(interval[1])
        midpoint = (lower + upper) / 2
        d.append(midpoint)
        d.append(d[1] * midpoint)
        cumulated += d[1]
        d.append(cumulated)

    mean = sum([d[3] for d in data]) / total
    print(f"Media: {mean}")

    median_point = total / 2 if total % 2 == 0 else (total + 1) / 2
    print(f"Punto mediano: {median_point}")
    for d in data:
        if d[4] > median_point:
            print(f"Mediana: {d[0]}")
            break