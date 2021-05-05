def recup_sac(commande):
    fichier = commande[-1]
    return fichier



def caracteristique(sac):
    carac = []
    with open("exemple_sac/"+sac,'r') as f :
        for ligne in f:
            ligne1 = ligne.split()
            valeur = int(ligne1[-1])
            carac.append(valeur)
            if len(carac) == 2:
                break


    return carac

def detail_objet(fichier):
    scenar = {}
    id = 1
    with open("exemple_sac/" + fichier, 'r') as f:
        for ligne in f:
            ligne1 = ligne.split()
            if len(ligne1) == 2 :
                scenar["objet{}".format(id)] = [int(ligne1[0]),int(ligne1[1])]
                id += 1

    return scenar