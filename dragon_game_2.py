nom =input("Tapez votre nom : ")
print("Bonjour "+ nom)


print("Tu te trouves dans une pièce obscure d'un mystérieux château.")
print("Tu dois choisir entre 4 portes pour continuer ton aventure.")

gamerChoice = input("Choisis 1,2, 3 ou 4...")

if gamerChoice == "1":
    print(nom +", tu te retrouves face à un dragon endormi, ton haleine fetide le réveille !")
    print("Tu es mort ! Brosse-toi les dents la prochaine fois !")
    print("Relance le jeu avec la commande python dragon_game_2.py "+nom)
elif gamerChoice == "2":
    print("Derrière la porte se trouve la queue d'un dragon.")
    print("Tu peux soit :")
    print("1) Le réveiller vu que tu ne t'es sûrement pas brossé les dents !")
    print("2) Fermer la porte")
    dragonChoice = input("Entre 1 ou 2... ")
    if dragonChoice == "1":
        print(nom+", tu as réveillé le dragon ! Tu es mort !")
        print("Brosse-toi les dents bordel !")
        print(nom+", si tu veux essayer à nouveau, relance le jeu avec la commande python dragon_game_2.py ")
    elif dragonChoice == "2":
        print("Tu as fermé la porte et tu peux retenter ta chance ! (c'est la 4, si tu es un peu neuneu)")
        gamerChoice = input("Choisis 1,2, 3 ou 4... ")
        if gamerChoice == "1":
            print(nom+", tu te retrouves face à un dragon endormi, ton haleine fetide le réveille !")
            print("Tu es mort ! Brosse-toi les dents la prochaine fois !") 
            print("Relance le jeu avec la commande python dragon_game_2.py "+nom)
        elif gamerChoice == "2":
            print("T'es pas futfut " +nom+ ", tu es revenu dans la même pièce !")
            print("Et le dragon est toujours là !")
            print("Laisse toi bouffer, tu le mérites !")
            print("Tu veux encore essayer "+nom+ ", relance le jeu avec la commande python dragon_game_2.py " )
            
        elif gamerChoice == "3":
            print("Tu as trouvé un sac de croquette !")
            print("Bravo" +nom+ ", si on veut... tu peux toujours essayer de les donner au dragon !")
        elif gamerChoice == "4":
            print("Tu as fait toutes les portes, casse-toi de mon château maintenant !")
            print("Et n'oublie pas le chat !!! ")
            print("Oui " +nom+ ", il y avait un chat")
            print("Je parie que tu as donné les croquettes au dragon !")
            
        else:
            print("Apparement tu ne sais pas ce qu'est un chiffre entre 1 et 2.")
elif gamerChoice == "3":
    print("Tu as trouvé un sac de croquette !")
    print("Bravo " +nom+ ", si on veut... tu peux toujours essayer de les donner au dragon !")
elif gamerChoice == "4":
    print("Tu as fait toutes les portes, casse-toi de mon château maintenant !")
    print("Et n'oublie pas le chat !!! ")
    print("Oui " +nom+ ", il y avait un chat")
    print("Je parie que tu as donné les croquettes au dragon !")
else:
    print("Apparement " +nom+ ", tu ne sais pas ce qu'est un chiffre entre 1 et 4.")

