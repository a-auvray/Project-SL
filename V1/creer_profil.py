import json 
import os
from datetime import datetime




# On identifie l'utilisateur qui se connecte 
def initialiser_utilisateur() :

    print("=== CONNEXION AU JOURNAL ===")
    nom_utilisateur = input("Qui etes-vous ? ").strip().capitalize()

    fichier_profil = f"profil_{nom_utilisateur}.json"


# Si c'est sa première connexion, on crée une nouvelle sauvegarde pour ses données 
    if not os.path.exists(fichier_profil) :
            profil_default = { 
            "nom" : nom_utilisateur,
            "records" : {
                "tractions" : 0.0,
                "dips" : 0.0,
                "muscle-up" : 0.0
            }
        }
            
    with open(fichier_profil, "w", encoding="utf-8") as f:
            json.dump(profil_default, f, indent=4)
    print(f"Nouveau profil créé pour {nom_utilisateur}")

    return nom_utilisateur, fichier_profil