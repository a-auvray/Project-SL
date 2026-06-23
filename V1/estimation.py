# 1. On définit la fonction (la boite à calcul) et on renvoie M à l'extérieur 
def calculer_1RM(C, R, E, P) :

    if 6 > E > 10 :
        print("Le RPE doit etre compris en 6 et 10 ")
        return 0.0

    else :
        M = (C + P) * (1 + (R + (10 - E)) / 32.5) - P

        M = M.__round__(3)

        M = int(M / 0.25) * 0.25

    return M 

#2. On demande à l'uilisateur de rentrer ses données 
C = float(input("Entrer la charge de travail : "))

R = int(input("Entrer le nombre de répétitions effecutées : "))

while True :
    E = float(input("Entrer le RPE : "))
    if 6 <= E <= 10 : 
        break
    else :
        print("Erreur ! Veuillez entrer un RPE compris entre 6 et 10 ")


P = float(input("Entrer votre poids de corps actuel : "))

#3. On utilise la fonction, on arrondit la valeur et on affiche le résulat
M = calculer_1RM(C, R, E, P)

print(f"Votre 1RM estimée est {M}")
