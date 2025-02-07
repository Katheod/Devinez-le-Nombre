import random


# Fonction pour afficher les messages d'erreur
def afficher_message_erreur(nombre, nombre_aléatoire):
    if nombre < nombre_aléatoire:
        print(f"Désolé, mauvais nombre. Mon nombre est plus grand que {nombre}.")
    elif nombre > nombre_aléatoire:
        print(f"Désolé, mauvais nombre. Mon nombre est plus petit que {nombre}.")

# Fonction pour deviner le nombre choisi par l'ordinateur
def devines_le_nombre(x): 
    nombre_aléatoire = random.randint(1, x)
    nombre = 0 
    essai = 1
    while nombre_aléatoire != nombre:
        try:
            nombre = int(input(f"Choisis un nombre entre 1 et {x} : "))
            if 1 <= nombre <= x:
                afficher_message_erreur(nombre, nombre_aléatoire)
                essai += 1
            else:
                print(f"Veuillez entrer un nombre valide entre 1 et {x}")
        except ValueError:
            print(f"Veuillez entrer un nombre valide.")
    
    print(f"Bravo! Tu as trouvé mon nombre après {essai} essais. C'était bien le {nombre_aléatoire}")


#Fonction pour afficher le résultat de la devinette de l'ordinateur
def afficher_resultat(choix, essai):
    print(f"Ton numéro est le {choix} et je l'ai trouvé après {essai} coups!")


# Fonction pour l'ordinateur devine le nombre choisi par l'utilisateur
def ordinateur_devine(x):
    min_val, max_val = 1, x
    retour = ""
    essai = 1
    while retour != "c":
        if min_val != max_val:
            choix = random.randint(min_val, max_val)
        else:
            choix = min_val # Ou max. Ça importe peu puisque c'est uniquement si min_val == max_val.
        retour = input(f"Est-ce que {choix} est trop grand (g), trop petit (p) ou correct (c) ? ").lower()
        # Filtrer les nombres restant avec un algorithme de recherche binaire.
        if retour == "g":
            max_val = choix - 1
            essai += 1
        elif retour == "p":
            min_val = choix + 1
            essai += 1
    
    afficher_resultat(choix, essai)
