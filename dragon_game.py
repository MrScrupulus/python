print("Tu te trouves dans une pièce obscure d'un mystérieux château.")
print("Tu dois choisir entre 3 portes pour continuer ton aventure.")

gamerChoice = input("Choisis 1,2 ou 3...")

if gamerChoice == "1":
    print("Tu te retrouves face à un dragon endormi, ton haleine fetide le réveille !")
    print("Tu es mort ! Brosse-toi les dents la prochaine fois !")
elif gamerChoice == "2":
    print("Derrière la porte se trouve la queue d'un dragon.")
    print("Ne le réveille pas en lui tripotant !")
    print("Ferme la porte et retente tachance (c'est la 3, si tu es un peu neuneu)")
elif gamerChoice == "3":
    print("Tu as trouvé un sac de croquette !")
    print("Bravo, si on veut... tu peux toujours essayer de les donner au dragon !")
else:
    print("Apparement tu ne sais pas ce qu'est un chiffre entre 1 et 3.")

