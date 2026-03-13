"""
Module utilitaire avec fonctions d'aide
"""


def calculer_score(tentatives, limite):
"""Calcule un score base sur les tentatives et la difficulte"""
score_max = 1000
malus_par_tentative = 50
bonus_difficulte = limite * 2
score = score_max - (tentatives * malus_par_tentative) + bonus_difficulte
return max(0, score)


def afficher_score(tentatives, niveau):
"""Affiche le score final du joueur"""
limites = {"1": 50, "2": 100, "3": 200}
limite = limites.get(niveau, 100)
score = calculer_score(tentatives, limite)
print("\n" + "=" * 30)
print(f" SCORE FINAL: {score} points")
print("=" * 30)
if tentatives <= 5:
print("Excellent! Vous etes un pro!")
elif tentatives <= 10:
print("Bien joue!")
else:
print("Continuez a vous entrainer!")
