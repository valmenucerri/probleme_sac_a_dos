def calcul_rapport(objets):
    rapport = {}
    for id,objet in objets.items():
        valeur = objet[1]
        poids = objet[0]
        rap = valeur // poids
        rapport[id] = rap
    return rapport

def trier_rapport(rapport):
    '''
    Ranger le dico des rapports dans l'ordre décroissant des rapports
    :param rapport: le dico des rapports valeur/poids. type : dict
    :return: rap_trie: les objets dans l'ordre décroissant des rapports . type : list
    '''
    rap_trie = []
    for id, rap in sorted(rapport.items(), key=lambda x: x[1],reverse=True):
        rap_trie.append(id)

    return rap_trie


def remplir_sac(scenar,carac):
    '''
    Remplir le sac avec une valeur maximale d'objet, tout en restant en dessous du poids limite
    :param scenar:
    :param carac:
    :return:
    '''
    rapport = calcul_rapport(scenar)
    rap_trie = trier_rapport(rapport)
    pd_max = carac[0]
    valeur = 0
    poidscourant = 0
    indice = 0
    nb_objet = 0
    objets_ajoutes = []
    continu = True
    while continu:
        poids_a_ajouter = scenar[rap_trie[indice]][0]
        if poids_a_ajouter + poidscourant > pd_max:
            continu = False
        else:
            valeur_a_ajouter = scenar[rap_trie[indice]][1]
            valeur += valeur_a_ajouter
            poidscourant += poids_a_ajouter
            objets_ajoutes.append(rap_trie[indice])
            nb_objet += 1
            indice += 1




    return nb_objet, objets_ajoutes, valeur, poidscourant