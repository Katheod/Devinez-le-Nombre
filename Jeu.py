import random

# Version où l'utilisateur doit deviner le nombre que l'ordinateur choisit.
def devines_le_nombre(x): # Le x est pour que l'utilisateur choisit la difficulté du jeu.
    nombre_aléatoire = random.randint(1, x)
    nombre = 0 # Initier la variable.
    while nombre_aléatoire != nombre:
        nombre = int(input(f"Choisis un nombre entre 1 et {x}: "))
        if nombre < nombre_aléatoire:
            print(f"Désolé, mauvais nombre. Mon nombre est plus grand que {nombre}")
        elif nombre > nombre_aléatoire: 
            print(f"Désolé, mauvais nombre. Mon nombre est plus petit que {nombre}")
    
    print(f"Bravo! Tu as trouvé mon nombre. C'était bien le {nombre_aléatoire}")


def ordinateur_devine(x):
    min, max = 1, x
    Retour = ""
    while Retour != "c":
        if min != max:
            choix = random.randint(min, max)
        else:
            choix = min
        Retour = input(f"Est-ce que {choix} est trop grand (g), trop petit (p) ou correct (c): ")
        if Retour == "g":
            max = choix - 1
        elif Retour == "g":
            min = choix + 1
    
    print(f"Ton numéro est le {choix}")

ordinateur_devine(100)