def crea_matrice(taille):
    tab = []
    mat = []
    a = 0
    dico = {}
    for i in range(taille+2): # +2 pour les bords que l'on ne vas pas compter dans les cases mais dont on a besoin
        tab = []
        for j in range (taille+2):
            dico = {}
            tab.append(dico)
        mat.append(tab)
    return mat