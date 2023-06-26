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