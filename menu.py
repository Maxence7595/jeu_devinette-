"""
Module de gestion du menu principal du jeu
"""

def afficher_titre():
"""Affiche le titre du jeu"""
print("\n" + "=" * 40)
print(" JEU DE DEVINETTE")
print(" Nombre Mystere")
print(" Par Maxence MUSIC")
print("=" * 40)


def afficher_menu_principal():
"""Affiche le menu principal et retourne le choix"""
print("\n--- MENU PRINCIPAL ---")
print("1. Nouvelle partie")
print("2. Regles du jeu")
print("3. Quitter")
print("-" * 22)
choix = input("Votre choix (1-3): ")
return choix


def afficher_regles():
"""Affiche les regles du jeu"""
print("\n--- REGLES DU JEU ---")
print("Le but est de deviner un nombre mystere.")
print("A chaque tentative, vous saurez si le nombre")
print("a trouver est plus GRAND ou plus PETIT.")
print("Essayez de trouver en un minimum de coups!")
print("-" * 35)
input("\nAppuyez sur Entree pour continuer...")


def choisir_difficulte():
"""Permet de choisir le niveau de difficulte"""
print("\n--- NIVEAU DE DIFFICULTE ---")
print("1. Facile (1-50)")
print("2. Moyen (1-100)")
print("3. Difficile (1-200)")
print("-" * 28)
while True:
choix = input("Votre choix (1-3): ")
if choix in ["1", "2", "3"]:
return choix
print("Choix invalide! Entrez 1, 2 ou 3.")
