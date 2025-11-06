from app.utils import Saluer
import sys

def main():
    print("Début d'exécution du programme")
    Saluer("Bloup")
    if len(sys.argv) > 1:
        print(f"Argument fourni : {sys.argv[1:]}")
    else:
        print("Aucun argument fourni.")
        
    rien = None
    print(f"La valeur de {rien} est de type {type(rien)}")
    
    #operateur
    a = 10
    print(f"{5//9}")


if __name__ == "__main__":
    main()
    


x = 10
y = 20

if x == 10:
    if y == 20:
        print("x vaut 10 et y vaut 20")
    else:
        print("x vaut 10 mais y ne vaut pas 20")
else:
    print("x ne vaut pas 10")
    
#elif
if x > 10:
    print("x est supérieur à 10")
elif x == 10:
    print("x est égal à 10")
elif x < 10:
    print("x est inférieur à 10")
    
# ternaire
resultat = "x est 10" if x == 10 else "x n'est pas 10"

# switch
jour = 'lundi'
match jour:
    case 'lundi':
        print("C'est le premier jour de la semaine.")
    case 'mardi':
        print("C'est le deuxième jour de la semaine.")
    case 'mercredi':
        print("C'est le troisième jour de la semaine.")
    case _:
        print("C'est un autre jour de la semaine.")
        
# boucles
for i in range(5):
    print(f"itération {i}")
    
compteur = 0
while compteur < 5:
    print(f"compteur = {compteur}")
    compteur += 1
    
# boucle inversée
compteur = 10
while compteur > 0:
    print(f"compteur = {compteur}")
    compteur -= 1
    
for i in range(10, 0, -1):
    print(f"inversée {i}")
    
# triangle complet inversé
#n = int(input("Entrez le nombre d'étoiles : "))
""" for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print() """
    
# triangle boucle while
""" n = int(input("[While] Entrez le nombre d'étoiles : "))
while n > 0:
    print('*' * n)
    n -= 1 """
    
# simulez un jeu de dès entre 2 joueurs
# max dès : 12 (2 x 6)
# 10 tours
# Chaque joueur tire aléatoirement un nombre entre 2 et 12 (2 dès)
# Gagne = +1 point sur le score
# Afficher le score à la fin des 10 tours

# import random
# joueur1_score = 0
# joueur2_score = 0
# tours = 10

# for tour in range(1, tours +1):
#     joueur1_tirage = random.randint(2, 12)
#     joueur2_tirage = random.randint(2, 12)
#     print(f"Tour {tour} : Joueur 1 joue {joueur1_tirage}, Joueur 2 joue {joueur2_tirage}")
#     if joueur1_tirage > joueur2_tirage:
#         joueur1_score +=1
#     elif joueur2_tirage > joueur1_tirage:
#         joueur2_score +=1
#     else:
#         print('égalité ce tour')

# print(f'Score final : Joueur 1 = {joueur1_score}, Joueur 2 = {joueur2_score}')
# if joueur1_score > joueur2_score:
#     print("Joueur 1 gagne la partie !")
# elif joueur2_score > joueur1_score:
#     print("Joueur 2 gagne la partie !")

# instruction de controle exceptionnelle
for i in range(5):
    if i == 2:
        continue  # saute l'itération lorsque i vaut 2
    if i == 3:
        pass     # ne fait rien lorsque i vaut 3
    if i == 4:
        break     # quitte la boucle lorsque i vaut 4
    print(f"i = {i}")
    
# dictionnaires
mon_dict = {
    "nom": "Alice",
    "âge": 30,
    "ville": "Paris"
}
print(mon_dict["nom"])  # Accès à la valeur associée à la clé "nom"
mon_dict["âge"] = 31    # Modification de la valeur associée à la clé "âge"
mon_dict["pays"] = "France"  # Ajout d'une nouvelle paire clé-valeur
print(mon_dict)

note = {'alice': 15, 'bob': 18, 'charlie': 12}
print(note['bob'])

for eleve, note in note.items():
    print(f"L'élève {eleve} a obtenu la note de {note}")
    
# verifier l'existence d'une clé
classe = {'alice': 15, 'bob': 18, 'charlie': 12}
if 'bob' in classe:
    print("Bob est dans la classe.")


# nombre d'éléments dans un dictionnaire
print(f"Le dictionnaire contient {len(classe)} éléments.")

#-------------------------------------------------------------
#Les listes
# mutables
fruits = ["pomme", "banane", "cerise"]
listeVide = []

# acceder aux elements
print(f"Premier fruit: {fruits[0]}")

# modifier un element
fruits[1] = "orange"

#supprimer un element
del fruits[2]
print(f"Fruits apres suppression: {fruits}")

#boucler a travers les elements
for fruit in fruits:
    print(f"Fruit: {fruit}")

# verifier l'existence d'un element
if "pomme" in fruits:
    print("La pomme est dans la liste des fruits.")

# nombre d'elements
# print(f"La liste contient {len(fruits)} fruits.")

# creer une liste de nombres de 0 a 9
nombres = list(range(10))

# -------------------------------------------------------------

# ajouter un element a la fin
fruits.append("kiwi")
# Inserer un element a une position specifique
fruits.insert(1, "fraise")

panier = ["banane", "cerise"]
fruits.extend(panier) # ajoute les elements de panier a fruits

# supprimer un element par valeur
fruits.remove("pomme")

# supprime et retourne le dernier element
denier_fruit = fruits.pop() 

# découper une liste
sous_liste = fruits[1:3]  # elements d'index 1 a 2
autre_sous_liste = fruits[:2]  # premiers deux elements
autre_sous_liste2 = fruits[2:]  # elements a partir de l'index 2    
autre_sous_liste3 = fruits[1::2]  # elements d'index impair

# les listes de listes (listes imbriquees)
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for ligne in matrice:
    for element in ligne:
        print(f"Element: {element}")
# acceder a un element specifique
element = matrice[1][2] # 6

# modifier un element specifique
matrice[0][0] = 10  # change 1 en 10

    
    


