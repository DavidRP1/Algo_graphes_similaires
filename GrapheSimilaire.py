# David Raby-Pepin (p0918119)

# Description: Algorithme qui indique si deux matrices d'adjacence symetriques A et B de taille m par m representent
#              le meme graphe non oriente.

# fonction qui indique si les matrices d'adjacence symetriques A et B representent le meme graphe non oriente
def grapheSimilaire(A, B, v):
    egalite = False     # indique si les matrices representent le meme graphe
    index = len(v)      # index representant la ligne de la matrice A observee ainsi que la longueur de v
    m = len(A)          # nombre de lignes dans la matrice A

    # si v est de longueur m, alors A et B representent le meme graphe
    if index == m:
        return True

    # observer chaque ligne de B
    for i in range(m):
        # si on trouve une ligne de B contenant le meme nombre de 1 que la ligne de A observee, que l'element
        # A[index][index] esl le meme que B[i][i], et que i n'est pas encore place dans le vecteur v, alors on a
        # trouve un i qui peut potentiellement donne une solution
        if A[index].count(1) == B[i].count(1) and A[index][index] == B[i][i] and i not in v:
            k = 0
            fonctionne = True

            # verifier si les permutations dans v fonctionnent tous avec la ligne de B observee
            for j in v:
                if A[index][k] != B[i][j]:
                    fonctionne = False
                k = k+1

            # si c'est le cas, on ajoute i au vecteur v et on rappelle la fonction avec un vecteur de taille augmentee
            if fonctionne:
                w = v.copy()
                w.append(i)
                egalite = grapheSimilaire(A, B, w)  # si l'algo reussit a trouver une solution, alors egalite sera True
                if(egalite):
                    return egalite
    return egalite


A = [[0,1,1,1],
     [1,0,0,1],
     [1,0,0,0],
     [1,1,0,0]]

B = [[0,1,1,0],
     [1,0,1,0],
     [1,1,0,1],
     [0,0,1,0]]

v = []

C = [[0,1,0,1,0,0],
     [1,0,0,1,0,1],
     [0,0,0,1,1,1],
     [1,1,1,0,1,0],
     [0,0,1,1,0,0],
     [0,1,1,0,0,0]]

D = [[0,1,1,0,1,1],
     [1,0,0,1,1,0],
     [1,0,0,1,0,1],
     [0,1,1,0,0,0],
     [1,1,0,0,0,0],
     [1,0,1,0,0,0]]

print(grapheSimilaire(C, D, v))
