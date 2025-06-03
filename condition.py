age = 10
age == 12 # '==' pose la question → est-ce que age est égal à 12 ?
print (age)


userAnswer = input("Aimes-tu les robots ? (oui/non/peut-être/que les robots minous)")
if userAnswer == "oui":
    print("Bip bip !")
elif userAnswer == "peut-être":
    print("humm, quel indécis !")
elif userAnswer == "que les robots minous":
    print("Meow ! Les robots minous sont les meilleurs !")
elif userAnswer == "non":
    print("les robots ne t'aiment pas non plus !")
else:
    print("Que dis-tu petit humain ?")
    