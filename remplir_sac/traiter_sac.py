def recup_sac(commande):
    '''
    R�cup�rer le nom du fichier repr�setant le sac
    :param commande: la ligne de commande. type : list
    :return: fichier: le nom du fichier. type : str
    '''
    fichier = commande[-1]
    return fichier



def caracteristique(sac):
    '''
    R�cup�rer les caract�ristiques principales du sac
    :param sac: le fichier repr�sentant le sac. type : str
    :return: carac: le poids max du sac et le nombe d'objets consid�r�. type : list
    '''
    carac = []
    with open("exemple_sac/"+sac,'r') as f :
        for ligne in f:
            ligne1 = ligne.split()
            valeur = int(ligne1[-1])
            carac.append(valeur)
            if len(carac) == 2: #consid�rer uniquement les deux premi�res lignes du fichier, puisqu'elles contiennent les informations voulues
                break


    return carac

def detail_objet(fichier):
    '''
    Repr�senter les caract�ristiques de chaque objet dans un dictionnaire
    :param fichier: le nom du fichier repr�sentant le sac. type : str
    :return: scenar. Les objets avec leur poids et leur valeur. type : dict
    '''
    scenar = {}
    id = 1
    with open("exemple_sac/" + fichier, 'r') as f:
        for ligne in f:
            ligne1 = ligne.split()
            if len(ligne1) == 2 :
                scenar["objet{}".format(id)] = [int(ligne1[0]),int(ligne1[1])]
                id += 1

    return scenar