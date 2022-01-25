"""
Module principal du package pymafia.
C'est ici le point d'entrée du programme.
Ce module définit 3 fonctions ainsi que les commandes principales qui lancent le jeu.
"""
from pymafia.partie import Partie


def demander_nombre_joueurs():
    """
    Fonction qui demande à l'utilisateur combien de joueurs entre 2 et 8 vont jouer une partie de pymafia.
    Les validations sont faites sur la valeur entrée par l'utilisateur et le programme redemande un nombre
    si la valeur entrée est invalide.

    Returns:
        int: le nombre de joueurs choisi par l'utilisateur
    """
    while True:
        nombre_joueurs = input('À combien de joueurs voulez-vous jouer une partie de pymafia? (entre 2 et 8) ')
        if nombre_joueurs.isnumeric():
            nombre_joueurs = int(nombre_joueurs)
            if 2 <= nombre_joueurs <= 8:
                return nombre_joueurs
        print("Choix invalide. Veuillez choisir un chiffre entre 2 et 8.\n")


def demander_nombre_joueurs_humains(nombre_joueurs):
    """
    Fonction qui demande le nombre de joueurs humains qui seront parmi les joueurs. Les autres joueurs
    seront contrôlés par l'ordinateur. Les validations sont faites sur la valeur entrée par l'utilisateur
    et le programme redemande un nombre si la valeur entrée est invalide. Cette valeur doit bien sûr être
    inférieure ou égale au nombre de joueurs.
    Args:
        nombre_joueurs (int): nombre de joueurs voulu par l'utilisateur.

    Returns:
        int: le nombre de joueurs humains choisi par l'utilisateur
    """
    while True:
        nombre_joueurs_humains = input("Parmi ces {} joueurs, combien y a-t-il d'humains? ".format(nombre_joueurs))
        if nombre_joueurs_humains.isnumeric():
            nombre_joueurs_humains = int(nombre_joueurs_humains)
            if 1 <= nombre_joueurs_humains <= nombre_joueurs:
                return nombre_joueurs_humains
        print("Choix invalide. Veuillez choisir un chiffre entre 1 et {}.\n".format(nombre_joueurs))


def afficher_instructions():
    """
    Fonction qui affiche les instructions du jeu.
    """
    #print("Instruction du jeu pyMafia.\n")
    return (f'Instructions:\nVous pouvez jouer entre 2 et 8 joueurs.\nAu départ, chaque joueur dispose de 5 dés '
           f'traditionnels à 6 '
           f'faces et 50 points points.\nVous jourez 10 rondes.\nAvant le début de la première ronde, chaque joueur '
           f'joue deux dés. Le joueur ayant le plus haut résultat commencera.\nTant qu’il y a égalité au plus haut '
           f'score entre plusieurs joueurs, ces derniers relancent les dés.\nLe premier joueur décide du sens dans '
           f'lequel vous allez jouer.\nÀ tours de rôles vous roulerez vos dés.\nLes dés ayant la valeur 6 sont passés '
           f'au prochain joueur. Les dés de valeur 1 sont retirés du jeu.\nLa ronde continue jusqu’à ce qu’un joueur '
           f'n’ait plus aucun dé.\nCeci termine la ronde. Les autres joueurs roulent alors leurs dés restants et '
           f'comptent le total des dés.\nIls perdent alors le nombre de points obtenus sur les dés et donnent ces '
           f'points au gagnant de la ronde.\nSi un joueur vient à ne plus avoir de point, il se retire du jeu.\nDans '
           f'ce cas, il donne le nombre de points qu’il lui restait plutôt que la somme des dés joués.\nLorsqu’on '
           f'recommence une ronde, tous les joueurs retrouvent 5 dés.\nLe gagnant de la ronde précédente est celui qui '
           f'commence la nouvelle ronde.\n')


if __name__ == '__main__':

    print("Jouons une partie de pyMafia!\n")
    afficher_instructions()
    nombre_joueurs = demander_nombre_joueurs()
    nombre_joueurs_humains = demander_nombre_joueurs_humains(nombre_joueurs)
    print("\n")

    # Création de l'objet partie
    partie = Partie(nombre_joueurs, nombre_joueurs_humains)

    # Démarrage de cette partie.
    partie.jouer()

    input('Appuyer sur ENTER pour quitter.')


