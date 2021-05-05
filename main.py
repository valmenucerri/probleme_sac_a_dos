from remplir_sac import traiter_sac as ts, remplissage as r
import sys

if "__main__" == __name__:
    sac = ts.recup_sac(sys.argv)
    carac = ts.caracteristique(sac)
    scenar = ts.detail_objet(sac)
    r.remplir_sac(scenar,carac)
