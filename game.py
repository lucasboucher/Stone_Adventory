from random import *
import time

senku = [20]

adversaires = [["un tigre", 10, "boss","de la fourrure majestueuse"],["Tsukasa", 20, "boss","des points de conquête"],["Homura", 30, "boss","des points de conquête"],["Tsukasa et ses compagnons", 40, "boss","les respects de la faction adverse"],["un ours", 5, "no_boss","de la fourrure"],["une chauve-souris", 10, "no_boss","de l'acide"],["un aigle", 15, "no_boss","des plumes"],["un requin", 20, "no_boss","de la viande"]]
capacites = [["un coup de pied", 3], ["une droite", 2],["un coup de genou", 3], ["un coup de coude", 2], ["un coup de tête", 1]]

parametres_delai = [0.1, 0.25, 0.50, 1]

def RoomDisposition(disposition):
    count = 0
    room = 1
    while count  < 8:
        k = randint(0,len(disposition)-1)
        j = randint(0,len(disposition[0])-1)
        if disposition[k][j] ==  0:
            disposition[k][j] = room
            count+= 1
            room += 1


def Combat(adversaire,etage):
    if etage < 0 :
          capacites.append(["Témérité de Taiju", 4])
    if etage < 3:
          capacites.append(["Lame de Yuzuriha", 6])
    #BossDown = False
#Définition des varibales de l'adversaire et de senku
    vie_adversaire = adversaires[adversaire][1]
    vie_max_adversaire = adversaires[adversaire][1]
    vie_senku = senku[0]
    nom_adversaire = adversaires[adversaire][0]
    boss_or_not = adversaires[adversaire][2]
    drop = adversaires[adversaire][3]

    print("Attention, vous être tombé nez à nez avec ",nom_adversaire,".", sep = '') 
    #Pour les séprations du print() --> https://www.geeksforgeeks.org/python-sep-parameter-print/
    
    nbr_tour = -1
    Premier_Tour = True

    while vie_adversaire > 0:
        nbr_tour = nbr_tour + 1
        time.sleep(parametres_delai[2])
        if boss_or_not == "boss" and Premier_Tour == True:
            Premier_Tour = False
            print("Il vous attaque sans hésiter:")
            attaque_adversaire = randint(1,3)
            vie_senku = vie_senku - attaque_adversaire
            time.sleep(parametres_delai[1])
            if vie_senku < 0:
                print("Vous perdez",attaque_adversaire,"points de vie.")
                time.sleep(parametres_delai[1])
                print("Vous êtes mort en",nbr_tour,"tours, vous avez perdu le combat...")
                time.sleep(parametres_delai[2])
                Menu()
                break
            else:
                print("Votre adversaire,",nom_adversaire,", vous attaque... Vous perdez",attaque_adversaire,"points de vie. Il vous en reste",vie_senku,"!")
                time.sleep(parametres_delai[2])
        print()
        print("¯¯¯¯¯ Combat en cours ¯¯¯¯¯")
        print()
        time.sleep(parametres_delai[2])
        combat_index = 0
        nombre_capacites = len(capacites)
        while nombre_capacites > 0:
            print("    ",combat_index+1,".  Avec ",capacites[combat_index][0], sep = "")
            combat_index = combat_index + 1
            nombre_capacites = nombre_capacites - 1
            time.sleep(parametres_delai[0])
        print("")
        choix_capacite = int(input("Comment voulez-vous attaquer ? "))
        if choix_capacite > len(capacites) or choix_capacite <= 0:
            print("Erreur : Cette capacité n'existe pas !")
        else:
            vie_adversaire = vie_adversaire - capacites[choix_capacite-1][1]
            print("_____________________________")
            print()
            time.sleep(parametres_delai[2])
            if vie_adversaire > (vie_max_adversaire/3):
                print("Vous avez envoyé",capacites[choix_capacite-1][0],"! Il lui reste",vie_adversaire,"points de vie.")
                attaque_adversaire = randint(1,3)
                vie_senku = vie_senku - attaque_adversaire
                time.sleep(parametres_delai[1])
                if vie_senku < 0:
                    print("Votre adversaire,",nom_adversaire,", vous attaque... Vous perdez",attaque_adversaire,"points de vie.")
                    time.sleep(parametres_delai[1])
                    print("Vous êtes mort en",nbr_tour,"tours, vous avez perdu le combat...")
                    time.sleep(parametres_delai[2])
                    Menu()
                    break
                else:
                    print("Votre adversaire,",nom_adversaire,", vous attaque... Vous perdez",attaque_adversaire,"points de vie. Il vous en reste",vie_senku,"!")
                    time.sleep(parametres_delai[2])
            elif vie_adversaire > 0:
                print("Vous avez envoyé",capacites[choix_capacite-1][0],"! Il lui reste",vie_adversaire,"points de vie.")
                time.sleep(parametres_delai[1])
                print("Il ne lui reste plus beaucoup de vie. Attention, il enrage et ses dégâts augmentent !")
                attaque_adversaire = randint(2,4)
                vie_senku = vie_senku - attaque_adversaire
                time.sleep(parametres_delai[1])
                if vie_senku < 0:
                    print("Votre adversaire,",nom_adversaire,", vous attaque... Vous perdez",attaque_adversaire,"points de vie.")
                    time.sleep(parametres_delai[1])
                    print("Vous êtes mort en",nbr_tour,"tours, vous avez perdu le combat...")
                    time.sleep(parametres_delai[2])
                    Menu()
                    break
                else:
                    print("Votre adversaire,",nom_adversaire,", vous attaque... Vous perdez",attaque_adversaire,"points de vie. Il vous en reste",vie_senku,"!")
                    time.sleep(parametres_delai[2])
            else:
                print("¯¯¯¯¯¯ BRAVO ¯¯¯¯¯¯")
                time.sleep(parametres_delai[0])
                print("Bravo ! Vous avez battu",nom_adversaire,"! Vous avez obtenu",drop)
                time.sleep(parametres_delai[1])
                print("N'oubliez pas de vous soigner. Vous avez encore",vie_senku,"points de vie !")
                #if boss_or_not =="boss":
                  #BossDown = True
                print("___________________")
                time.sleep(parametres_delai[2])

