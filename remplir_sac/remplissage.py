import remplir_sac.creer_resultat as cr


def calcul_rapport_vp(objets):
    '''
    calculer le rapport valeur/poids de chaque objet
    :param objets: les caractéristiques valeur et poids de tous les objets. type : dict
    :return: rapport: les objets associés à leur rapport respectif valeur/poids. type : dict
    '''
    rapport = {}
    for id,objet in objets.items():
        valeur = objet[1]
        poids = objet[0]
        rap = valeur // poids
        rapport[id] = rap
    return rapport

def trier_rapport_vp(rapport):
    '''
    Ranger le dico des rapports dans l'ordre décroissant des rapports
    :param rapport: le dico des rapports valeur/poids. type : dict
    :return: rap_trie: les objets dans l'ordre décroissant des rapports . type : list
    '''
    rap_trie = []
    for id, rap in sorted(rapport.items(), key=lambda x: x[1],reverse=True):
        rap_trie.append(id)

    return rap_trie

def calcul_rapport_pv(objets):
    '''
    calculer le rapport poids/valeur de chaque objet
    :param objets: les caractéristiques valeur et poids de tous les objets. type : dict
    :return: rapport: les objets associés à leur rapport respectif poids/valeur. type : dict
    '''
    rapport = {}
    for id,objet in objets.items():
        valeur = objet[1]
        poids = objet[0]
        rap = poids / valeur
        rapport[id] = rap
    return rapport

def trier_rapport_pv(rapport):
    '''
    Ranger le dico des rapports dans l'ordre décroissant des rapports poids valeur
    :param rapport: le dico des rapports poids/valeur. type : dict
    :return: rap_trie: les objets dans l'ordre décroissant des rapports . type : list
    '''
    rap_trie = []
    for id, rap in sorted(rapport.items(), key=lambda x: x[1]):
        rap_trie.append(id)

    return rap_trie



def remplir_sac(scenar,carac):
    '''
    Remplir le sac avec une valeur maximale d'objet, tout en restant en dessous du poids limite
    :param scenar:
    :param carac:
    :return:
    '''
    rapport = calcul_rapport_pv(scenar)
    rap_trie = trier_rapport_pv(rapport)
    pd_max = carac[0]
    valeur = 0  #initialiser le compteur de valeur ajoutée dans le sac
    poidscourant = 0 #garder en mémoire le poids du sac pour savoir quand arrêter le remplissage
    indice = 0
    nb_objet = 0
    objets_ajoutes = []
    continu = True
    while continu:
        poids_a_ajouter = scenar[rap_trie[indice]][0]
        if poids_a_ajouter + poidscourant > pd_max:
            continu = False #arrêter le remplissage si le poids suivant dépasse le poids courant
        else:
            valeur_a_ajouter = scenar[rap_trie[indice]][1]
            valeur += valeur_a_ajouter
            poidscourant += poids_a_ajouter
            objets_ajoutes.append(rap_trie[indice])
            nb_objet += 1
            indice += 1




    cr.resul(nb_objet, objets_ajoutes, valeur, poidscourant,pd_max,carac[1])