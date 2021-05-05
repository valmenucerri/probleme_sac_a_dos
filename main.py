from remplir_sac import traiter_sac as ts, remplissage as r
import sys

if "__main__" == __name__:
    sac = ts.recup_sac(sys.argv)
    scenar = ts.detail_objet(sac)
    rap = r.calcul_rapport(scenar)
    rap_trie = r.trier_rapport(rap)
    print(rap)
    print(rap_trie)