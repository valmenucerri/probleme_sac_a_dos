'''
Générer un sac avec un nombre d'objet voulu, les valeurs et poids des objets sont pris aléatoirement
'''
import sys
import random as r

N = int(sys.argv[-1])
poids_max = 2*N
objet_poids = [r.randint(1,N) for i in range (N)]
objet_valeur = [r.randint(1,N**2) for _ in range(N)]

with open("exemple_sac/sac{}_objets{}.txt".format(poids_max,N),'w') as fichier:
    fichier.write("poids max = "+str(poids_max)+"\n")
    fichier.write("nombre d'objets = "+str(N)+"\n")
    for i in range(N):
        fichier.write(str(objet_poids[i])+" "+ str(objet_valeur[i])+"\n")

