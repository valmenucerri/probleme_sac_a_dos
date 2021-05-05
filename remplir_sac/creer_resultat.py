def resul(nb_objet, objets_ajoutes, valeur, poidscourant,pd_max,nbr_obj):
    '''
    Créer le fichier résultat
    :param nb_objet: le nombre d'objets ajoutés. type : int
    :param objets_ajoutes: la liste des objets ajoutés . type : list
    :param valeur: la valeur finale de tous les objets du sac réunis. type : int
    :param poidscourant: le poids actuel du sac, une fois rempli. type : int
    :param pd_max: le poids maximum que pouvait atteindre le sac. type : int
    :param nbr_obj: le nombre initial d'objets disponibles. type : int
    :return: None
    '''
    with open("Resultats/sac_capa_max{}_{}_objets.txt".format(pd_max,nbr_obj),'w') as f:
        f.write(str(nb_objet)+" objets sont entrés dans le sac"+"\n")
        f.write("Il s'agit des objets :")
        for obj in objets_ajoutes:
            f.write(obj+",")
        f.write("\n"+ "La valeur totale est de "+ str(valeur)+"\n")
        f.write("Le poids final du sac est de "+str(poidscourant)+". " + "C'est "+str(pd_max - poidscourant)+" unités en dessous du poids maximum")
