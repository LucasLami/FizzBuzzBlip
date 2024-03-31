import tkinter as tk
import random
from tkinter import simpledialog, messagebox
import xml.etree.ElementTree as ET
import threading
import pygame

class FizzBuzzBlipGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FizzBuzz Blip")
        self.geometry("400x300")
        
        self.numero_courant = None
        self.temps_reponse = 10
        self.scores_partie = {}
        self.scores_fichier = {}
        self.joueurs = []

        self.charger_scores()

        self.setup_ui()
    
    def setup_ui(self):
        self.label_nombre_joueurs = tk.Label(self, text="Entrez le nombre de joueurs : ")
        self.label_nombre_joueurs.pack()
        
        self.nombre_joueurs_entry = tk.Entry(self, width=10)
        self.nombre_joueurs_entry.pack()
        
        self.bouton_nombre_joueurs = tk.Button(self, text="Valider", command=self.entrer_nombre_joueurs)
        self.bouton_nombre_joueurs.pack()

    def entrer_nombre_joueurs(self):
        nb_joueurs = int(self.nombre_joueurs_entry.get())
        for i in range(nb_joueurs):
            nom_joueur = simpledialog.askstring("Nom du joueur", f"Entrez le nom du joueur {i + 1}: ")
            self.joueurs.append(nom_joueur)
            if nom_joueur not in self.scores_fichier:
                self.scores_fichier[nom_joueur] = 0
            if nom_joueur not in self.scores_partie:
                self.scores_partie[nom_joueur] = 0
        
        self.nouvelle_partie()

    def nouvelle_partie(self):
        self.label_nombre_joueurs.destroy()
        self.nombre_joueurs_entry.destroy()
        self.bouton_nombre_joueurs.destroy()
        
        self.jouer_fizzbuzz_blip()

    def jouer_fizzbuzz_blip(self):
        self.label_numero = tk.Label(self, text=f"Nombre actuel: {self.numero_courant}")
        self.label_numero.pack()

        self.nouveau_nombre_courant()
        
        self.label_temps_restant = tk.Label(self, text="Temps restant: ")
        self.label_temps_restant.pack()
        
        self.label_joueur = tk.Label(self, text="")
        self.label_joueur.pack()
        
        self.frame_boutons = tk.Frame(self)
        self.frame_boutons.pack()

        self.bouton_fizz = tk.Button(self.frame_boutons, text="Fizz", command=lambda: self.verifier_reponse("Fizz"))
        self.bouton_fizz.pack(side=tk.LEFT, padx=5, pady=5)
        self.bouton_buzz = tk.Button(self.frame_boutons, text="Buzz", command=lambda: self.verifier_reponse("Buzz"))
        self.bouton_buzz.pack(side=tk.LEFT, padx=5, pady=5)
        self.bouton_fizzbuzz = tk.Button(self.frame_boutons, text="FizzBuzz", command=lambda: self.verifier_reponse("FizzBuzz"))
        self.bouton_fizzbuzz.pack(side=tk.LEFT, padx=5, pady=5)
        self.bouton_blip = tk.Button(self.frame_boutons, text="Blip", command=lambda: self.verifier_reponse("Blip"))
        self.bouton_blip.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.label_scores = tk.Label(self, text="")
        self.label_scores.pack()

        self.actualiser_infos_joueur()

    def actualiser_infos_joueur(self):
        if self.joueurs:
            score_text = "\n".join([f"{nom}: {self.scores_partie[nom]}" for nom in self.joueurs])
            self.label_scores.config(text=score_text)
        else:
            self.label_scores.config(text="Fin du jeu")

        self.label_temps_restant.config(text=f"Temps restant: {self.temps_reponse}")
        if self.joueurs:
            self.label_joueur.config(text=f"Joueur : {self.joueurs[0]}")
        else:
            self.label_joueur.config(text="Fin du jeu")

    def jouer_prochain_joueur(self):
        if self.joueurs:
            self.temps_reponse = 10
            joueur_suivant = self.joueurs.pop(0)
            self.joueurs.append(joueur_suivant)
            self.actualiser_infos_joueur()
            self.nouveau_nombre_courant()

    def verifier_reponse(self, choix):
        joueur_actuel = self.joueurs[0]
        if self.numero_courant % 3 == 0 and self.numero_courant % 5 == 0:
            if choix != "FizzBuzz":
                self.afficher_gagnant()
                return
        elif self.numero_courant % 3 == 0:
            if choix != "Fizz":
                self.afficher_gagnant()
                return
        elif self.numero_courant % 5 == 0:
            if choix != "Buzz":
                self.afficher_gagnant()
                return
        else:
            if choix != "Blip":
                self.afficher_gagnant()
                return

        self.scores_partie[joueur_actuel] += 1
        self.jouer_prochain_joueur()

    def nouveau_nombre_courant(self):
        self.numero_courant = random.randint(1, 100)
        self.label_numero.config(text=f"Nombre actuel: {self.numero_courant}")

    def afficher_gagnant(self):
        if self.joueurs:
            joueur_actuel = self.joueurs[0]
            if self.scores_partie[joueur_actuel] > self.scores_fichier.get(joueur_actuel, 0):
                self.scores_fichier[joueur_actuel] = self.scores_partie[joueur_actuel]
                self.sauvegarder_scores()
            joueur_suivant = self.joueurs[1]
            if self.scores_partie[joueur_suivant] > self.scores_fichier.get(joueur_suivant, 0):
                self.scores_fichier[joueur_suivant] = self.scores_partie[joueur_suivant]
                self.sauvegarder_scores()
                joueur_actuel = joueur_suivant
            else:
                joueur_actuel = None
            if joueur_actuel:
                message = f"{joueur_actuel} a gagné avec un score de {self.scores_partie[joueur_actuel]} !\nVoulez-vous rejouer avec les mêmes joueurs ?"
            else:
                message = "Le joueur a répondu incorrectement. Le joueur adverse gagne !\nVoulez-vous rejouer avec les mêmes joueurs ?"
            if messagebox.askyesno("Partie terminée", message):
                self.nouvelle_partie()
            else:
                self.rejouer_avec_nouveaux_joueurs()

    def rejouer_avec_nouveaux_joueurs(self):
        self.destroy()
        FizzBuzzBlipGUI().mainloop()

    def charger_scores(self):
        try:
            tree = ET.parse("scores.xml")
            root = tree.getroot()
            for joueur in root.findall("joueur"):
                nom_joueur = joueur.get("nom")
                score = int(joueur.text)
                self.scores_fichier[nom_joueur] = score
        except FileNotFoundError:
            self.scores_fichier = {}

    def sauvegarder_scores(self):
        root = ET.Element("scores")
        for nom, score in self.scores_fichier.items():
            joueur = ET.SubElement(root, "joueur")
            joueur.set("nom", nom)
            joueur.text = str(score)
        
        tree = ET.ElementTree(root)
        tree.write("scores.xml")

def jouer_musique():
    pygame.mixer.init()
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.play(-1)

if __name__ == "__main__":
    # Démarrage de la musique en arrière-plan
    threading.Thread(target=jouer_musique).start()

    app = FizzBuzzBlipGUI()
    app.mainloop()
