import inspect
import random
import marconi.verifica_di_ipotesi as vf
import marconi.metodologica as m
import marconi.probabilita as pr
import marconi.due_campioni as dc

if __name__ == "__main__":
    classes = [member for module in [vf, m, pr, dc] for name, member in inspect.getmembers(module) if
               inspect.isclass(member) and name != "Esercizio"]
    classes_len = len(classes)
    exercise_to_do = random.Random() \
        .randint(0, classes_len - 1)
    to_do = classes[exercise_to_do]
    exercise = to_do()
    print(exercise.nome)
    print(exercise.consegna)
