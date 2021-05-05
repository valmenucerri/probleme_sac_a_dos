import remplir_sac.traiter_sac as ts
import sys

if "__main__" == __name__:
    sac = ts.recup_sac(sys.argv)
    print(ts.caracteristique(sac))
