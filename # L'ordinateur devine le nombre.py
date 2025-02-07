# L'ordinateur devine le nombre
import random
import time


def timer_decorator(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        print(f"Et ça ma prit seulement {end - start: .5f} secondes")
        return result
    return wrapper

@timer_decorator
def ordinateur_devine(x):
    min, max = 1, x
    Retour = ""
    essai = 1
    while Retour != "c":
        if min != max:
            choix = random.randint(min, max)
        else:
            choix = min
        Retour = input(f"Est-ce que {choix} est trop grand (g), trop petit (p) ou correct (c): ").lower()
        # Trouver filter les nombres restant avec un algorithme de recherche binaire
        if Retour == "g":
            max = choix - 1
            essai += 1
        elif Retour == "p":
            min = choix + 1
            essai += 1
    
    print(f"Ton numéro est le {choix} et je l'ai trouvé en {essai} coups")

ordinateur_devine(100)