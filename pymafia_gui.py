"""
Module contenant la description d'une classe pour la fenêtre du jeu Pymafia et de classes secondaires.
"""

from pymafia.partie import Partie, RONDEMAX
from tkinter import Tk, Frame, Button, Label, StringVar, DISABLED, NORMAL, Toplevel, BOTTOM
from pymafia.__main__ import afficher_instructions
import tkinter.ttk as ttk
from random import randint


class FrameJoueur(Frame):
    """
    Classe pour les frames de tous les joueurs qui prévoit les widgets communs.

    Attributs:
    joueurs (list): Liste des joueurs au départ de la partie
    nom_joueur : Nom du joueur
    label_nom_joueur: Widget du nom du joueur
    bouton_rouler_dés : Widget permettant de rouler les dés
    """

    def __init__(self, joueur, parent):
        super().__init__(parent)
        self.joueur = joueur
        self.nom_joueur = StringVar()
        self.nom_joueur.set("Joueur {}".format(self.joueur.identifiant))
        self.label_nom_joueur = Label(self, textvariable=self.nom_joueur, padx=10)
        self.bouton_rouler_dés = Button(self, command=self.rouler_dés, text="Rouler\nles\ndés")

    def rouler_dés(self):
        """
        Méthode la classe qui permet l'affiche des dés roulés.
        """
        self.joueur.rouler_dés()
        afficher_des = Label(self.master,
                             text=f'Le joueur {self.master.partie.joueur_courant.identifiant} a roulé:'
                                  f'\n       {self.master.partie.joueur_courant}       ', font=("Courier", 11))
        afficher_des.grid(row=1, column=1)

        self.master.partie.determiner_joueur_suivant(self.master.partie)

        des = self.master.partie.verifier_dés_joueur_courant_pour_1_et_6(self.master.partie)
        self.master.partie.deplacer_les_dés_1_et_6(self.master.partie, des[0], des[1])

        self.master.mettre_a_jour_des()

        if self.master.partie.verifier_si_fin_de_ronde(self.master.partie):
            for joueur in self.master.frames_joueurs:
                joueur.inactiver_bouton()
            self.master.des_fin_de_ronde()
        else:
            self.master.partie.joueur_courant = self.master.partie.joueur_suivant
            self.master.activer_bouton_joueur_courant()

    def activer_bouton(self):
        """
        Méthode permettant d'activer le bouton de roulement de dés des joueurs.
        """
        self.bouton_rouler_dés['state'] = NORMAL

    def inactiver_bouton(self):
        """
        Méthode permettant de désactiver le bouton de roulement de dés des joueurs.
        """
        self.bouton_rouler_dés['state'] = DISABLED


class FrameJoueurGauche(FrameJoueur):
    """
    Classe pour un joueur situé à gauche du plateau de jeu.

    Attributes:
        label_nom_joueur : Affiche l'étiquette du joueur, soit Joueur suivit de son numéro.
        dés_joueur1(): Dés du joueur 1.
        dés_joueur2(): Dés du joueur 2.
        self.label_dés_joueur1(): Affichage des dés roulés par le joueur 1.
        self.label_dés_joueur2(): Affichage des dés roulés par le joueur 2.
        bouton_rouler_dés(): Bouton de roulement de dés.
    """

    def __init__(self, joueur, parent):
        super().__init__(joueur, parent)

        self.label_nom_joueur.grid(row=0, column=0)

        self.dés_joueur1 = StringVar()
        self.dés_joueur1.set(str(self.joueur).replace(" ", "\n"))
        self.dés_joueur2 = StringVar()

        self.label_dés_joueur1 = Label(self, textvariable=self.dés_joueur1, font=("Courier", 32), height=5)
        self.label_dés_joueur1.grid(row=0, column=1)
        self.label_dés_joueur2 = Label(self, textvariable=self.dés_joueur2, font=("Courier", 32), width=1)
        self.label_dés_joueur2.grid(row=0, column=2)

        self.bouton_rouler_dés.grid(row=0, column=3)

    def mettre_label_dés_a_jour(self):
        """
        Méthode permettant de modifier l'affichage des dés à mesure qu'ils sont roulés par le joueur.
        """
        if len(self.joueur.dés) <= 5:
            self.dés_joueur1.set(str(self.joueur).replace(" ", "\n"))
            self.dés_joueur2.set("")
        else:
            self.dés_joueur1.set(str(self.joueur)[0:9].replace(" ", "\n"))
            self.dés_joueur2.set(str(self.joueur)[10:].replace(" ", "\n"))


