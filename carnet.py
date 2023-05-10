

carnet = [
    {
        "nom": "Florian",
        "numero": 678394839,
    },
    {
        "nom": "Fabien",
        "numero": 847384777,
    },
    {
        "nom": "test",
        "numero": 987654321,
    },
    {
        "nom": "Hello",
        "numero": 0000
    }
]


def fin():
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Tapez 1 pour continuer")
    print("Tapez 2 pour quitter")
    choix = int(input("Quel est votre choix ?"))

    match choix:
        case 1:
            interface()
        case 2:
            print("Fin du programme...")


def ajouter_contact():
    nom = input("Taper le nom du contact: ")
    numero = int(input("Taper le numero du contact: "))
    carnet.append([{"nom": nom, "numero": numero}])
    print("-------------------------------------------------------------------")
    print("Votre contact a bien été ajouté a la liste")
    print(carnet)
    fin()


def supprimer():
    print("----------------------------------------------------------------")
    nom = input("Taper le nom du contact que vous souhaitez supprimer ")
    for i in carnet:
        if i["nom"].lower() == nom.lower():
            carnet.remove(i)
            print("-------------------------------------------------------------------")
            print(f"{nom} à été supprimé")
            print(carnet)


def rechercher_nom():

    print("-------------------------------------")
    print("Tapez 1 pour rechercher un numéro de téléphone à partir d'un nom")
    print("Tapez 2 pour rechercher un nom à partir d'un numéro de téléphone")
    print("-------------------------------------")

    choix = int(input("Quel est votre choix?"))

    match choix:

        case 1:

            nom = input("Entrer le nom ")
            for i in carnet:
                if i["nom"].lower() == nom.lower():
                    numero = i["numero"]
                    print(
                        "-------------------------------------------------------------------")
                    print(f"Le numéro de téléphone de {nom} est {numero}")

        case 2:

            telephone = int(input("Entrer le numéro de téléphone "))
            for i in carnet:
                if i["numero"] == telephone:
                    nom = i["nom"]
                    print(
                        "-------------------------------------------------------------------")
                    print(
                        f"la personne que vous rechercher avec le numero {telephone} est {nom}")


def afficher():
    print(carnet)
    fin()


def modifier():
    print("Tapez 1 pour modifier un nom")
    print("Taper 2 pour modifier un numero")
    choix = int(input("Quel est votre choix? "))
    match choix:
        case 1:

            nom = input("Tapez le nom que vous voulez modifier: ")

            for i in carnet:
                if nom.lower() == i["nom"].lower():
                    nouveauNom = input("Taper le nouveau nom ")
                    i["nom"] = nouveauNom
                    print(
                        "-------------------------------------------------------------------")
                    print(carnet)

        case 2:

            telephone = int(input(
                "Entrez le numéro de téléphone que vous souhaitez modifier: "))

            for i in carnet:
                if telephone == i["numero"]:
                    nouveauNumero = int(input(
                        "Entrez le nouveau numéro de téléphone "))
                    i["numero"] = nouveauNumero
                    print(
                        "-------------------------------------------------------------------")
                    print(carnet)


# ajouter_contact(nom1, numero1)

def interface():
    print("----------------------------------------------------------------")
    print("------------------------------Taper 1 pour ajouter des contacts------------------------------")
    print("-----------------------------Tapez 2 pour supprimer des contacts------------------------------")
    print("-----------------------------Tapez 3 pour rechercher des contacts------------------------------")
    print("----------------------------Taper 4 pour afficher tous les contacts------------------------------")
    print("------------------------------Tapez 5 pour modifier des contacts")
    print("------------------------------Taper 6 pour quitter le programme------------------------------")
    print("----------------------------------------------------------------")

    try:
        choix = int(input("Quel est votre choix ? "))

        match choix:
            case 1:
                ajouter_contact()

            case 2:
                supprimer()

            case 3:
                rechercher_nom()

            case 4:
                afficher()

            case 5:
                modifier()

            case 6:
                fin()

    except ValueError:
        interface()


interface()
