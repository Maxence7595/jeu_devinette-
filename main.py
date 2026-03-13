"""
Jeu de Devinette - Nombre Mystere
Point d'entree principal du jeu

Auteur: Maxence Amirkhanian
"""

from menu import afficher_titre, afficher_menu_principal, afficher_regles, choisir_difficulte
from game import jouer_partie
from utils import afficher_score


def main():
"""Fonction principale du jeu"""
afficher_titre()
while True:
choix = afficher_menu_principal()
if choix == "1":
niveau = choisir_difficulte()
tentatives = jouer_partie(niveau)
afficher_score(tentatives, niveau)
elif choix == "2":
afficher_regles()
elif choix == "3":
print("\nMerci d'avoir joue! A bientot!")
break
else:
print("Choix invalide. Veuillez reessayer.")


if __name__ == "__main__":
main()