class FrameJoueurDroite(FrameJoueur):
    """
    Classe pour un joueur situé à droite du plateau de jeu.

    Attributes:
        self.label_nom_joueur : Affiche l'étiquette du joueur, soit Joueur suivit de son numéro.
        dés_joueur1(): Dés du joueur 1.
        dés_joueur2(): Dés du joueur 2.
        self.label_dés_joueur1(): Affichage des dés roulés par le joueur 1.
        self.label_dés_joueur2(): Affichage des dés roulés par le joueur 2.
        self.bouton_rouler_dés(): Bouton de roulement de dés.
    """

    def __init__(self, joueur, parent):
        super().__init__(joueur, parent)

        self.label_nom_joueur.grid(row=0, column=3)

        self.dés_joueur1 = StringVar()
        self.dés_joueur1.set(str(self.joueur).replace(" ", "\n"))
        self.dés_joueur2 = StringVar()
        self.label_dés_joueur1 = Label(self, textvariable=self.dés_joueur1, font=("Courier", 32), height=5)
        self.label_dés_joueur1.grid(row=0, column=2)
        self.label_dés_joueur2 = Label(self, textvariable=self.dés_joueur2, font=('Courier', 32), width=1)
        self.label_dés_joueur2.grid(row=0, column=1)

        self.bouton_rouler_dés.grid(row=0, column=0)

    def mettre_label_dés_a_jour(self):
        """
        Méthode permettant de modifier l'affichage des dés à mesure qu'ils sont roulés par le joueur.
        """
        if len(self.joueur.dés) <= 5:
            self.dés_joueur1.set(str(self.joueur).replace(" ", "\n"))
            self.dés_joueur2.set("")
        else:
            self.dés_joueur1.set(str(self.joueur)[0:9].replace(" ", "\n"))
            self.dés_joueur2.set(str(self.joueur)[10:].replace(" ", "\n"))


class FrameJoueurHaut(FrameJoueur):
    """
    Classe pour un joueur situé en haut du plateau de jeu

    Attributes:
        label_nom_joueur : Affiche l'étiquette du joueur, soit Joueur suivit de son numéro.
        self.dés_joueur1(): Dés du joueur 1.
        self.dés_joueur2(): Dés du joueur 2.
        self.label_dés_joueur1(): Affichage des dés roulés par le joueur 1.
        self.label_dés_joueur2(): Affichage des dés roulés par le joueur 2.
        bouton_rouler_dés(): Bouton de roulement de dés.
    """

    def __init__(self, joueur, parent):
        super().__init__(joueur, parent)

        self.label_nom_joueur.grid(row=0, column=0)

        self.dés_joueur = StringVar()
        self.dés_joueur.set(str(self.joueur).replace(" ", ""))
        self.label_dés_joueur = Label(self, textvariable=self.dés_joueur, font=("Courier", 32), width=14)
        self.label_dés_joueur.grid(row=1, column=0)

        self.bouton_rouler_dés.grid(row=2, column=0)

    def mettre_label_dés_a_jour(self):
        """
        Méthode permettant de modifier l'affichage des dés à mesure qu'ils sont roulés par le joueur.
        """
        self.dés_joueur.set(str(self.joueur).replace(" ", ""))


class FrameJoueurBas(FrameJoueur):
    """
    Classe pour un joueur situé en bas du plateau de jeu

    Attributes:
        label_nom_joueur : Affiche l'étiquette du joueur, soit Joueur suivit de son numéro.
        self.dés_joueur1(): Dés du joueur 1.
        self.dés_joueur2(): Dés du joueur 2.
        self.label_dés_joueur1(): Affichage des dés roulés par le joueur 1.
        self.label_dés_joueur2(): Affichage des dés roulés par le joueur 2.
        bouton_rouler_dés(): Bouton de roulement de dés.
    """

    def __init__(self, joueur, parent):
        super().__init__(joueur, parent)

        self.label_nom_joueur.grid(row=2, column=0)

        self.dés_joueur = StringVar()
        self.dés_joueur.set(str(self.joueur).replace(" ", ""))
        self.label_dés_joueur = Label(self, textvariable=self.dés_joueur, font=("Courier", 32), width=14)
        self.label_dés_joueur.grid(row=1, column=0)

        self.bouton_rouler_dés.grid(row=0, column=0)

    def mettre_label_dés_a_jour(self):
        """
        Méthode permettant de modifier l'affichage des dés à mesure qu'ils sont roulés par le joueur.
        """
        self.dés_joueur.set(str(self.joueur).replace(" ", ""))


