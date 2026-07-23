import json 
import os
from datetime import datetime
from creer_profil import initialiser_utilisateur


def creer_seance(nom_utilisateur, fichier_profil):
    
    exo_autorises = ["traction", "dips", "muscle-up"]
    date_jour = datetime.now().strftime("%d/%m/%y")
    
    print(f"\n=== SAISIE DE LA SEANCE DU {date_jour} ===")

    # 1. OBJECTIFS
    obj1 = input("Quel est l'objectif de la séance (Force/Volume/PDC) ? ").strip().lower()
    obj2 = input("Autre objectif (ou taper 'aucun') ? ").strip().lower()
    
    objectifs = [obj1]
    if obj2 != "aucun" and obj2 != "":
        objectifs.append(obj2)

    # 2. EXERCICES RÉALISÉS
    exercices_saisis = input("\nQuels exercices sont réalisés aujourd'hui ? ").strip().lower()
    
    exercices_valides = []
    for e in exo_autorises:
        if e in exercices_saisis:
            exercices_valides.append(e)

    # 3. SAISIE DES SÉRIES (Stockées dans une liste de dictionnaires)
    series = []
    
    while True:
        print("\n--- SAISIE D'UNE SERIE ---")
        ex = input("Exercice (Traction / Dips / MU) : ").strip().capitalize()
        methode = input("Méthode d'intensification (Classique / Cluster / EMOM) : ").strip().capitalize()
        commentaire = input("Entrer un commentaire sur la séance : ")
        
        # Astuce : conversion directe des nombres
        charge = float(input("Charge leste (kg) : ").strip() or 0.0)
        reps = int(input("Répétitions : ").strip() or 0)
        rpe = float(input("RPE (ex: 8.5) : ").strip() or 0.0)

        # On crée l'objet "série" et on l'ajoute à notre liste de la séance
        une_serie = {
            "exercice": ex,
            "methode": methode,
            "charge_kg": charge,
            "repetitions": reps,
            "rpe": rpe
        }
        series.append(une_serie)

        choix = input("\nAjouter une autre série ? (1: OUI / 2: NON) : ").strip()
        if choix == "2" or choix.lower() == "non":
            break

    # 4. CRÉATION DU DICTIONNAIRE COMPLET DE LA SÉANCE
    donnees_seance = {
        "date": date_jour,
        "objectifs": objectifs,
        "exercices_prevus": exercices_valides,
        "commentaire" : commentaire,
        "series": series
    }

    # 5. SAUVEGARDE DANS LE FICHIER JSON DU PROFIL
    sauvegarder_seance_json(fichier_profil, donnees_seance)

    return donnees_seance


def sauvegarder_seance_json(fichier_profil, donnees_seance):
    """Lit le fichier JSON du joueur, ajoute la nouvelle séance et réécrit tout."""
    
    # 1. On lit le fichier JSON existant
    with open(fichier_profil, "r", encoding="utf-8") as f:
        profil = json.load(f)

    # 2. Si la clé 'historique_seances' n'existe pas encore dans le profil, on la crée
    if "historique_seances" not in profil:
        profil["historique_seances"] = []

    # 3. On ajoute notre séance tout à la fin de la liste
    profil["historique_seances"].append(donnees_seance)

    # 4. On réécrit le fichier JSON mis à jour
    with open(fichier_profil, "w", encoding="utf-8") as f:
        json.dump(profil, f, indent=4, ensure_ascii=False)

    print(f"\n✅ Séance enregistrée avec succès dans {fichier_profil} !")


nom, fichier = initialiser_utilisateur()
creer_seance(nom, fichier)