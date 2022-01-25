def activer_bouton_joueur_courant(self):
    index_courant = self.partie.joueurs_actifs.index(self.partie.joueur_courant)
    for joueur in self.frames_joueurs:
        if joueur != self.frames_joueurs[index_courant]:
            joueur.inactiver_bouton()
        else:
            joueur.activer_bouton()


def preparer_debut_partie(self):
    self.partie.joueurs_actifs = self.partie.joueurs
    self.partie.joueur_courant = self.partie.premier_joueur

    index_premier = self.partie.joueurs_actifs.index(self.partie.premier_joueur)
    index_suivant = index_premier + self.partie.sens

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