def calcul_rapport(objets):
    rapport = {}
    for id,objet in objets.items():
        valeur = objet[1]
        poids = objet[0]
        rap = valeur // poids
        rapport[id] = rap
    return rapport

def trier_rapport(rapport):
    rap_trie = {}
    for id, rap in sorted(rapport.items(), key=lambda x: x[1],reverse=True):
        rap_trie[id] = rap

    return rap_trie


