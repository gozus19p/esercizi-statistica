import funzioni as f
from marconi import metodologica as m


def test_metodologica_1():
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
    assert m.Metodologica_1().execute() == (mean, median, mode)


def test_metodologica_2():
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
    mp = middle_position
    median = -1
    for i, d in enumerate(data):
        if mp - d[1] > middle_position:
            median = data[i][0]
            break
    print(f"Median = {median}")
    assert m.Metodologica_2().execute() == (mean, median)


def test_metodologica_3():
    data = [
        [m.Threshold(0, 160), 3],
        [m.Threshold(160, 170), 3],
        [m.Threshold(170, 180), 6],
        [m.Threshold(180, 190), 4],
        [m.Threshold(190, 200), 2],
        [m.Threshold(200, 0), 4],
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
    mean = sum([d[1] * d[4] for d in data]) / total
    print(f"Media aritmetica: {mean}")

    median_point = total / 2 if total % 2 == 0 else (total + 1) / 2
    median = None
    for d in data:
        if d[3] > median_point:
            median = d[0]
            break
    print(f"Mediana: {median}")
    assert m.Metodologica_3().execute() == (mean, median)
