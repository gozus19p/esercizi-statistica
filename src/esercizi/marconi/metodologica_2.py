import numbers


class Threshold:
    lower_bound: float
    upper_bound: float

    def __init__(self, lower_bound: float, upper_bound: float):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return f"[{self.lower_bound}, {self.upper_bound})"


if __name__ == "__main__":
    print("""

    Data la distribuzione di frequenze a seguire, relativa ad un carattere quantitativo discreto X raggruppato in
    classi, determinarne: a) la media aritmetica e b) la mediana.

    | Altezza in cm | Frequenze assolute | Frequenze relative | Frequenze cumulate         |
    |---------------|--------------------|--------------------|----------------------------|
    | fino a 160    | 3                  |                    |                            |
    | 160 --- 170   | 3                  |                    |                            |
    | 170 --- 180   | 6                  |                    |                            |
    | 180 --- 190   | 4                  |                    |                            |
    | 190 --- 200   | 2                  |                    |                            |
    | oltre 200     | 4                  |                    |                            |
    | TOTALE        | 22                 |                    |                            |
    """)
    data = [
        [Threshold(0, 160), 3],
        [Threshold(160, 170), 3],
        [Threshold(170, 180), 6],
        [Threshold(180, 190), 4],
        [Threshold(190, 200), 2],
        [Threshold(200, 0), 4],
    ]
    total = 22

    cumulated = 0
    for d in data:
        cumulated += d[1]
        relative = d[1] / total
        d.append(relative)
        d.append(cumulated)

        # Midpoint
        thresh = d[0]
        if thresh.lower_bound and thresh.upper_bound:
            d.append((thresh.upper_bound + thresh.lower_bound) / 2)
        elif thresh.lower_bound:
            d.append(thresh.lower_bound)
        elif thresh.upper_bound:
            d.append(thresh.upper_bound)

    print("\n".join(list(map(lambda x: ", ".join([str(f) for f in x]), data))))
    print(f"Media aritmetica: {sum([d[1] * d[4] for d in data]) / total}")

    median_point = total / 2 if total % 2 == 0 else (total + 1) / 2
    median = None
    for d in data:
        if d[3] > median_point:
            median = d[0]
            break
    print(f"Mediana: {median}")