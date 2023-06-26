def ajouter_élève():
    id_élève = input("Entrez l'identifiant de l'élève : ")
    nom_élève = input("Entrez le nom de l'élève : ")
    élèves[id_élève] = nom_élève
    print("Élève ajouté avec succès !")

def modifier_élève():
    id_élève = input("Entrez l'identifiant de l'élève à modifier : ")
    if id_élève in élèves:
        nouveau_nom = input("Entrez le nouveau nom de l'élève : ")
        élèves[id_élève] = nouveau_nom
        print("Élève mis à jour avec succès !")
    else:
        print("L'élève n'existe pas.")

def supprimer_élève():
    id_élève = input("Entrez l'identifiant de l'élève à supprimer : ")
    if id_élève in élèves:
        del élèves[id_élève]
        print("Élève supprimé avec succès !")
    else:
        print("L'élève n'existe pas.")

élèves = {}
def afficher_tous_les_élèves():
    if élèves:
        print("Liste complète des élèves :")
        for id_élève, nom_élève in élèves.items():
            print(f"ID : {id_élève}, Nom : {nom_élève}")
    else:
        print("Aucun élève dans la liste.")

def gestion_eleves():
    print("Bienvenue dans la gestion des élèves !")
    while True:
        print("\nMenu :")
        print("1. Ajouter un élève")
        print("2. Modifier un élève")
        print("3. Supprimer un élève")
        print("4. Afficher la liste complète des élèves")
        print("5. Quitter")

        choix = input("Veuillez sélectionner une option (1-5) : ")

        if choix == "1":
            ajouter_élève()
        elif choix == "2":
            modifier_élève()
        elif choix == "3":
            supprimer_élève()
        elif choix == "4":
            afficher_tous_les_élèves()
        elif choix == "5":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    gestion_eleves()