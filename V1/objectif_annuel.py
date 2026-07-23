import json
import os
from programmation import creer_seance, sauvegarder_seance_json
from datetime import datetime



def objectif_annuel(fichier_profil, donnees_seance) :
    année = datetime.now().strftime("%y")
    print(f"=== Objectifs {année} ===")

    # with open(fichier_profil, "w", encoding="utf-8") as f :
        # json.dump(fichier_profil, )