import random
import time

def jouer_fizzbuzz_blip():
  """Fonction principale pour jouer au FizzBuzz avec Blip."""
  joueurs = []
  noms_joueurs = []
  scores = {}
  temps_reponse = 10

  # Début du jeu
  print("**Début du jeu FizzBuzz Blip !**")

  # Demande du nombre de joueurs
  nb_joueurs = int(input("Entrez le nombre de joueurs: "))

  # Boucle pour entrer les noms des joueurs
  for i in range(nb_joueurs):
    nom = input(f"Entrez le nom du joueur {i + 1}: ")
    noms_joueurs.append(nom)
    joueurs.append(nom)
    scores[nom] = 0

  numero_courant = random.randint(1, 100)  # Choisir un nombre aléatoire entre 1 et 100
  while len(joueurs) > 1:
    for joueur in joueurs:
      print(f"\nAu tour du joueur : {joueur}")

      print(f"\nLe nombre demandé est : {numero_courant:<20}")

      # Use a loop counter for remaining time
      temps_restant = temps_reponse  # Initialize remaining time

      print(f"**Temps restant: {temps_restant} secondes**")

      print("Choisissez parmi :")
      print("1. Fizz")
      print("2. Buzz")
      print("3. FizzBuzz")
      print("4. Blip")

      # Saisie du choix du joueur
      choix = input("Votre choix (1-4): ")

      # Début du chronomètre
      debut_temps = time.time()

      # Contrôle du temps imparti
      if time.time() > debut_temps + temps_reponse:
        print("\n")
        print(f"{noms_joueurs[joueurs.index(joueur)]} a perdu ! Dépassement du temps imparti !")
        joueurs.remove(joueur)
        break

      # Arrêt du chronomètre
      fin_temps = time.time()

      # Calcul du temps de réponse
      temps_reponse_joueur = fin_temps - debut_temps

      # Validation de la réponse du joueur
      if numero_courant % 3 == 0 and numero_courant % 5 == 0:
        if choix != "3":
          print(f"{noms_joueurs[joueurs.index(joueur)]} a perdu !")
          joueurs.remove(joueur)
          break
        else:
          scores[joueur] += 1
      elif numero_courant % 3 == 0:
        if choix != "1":
          print(f"{noms_joueurs[joueurs.index(joueur)]} a perdu !")
          joueurs.remove(joueur)
          break
        else:
          scores[joueur] += 1
      elif numero_courant % 5 == 0:
        if choix != "2":
          print(f"{noms_joueurs[joueurs.index(joueur)]} a perdu !")
          joueurs.remove(joueur)
          break
        else:
          scores[joueur] += 1
      elif numero_courant % 3 != 0 and numero_courant % 5 != 0:
        if choix != "4":
          print(f"{noms_joueurs[joueurs.index(joueur)]} a perdu !")
          joueurs.remove(joueur)
          break
        else:
          scores[joueur] += 1

      # Affichage du score
      for nom, score in scores.items():
        print(f"{nom}: {score}")

      # Diminution du temps de réponse si les deux joueurs atteignent 10 points
      if scores[joueurs[0]] >= 10 and scores[joueurs[1]] >= 10:
        temps_reponse = 5

      numero_courant = random.randint(1, 100)  # Choisir un nouveau nombre aléatoire

  # Affichage du gagnant
  if len(joueurs) == 1:
    print(f"\n{joueurs[0]} a gagné !")
    
 # Début du jeu
jouer_fizzbuzz_blip()
