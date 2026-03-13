"""
Module de logique principale du jeu de devinette
"""
import random


def generer_nombre_mystere(niveau):
"""Genere un nombre mystere selon le niveau"""
limites = {
"1": 50,
"2": 100,
"3": 200
}
limite_max = limites.get(niveau, 100)
return random.randint(1, limite_max), limite_max


def verifier_proposition(proposition, nombre_mystere):
"""
Verifie la proposition du joueur
Retourne: gagne, plus_grand, plus_petit ou erreur
"""
try:
nombre = int(proposition)
if nombre == nombre_mystere:
return "gagne"
elif nombre < nombre_mystere:
return "plus_grand"
else:
return "plus_petit"
except ValueError:
return "erreur"


def jouer_partie(niveau):
"""Lance une partie complete"""
nombre_mystere, limite = generer_nombre_mystere(niveau)
tentatives = 0
print(f"\nJ'ai choisi un nombre entre 1 et {limite}...")
print("A vous de deviner!\n")
while True:
proposition = input(f"Tentative {tentatives + 1} - Votre proposition: ")
resultat = verifier_proposition(proposition, nombre_mystere)
tentatives += 1
if resultat == "gagne":
print(f"\nBRAVO! Vous avez trouve {nombre_mystere} en {tentatives} tentatives!")
return tentatives
elif resultat == "plus_grand":
print("C'est PLUS GRAND!")
elif resultat == "plus_petit":
print("C'est PLUS PETIT!")
else:
print("Erreur: Veuillez entrer un nombre valide.")
tentatives -= 1