#def BossKilled(BossDown,floor):
 # if Bossdown == True:
  #  print("Vous avez découvert une nouvelle zone")
   # floor+= 1
  #return floor




def BossRoom(floor): #Cinématiques 
    if floor == 1:
         Combat(0,floor)
    if floor == 2:
         Combat(1,floor)
    if floor == 3:
         Combat(2,floor)
    if floor == 4:
         Combat(3,floor)

def Fights(floor):
    Combat(4,floor)
    if floor > 1:
      opponent = randint(4,5)
      Combat(opponent,floor)
    if floor > 2:
      opponent = randint(4,6)
      Combat(opponent,floor)    
    if floor > 3:
      opponent = randint(4,7)
      Combat(opponent,floor) 

def Objects(floor):
    ressources = ["bois","fruits","Herbes médicinales","Eau"] 
    if floor > 1:
        ressources.append("coton")
    if floor > 2:
        ressources.append("charbon")
        ressources.append("sable")
    if floor > 3:
        ressources.append("fer")
    Loot = UsableObjects(ressources)
    print("Vous avez trouver plusieurs objets dans les alentours : ")
    print("")
    for i in Loot:
      print(i)

def UsableObjects(ressources):
    usableObjects = choices(ressources,k=3)
    return usableObjects

def Landscape():
  print("    Vous admirez un beau paysage")

def CompagnonRoom(etage):
  compagnon = []
  if etage==1 :
    compagnon.append("Taiju")
    compagnon.append("Tsukasa")
  if etage==3:
    compagnon.append("Yuzuriha")
  for i in compagnon:
        print(i +"a rejoint votre équipe")

  
  
def WhereAmI(disposition,indexC,indexL,etage):
    room = disposition[indexL][indexC]
    if room == 0:
      Landscape()
    if room == 1:
      Spawn()
    if room == 2:
      Fights(etage)
    if room == 3:
      Objects(etage)
    if room == 4:
      BossRoom(etage)
    if room == 5:
      CompagnonRoom(etage)
    if room == 6:
      Mission(etage)
    if room == 7:
      Objects(etage)

def Navigation(line,column,directions):  
    for i in (directions):
        print(i)
    print("")
    direction = input("Où voulez vous allez ? ")
    print("___________________________________")
    if direction == "N":
        line = line - 1
    if direction == "O":
        column = column - 1
    if direction == "S":
        line = line + 1
    if direction == "E":
        column = column + 1
    return line,column
    
def PossibleDirection(indexL,indexC,grid):
    directions = []
    if indexL + 1  < 3:
        directions.append("    S.  Au sud")
    if indexC + 1 < 3:
        directions.append("    E.  À l'est")
    if indexL - 1 > -1:
        directions.append("    N.  Au nord") 
    if indexC - 1 > -1:
        directions.append("    O.  À l'ouest")
    return directions

