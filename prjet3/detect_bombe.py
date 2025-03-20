def detect_bombe(mat):
    case = 0
    nbrb = 0
    for x in range(len(mat)):
        for y in range(len(mat[x]):
            case = mat[x][y]
            if mat[x-1][y-1]['bombe'] == True :
                nbrb = nbrb +1
            if mat[x-1][y]['bombe'] == True :
                nbrb = nbrb +1
            if mat[x-1][y+1]['bombe'] == True :
                nbrb = nbrb +1
            if mat[x][y-1]['bombe'] == True :
                nbrb = nbrb +1
            if mat[x][y+1]['bombe'] == True :
                nbrb = nbrb +1
            if mat[x+1][y-1]['bombe'] == True :
                nbrb = nbrb +1
            if mat[x+1][y]['bombe'] == True :
                nbrb = nbrb +1
            if mat[x+1][y+1]['bombe'] == True :
                nbrb = nbrb +1
            case['bombe_near']= nbrb