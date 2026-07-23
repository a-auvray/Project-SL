def calculer_1RM(C, R, E, P):
    # Sécurité RPE
    if not (6 <= E <= 10):
        print("Le RPE doit être compris entre 6 et 10.")
        return 0.0

    # 1. Calcul du poids total du système (Lest + Poids de corps)
    poids_total_deplace = C + P

    # 2. Répétitions "virtuelles" (Reps réalisées + RIR restant)
    reps_virtuelles = R + (10 - E)

    # 3. Formule d'Epley appliquée au système global
    systeme_1RM = poids_total_deplace * (1 + (reps_virtuelles / 30))

    # 4. On extrait le lest pur en retirant le poids de corps
    lest_max_estime = systeme_1RM - P

    # Sécurité si le résultat calculé est négatif (ex: travail léger au PDC)
    if lest_max_estime < 0:
        lest_max_estime = 0.0

    # Arrondi au 0.25 kg près
    return round(lest_max_estime * 4) / 4 


def entrer_donnees():
    print("=== CALCULATEUR DE 1RM EN STREET LIFTING ===")
    
    # Sécurisation des inputs contre les erreurs de frappe (lettres au lieu de chiffres)
    try:
        C = float(input("Entrer la charge de travail (lest en kg) : ").strip() or 0.0)
        R = int(input("Entrer le nombre de répétitions effectuées : ").strip() or 0)
        
        while True:
            E = float(input("Entrer le RPE (6 à 10) : ").strip())
            if 6 <= E <= 10: 
                break
            print("❌ Erreur ! Veuillez entrer un RPE compris entre 6 et 10.")

        P = float(input("Entrer votre poids de corps actuel (en kg) : ").strip())

        # Calcul et affichage
        M = calculer_1RM(C, R, E, P)
        print(f"\n🔥 Votre lest max estimé (1RM) est de : {M} kg")
        return M

    except ValueError:
        print("❌ Saisie invalide ! Veuillez n'entrer que des chiffres.")
        return 0.0