def Spawn():
  print("Te revoilà là où tout à commencer !")

def Display(disposition):
    for i in range(len(disposition)):
        for j in range(len(disposition[i])):
            print(disposition[i][j], end=' ')
        print()  


mission_carte = False
mission_metal = False
mission_carte = False
mission_feu = False

def NewSkill(etage):
  if etage == 0:
    mission_acide = True
    print("Vous pouvez désormais faire de l'acide !")
  elif etage == 1:
    mission_feu = True
    print("Vous pouvez désormais faire du feu !")
  elif etage == 2:
    mission_carte = True
    print("Vous pouvez désormais lire la carte !")
  elif etage == 3:
    mission_metal = True
    print("Vous pouvez désormais forger le métal !")

def Mission(etage):
  print("Dans cette mission vous devez trouver le nombre coresspond à cette suite logique :")
  index_suite = 0
  logique = 0
  while logique == 0:
    logique = randint(-9, 9)
  nombre_suite = randint(50, 200)
  while index_suite < 5:
    if index_suite == 2:
      nombre_suite = nombre_suite + logique
      resultat_suite = nombre_suite
      print("...")
      index_suite = index_suite + 1
    else:
      nombre_suite = nombre_suite + logique
      print(nombre_suite)
      index_suite =  index_suite + 1
  resultat_joueur = int
  while resultat_suite != resultat_joueur:
    print("Votre nombre :")
    resultat_joueur = int(input())
    if resultat_suite == resultat_joueur:
      print("Bravo ! Vous avez débloqué une nouvelle compétence.")
      NewSkill(etage)
      break
    else:
      print("Vous avez perdu ! Réessayez !")

def Game():
  print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
  print("")
  print("Il y a 5 milliers d'années, une lueur verte jaillit du ciel et transforma l'humanité en statue...")
  print("Mais aujourd'hui, toi Senku, es parvenu à te délivrer de ta prison de pierre constatant que le monde est redevenu à l'état sauvage.")
  print("Scientifique né, tu te donnes pour mission de rétablir la civilisation telle que tu l'as connue.")
  print("Après quelques minutes de marche te voilà nez à nez avec la statue de Taiju, ton meilleur ami !")
  disposition = [[0,0,0],[0,0,0],[0,0,0]]
  etage = 1
  stop = False
  Display(disposition)
  print("")

  RoomDisposition(disposition)
  Display(disposition)
  print("")
  print("    Tu viens d'arriver dans une nouvelle zone !")
  print("")
  print("___________________________________")
  for i in range(3):
    for j in range(3):
      if disposition[i][j] == 1:
        indexL = i
        indexC = j
  while stop == False:
    directions = PossibleDirection(indexL,indexC,disposition)
    print("")
    PosL,PosC = Navigation(indexL,indexC,directions)
    print("")
    WhereAmI(disposition,PosL,PosC,etage)
    indexL = PosL
    indexC = PosC
    print("")
    #etage = BossKilled(BossDown,etage)
    arret = input("Voulez-vous continuer ? (Oui/Non) ")
    print("___________________________________")
    if arret == "Non":
      stop = True
      break

  
def Credits():
    print("¯¯¯¯¯¯¯ Concepteurs du jeu ¯¯¯¯¯¯¯")
    print("> Lucas BOUCHER")
    print("> Joakim DOMNGANG")
    print("> Félix GIRARD")
    print("> Meri HOVHANNISYAN")
    print("------- Autres informations -------")
    print("Projet RPG en Python à HETIC - H1")
    print("Intervenant : Loïc JANIN")
    print("__________________________________")
    print("")
    Menu()

def About():
  print("----- À propos de Stone Adventure -----")
  print("")
  print("Un RPG textuel retraçant l'histoire du personnage principal de Dr. Stone.")
  print("Ce jeu utilise comme technologie le langage de programmation Python.")
  print("Ont été également utilisés, les librairies 'time' et 'random'.")
  print("")
  print("_______________________________________")
  print("")
  Menu()

def Menu():
  print("¯¯¯¯¯ Menu de Stone Adventure ¯¯¯¯¯")
  print("")
  print("1 -> NOUVELLE PARTIE")
  print("2 -> À PROPOS")
  print("3 -> CRÉDITS")
  print("4 -> QUITTER")
  print("")
  print("___________________________________")
  print("")
  choix = int(input("Que voulez-vous faire ? "))
  print("")
  if choix == 1:
    Game()
  if choix == 2:
    About()
  if choix == 3:
    Credits()
  if choix == 4:
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("Arrêt du jeu...")
    print("_______________")
  
Menu()