class FenetrePymafia(Tk):
    """
    Classe principale du module pour l'interface du jeu pymafia.
    Attributes:
        self.title : Titre du jeu.
        bouton_instructions : Bouton permettant l'affichage des instructions.
        bouton_quitter : Bouton permettant de quitter le jeu à tout moment.
        self.bouton_demarrer : Bouton permettant de démarrer une nouvelle partie.
        partie (Partie): Données d'une partie du jeu Pymafia.
        frames_joueurs (list): Liste contenant les frames des 4 joueurs de la partie. Les index sont:
        0, joueur à gauche; 1, joueur en haut; 2, joueur à droite; 3, joueur en bas.
    """

    def __init__(self):
        super().__init__()
        self.title("Jeu de pymafia")
        self.resizable(0, 0)
        self.partie = Partie

        self.bouton_instructions = Button(self, command=self.afficher_fenetre_instructions,
                                          text="Afficher les instructions")
        self.bouton_instructions.grid(row=0, column=0, sticky='NW')

        self.bouton_quitter = Button(self, command=self.quitter_pymafia, text='Quitter')
        self.bouton_quitter.grid(row=2, column=2, sticky='SE')

        self.boutton_demarrer = Button(self, command=self.demarrer_partie, text='Démarrer partie')
        self.boutton_demarrer.grid(row=0, column=2, sticky='NE')

        self.boutton_afficher_score = Button(self, command=self.afficher_score, text='Afficher score et ronde',
                                             state=DISABLED)
        self.boutton_afficher_score.grid(row=2, column=0, sticky='SW')

        self.frames_joueurs = []

    def afficher_fenetre_instructions(self):
        """
        Méthode permettant l'affichage des instructions.
        """
        fenetre_instructions = Toplevel(self)
        fenetre_instructions.title('Instructions')
        instructions = Label(fenetre_instructions, text=afficher_instructions())
        instructions.pack()

        bouton_ok_ins = Button(fenetre_instructions, command=fenetre_instructions.destroy, text='Ok')
        bouton_ok_ins.pack()

    def quitter_pymafia(self):
        """
        Méthode permettant de quitter le jeu.
        La vérification de l'intention du joueur est réalisée à l'aide d'une question oui/non.
           """
        fenetre_quitter = Toplevel(self)
        fenetre_quitter.geometry('300x100+900+400')
        fenetre_quitter.title('Quitter pymafia')
        text_quitter = Label(fenetre_quitter, text='Voulez vous vraiment quitter le jeu?')
        text_quitter.pack()

        boutton_oui = Button(fenetre_quitter, command=lambda: quit(), text='Oui')
        boutton_oui.pack()

        boutton_non = Button(fenetre_quitter, command=lambda: fenetre_quitter.destroy(), text='Non')
        boutton_non.pack()

    def activer_bouton_joueur_courant(self):
        """
        Méthode permettant d'activer le bouton de roulage de dés du joueur actif.
        """
        index_courant = self.partie.joueurs_actifs.index(self.partie.joueur_courant)
        for joueur in self.frames_joueurs:
            if joueur != self.frames_joueurs[index_courant]:
                joueur.inactiver_bouton()
            else:
                joueur.activer_bouton()

    def preparer_debut_partie(self):
        """
        Méthode qui permet d'afficher les joueurs selon le nombre choisi par l'utilisateur dans la fenêtre de jeu
        qui réinitialise les dés des joueurs et qui active le bouton de roulage de dés du premier joueur.
        Permet ensuite d'activer le roulage de dés successivement pour les joueurs selon le sens de jeu
        choisi par l'utilisateur. Méthode qui initialise le score des joueurs à 50.
        """
        self.partie.joueurs_actifs = self.partie.joueurs
        self.partie.joueur_courant = self.partie.premier_joueur

        index_premier = self.partie.joueurs_actifs.index(self.partie.premier_joueur)
        index_suivant = index_premier + self.partie.sens

        for frame in self.frames_joueurs:
            frame.destroy()

        self.frames_joueurs = []

        if len(self.partie.joueurs_actifs) == index_premier + 1:
            self.partie.joueur_suivant = self.partie.joueurs_actifs[0]
        else:
            self.partie.joueur_suivant = self.partie.joueurs_actifs[index_suivant]
        self.partie.ronde = 1

        for joueurs in self.partie.joueurs_actifs:
            joueurs.score = 50
            joueurs.reinitialiser_dés()

        if len(self.partie.joueurs_actifs) == 2:

            frame_joueur_gauche = FrameJoueurGauche(self.partie.joueurs_actifs[0], self)
            self.frames_joueurs.append(frame_joueur_gauche)
            frame_joueur_haut = FrameJoueurHaut(self.partie.joueurs_actifs[1], self)
            self.frames_joueurs.append(frame_joueur_haut)
            frame_joueur_gauche.grid(row=1, column=0)
            frame_joueur_haut.grid(row=0, column=1)

        elif len(self.partie.joueurs_actifs) == 3:

            frame_joueur_gauche = FrameJoueurGauche(self.partie.joueurs_actifs[0], self)
            self.frames_joueurs.append(frame_joueur_gauche)
            frame_joueur_haut = FrameJoueurHaut(self.partie.joueurs_actifs[1], self)
            self.frames_joueurs.append(frame_joueur_haut)
            frame_joueur_droite = FrameJoueurDroite(self.partie.joueurs_actifs[2], self)
            self.frames_joueurs.append(frame_joueur_droite)

            frame_joueur_gauche.grid(row=1, column=0)
            frame_joueur_haut.grid(row=0, column=1)
            frame_joueur_droite.grid(row=1, column=2)

        else:
            frame_joueur_gauche = FrameJoueurGauche(self.partie.joueurs_actifs[0], self)
            self.frames_joueurs.append(frame_joueur_gauche)
            frame_joueur_haut = FrameJoueurHaut(self.partie.joueurs_actifs[1], self)
            self.frames_joueurs.append(frame_joueur_haut)
            frame_joueur_droite = FrameJoueurDroite(self.partie.joueurs_actifs[2], self)
            self.frames_joueurs.append(frame_joueur_droite)
            frame_joueur_bas = FrameJoueurBas(self.partie.joueurs_actifs[3], self)
            self.frames_joueurs.append(frame_joueur_bas)

            frame_joueur_gauche.grid(row=1, column=0)
            frame_joueur_haut.grid(row=0, column=1)
            frame_joueur_droite.grid(row=1, column=2)
            frame_joueur_bas.grid(row=2, column=1)

        self.activer_bouton_joueur_courant()
        self.boutton_afficher_score['state'] = NORMAL

    def demander_sens(self):
        """
        Méthode qui demande à l'usager de choisir le sens dans lequel les joueurs joueront.
        """
        fenetre_sens = Toplevel(self)
        fenetre_sens.geometry('350x100+900+400')
        fenetre_sens.title('Choisir sens')
        text_sens = Label(fenetre_sens,
                          text=f'Le joueur {self.partie.premier_joueur.identifiant} à été sélectionné au hasard comme '
                               f'premier joueur.\nÀ vous de choisir '
                               f'le sens:')
        text_sens.pack()

        def sens_droit():
            """
            Méthode qui permet d'afficher le bouton de choix droit et qui permet au jeu d'être joué vers la droite.
            """
            self.partie.sens = -1
            self.preparer_debut_partie()
            fenetre_sens.destroy()

        bouton_droit = Button(fenetre_sens, command=sens_droit, text='Droite')
        bouton_droit.pack()

        def sens_gauche():
            """
            Méthode qui permet d'afficher le bouton de choix gauche et qui permet au jeu d'être joué vers la gauche.
            """
            self.partie.sens = 1
            self.preparer_debut_partie()
            fenetre_sens.destroy()

        bouton_gauche = Button(fenetre_sens, command=sens_gauche, text='Gauche')
        bouton_gauche.pack()

    def choisir_premier_joueur(self, nombre):
        """
        Méthode qui permet de déterminer aléatoirement le premier joueur. Et qui place les joueurs dans le sens choisit.
        Args:
            nombre(int): nombre de joueurs
        """
        premier_joueur = randint(0, nombre - 1)
        self.partie.premier_joueur = self.partie.joueurs[premier_joueur]
        self.demander_sens()

    def demander_combien_joueurs(self):
        """
        Méthode qui affiche une fenêtre demandant à l'usager le nombre de joueurs (entre 2 et 4) à la partie.
        """
        fenetre_cmb_joueurs = Toplevel(self)
        fenetre_cmb_joueurs.geometry('500x100+900+400')
        fenetre_cmb_joueurs.title('Nombres de joueurs')

        text_cmb_joueurs = Label(fenetre_cmb_joueurs, text='Choisissez le nombre de joueurs entre 2 et 4')
        text_cmb_joueurs.pack()

        fene = ttk.Combobox(fenetre_cmb_joueurs, values=(2, 3, 4), state='readonly')
        fene.pack()

        def prochaine_fonction():
            """
            Méthode qui permet au joueur de sélectionner le nombre de joueurs et de confirmer sa sélection
            avec un bouton ok dans la fenêtre.
            """
            nb_joueurs = int(fene.get())
            self.partie.joueurs = self.partie.creer_joueurs(nb_joueurs, nb_joueurs)
            fenetre_cmb_joueurs.destroy()
            self.choisir_premier_joueur(nb_joueurs)

        boutton_ok = Button(fenetre_cmb_joueurs, command=prochaine_fonction, text='Ok')
        boutton_ok.pack()

    def des_fin_de_ronde(self):
        """
        Méthode qui affiche la fenêtre de fin de ronde, incluant l'affichage du gagnant.
        Méthode qui permet de lancer les dés en fin de ronde afin de calculer les points de chacun des joueurs.
        """
        fenetre_fin_de_ronde = Toplevel(self)
        fenetre_fin_de_ronde.geometry('700x350+900+400')
        fenetre_fin_de_ronde.title('Lancé de dés fin de ronde!')

        text_fin_de_ronde = Label(fenetre_fin_de_ronde, text=f'La ronde {self.partie.ronde} est terminé!\nLe joueur '
                                                             f'{self.partie.joueur_courant.identifiant} est le '
                                                             f'gagnant de cette ronde\nAppuyez sur '
                                                             f'\'Rouler\' pour rouler les dés de chaque '
                                                             'joueurs et déterminer les points de fin de partie.')
        text_fin_de_ronde.pack()

        for joueur in self.frames_joueurs:
            joueur.inactiver_bouton()

        def continuer_partie():
            """
            Méthode qui augmente de 1 le nombre de ronde à chacune des fins de ronde. Méthode qui demande à l'individu
            de poursuivre le jeu.
            """
            boutton_quitter = Button(fenetre_fin_de_ronde, command=continuer, text='Continuer')
            boutton_quitter.pack()
            self.partie.ronde += 1

        def continuer():
            """
            Méthode qui permet de vérifier que la ronde actuelle est inférieure au nombre de ronde maximale.
            Méthode qui réinitialise les dés des joueurs et qui active le bouton de roulage de dés du gagnant.
            La fenêtre de fin de ronde est fermée.
            """
            if self.partie.ronde > RONDEMAX:
                self.fin_de_partie()
            else:
                self.partie.reinitialiser_dés_joueurs(self.partie)
                self.mettre_a_jour_des()
                self.activer_bouton_joueur_courant()

            fenetre_fin_de_ronde.destroy()

        def afficher_score():
            """
            Méthode qui permet d'afficher les points obtenus par les dés brassés par les perdants.
            Un widget demande en suite à l'utilisateur de cliquer sur continuer pour poursuivre.
            """
            message_1 = self.partie.messages_pour_points_fin_de_ronde(self.partie)
            message_2 = self.partie.message_points_en_fin_de_ronde(self.partie)
            text_score = Label(fenetre_fin_de_ronde, text=f'{message_1}{message_2}\nAppuyez sur continuer '
                                                          f'pour passer à la prochaine ronde')
            text_score.pack()
            continuer_partie()

        def mettre_a_jour_score():
            """
            Méthode qui permet de calculer les scores de tous les joueurs.
            """
            score = self.partie.ajuster_points_des_perdants_en_fin_de_ronde(self.partie)
            self.partie.ajuster_points_du_gagnant(self.partie, score)
            afficher_score()

        def commande_rouler():
            """
            Méthode de désactiver les dés brassés par les perdants en fin de ronde.
            """
            self.partie.jouer_dés_en_fin_de_ronde(self.partie)
            mettre_a_jour_score()
            boutton_rouler["state"] = DISABLED

        boutton_rouler = Button(fenetre_fin_de_ronde, command=commande_rouler, text='Rouler')
        boutton_rouler.pack()

    def afficher_score(self):
        """
        Méthode qui permet d'afficher les scores de tous les joueurs dans un tableau des scores, ainsi
        que le numéro de la ronde qui s'entame.
        """
        fenetre_afficher_score = Toplevel(self)
        fenetre_afficher_score.geometry('250x150+900+400')
        fenetre_afficher_score.title('Tableau de score')
        liste_score = []
        for joueur in self.partie.joueurs_actifs:
            liste_score.append(joueur.score)
        message = ''
        for e in range(len(liste_score)):
            message += f'Le score du joueurs {self.partie.joueurs_actifs[e].identifiant} ' \
                       f'est de: {self.partie.joueurs_actifs[e].score}\n'
        score = Label(fenetre_afficher_score, text=f'Ronde : {self.partie.ronde}\n\n{message}')
        score.pack()

        bouton_ok = Button(fenetre_afficher_score, command=fenetre_afficher_score.destroy, text='Ok')
        bouton_ok.pack()

    def fin_de_partie(self):
        """
        Méthode qui détecte la fin de partie et affiche sa fenêtre: liste des joueurs, leurs points respectifs
        et affichage du gagnant. Message précisant au joueur qui pourra quitter ou recommencer une partie dans la
        fenêtre principale est également affiché.
        """
        fenetre_fin_de_partie = Toplevel(self)
        fenetre_fin_de_partie.geometry('400x250+900+400')
        fenetre_fin_de_partie.title('Fin de la partie')

        message_fin_partie_1 = self.partie.message_points_en_fin_de_partie(self.partie)
        liste_gagnant = self.partie.determiner_liste_gagnants(self.partie)
        message_fin_partie_2 = self.partie.message_gagnants(self.partie, liste_gagnant)

        text_fin_de_ronde = Label(fenetre_fin_de_partie, text=f'La partie est terminée.\n\n{message_fin_partie_1}\n '
                                                              f'{message_fin_partie_2}\n\nVous pouvez démarrer une '
                                                              f'nouvelle partie \nou\nquitter le jeu dans la fenêtre '
                                                              f'suivante.')
        text_fin_de_ronde.pack()

        bouton_ok_merci = Button(fenetre_fin_de_partie, command=fenetre_fin_de_partie.destroy, text='Ok merci et '
                                                                                                    'bon été!')
        bouton_ok_merci.pack()

    def mettre_a_jour_des(self):
        """
        Méthode qui reset les dés des joueurs de l'interface.
        """
        for joueur in self.frames_joueurs:
            joueur.mettre_label_dés_a_jour()

    def demarrer_partie(self):
        """
        Méthode qui permet de débuter une nouvelle partie. Méthode qui efface les joueurs contenus dans l'interface
        s'il y a lieu.
        """
        fenetre_demarrer = Toplevel(self)
        fenetre_demarrer.geometry('300x100+900+400')
        fenetre_demarrer.title('Démarrer une nouvelle partie')
        text_demarrer = Label(fenetre_demarrer, text='Êtes vous sûr de vouloir débuter une nouvelle partie?')
        text_demarrer.pack()

        def prochaine_fonction():
            """
            Méthode qui valide le choix de débuter une nouvelle partie avec une question Oui/Annuler, répondue
            avec des boutons.
            """
            self.demander_combien_joueurs()
            fenetre_demarrer.destroy()

        frame_boutons_demarrer = Frame(fenetre_demarrer)
        frame_boutons_demarrer.pack(side=BOTTOM)

        boutton_oui = Button(frame_boutons_demarrer, command=prochaine_fonction, text='Oui')
        boutton_oui.grid(row=0, column=0)

        boutton_annuler = Button(frame_boutons_demarrer, command=lambda: fenetre_demarrer.destroy(), text='Annuler')
        boutton_annuler.grid(row=0, column=2)


if __name__ == '__main__':
    fenetre_pymafia = FenetrePymafia()
    fenetre_pymafia.mainloop()
