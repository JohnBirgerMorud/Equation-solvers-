import numpy as np

# Setter verdi null før enerne:
def null(matrise):
    for i in range(1,len(matrise)):
        for j in range((i)):
            z = j
            while matrise[i][j] != 0:
                if matrise[z][j] != 0:
                    matrise[i] = matrise[z] - (matrise[z][j] / matrise[i][j]) * matrise[i]
                else:
                    z -= 1

                if abs(z-j) > len(matrise[i]):
                    print("Hello")
                    break
    return matrise


# Setter verdi 1 på rett plass

def ener(matrise):
    for i in range(len(matrise)):
        for j in range(len(matrise[i])):
            if matrise[i][i] != 1 and matrise[i][i] != 0:
                matrise[i] /= matrise[i][i]

    return matrise


# Løse matrisen: 
def los_matrise(matrise):
    for i in range(1, len(matrise)):
        los = matrise[-i][-1]
        
        for j in range((len(matrise)-i)):
            matrise[j][-1-i] *= los
            matrise[j][-1] -= matrise[j][-1-i]
            matrise[j][-1-i] -= matrise[j][-1-i]

    return matrise


# Flytte rader med bare null nederst i tabellen
def null_nederst(matrise):
    for i in range(len(matrise)):
        if all(val == 0 for val in matrise[i]):
            q = matrise[i].copy()

            if i+1 < len(matrise):
                if not all(val == 0 for val in matrise[i+1]):
                    matrise[i] = matrise[i+1]
                    matrise[i+1] = q
    return matrise



# avrunding:
def round_matrise(matrise): 
    svar = []
    for i in range(len(matrise)):
        for j in range(len(matrise[i])):
            matrise[i][j] = round(matrise[i][j], 4)
        svar.append(matrise[i][-1])

    return matrise, svar

### SELVE FUNKSJONEN

def gaus_matrise(matrise):
    matrise = null(matrise)
    matrise = ener(matrise)
    matrise = los_matrise(matrise)
    matrise = null_nederst(matrise)
    matrise, svar = round_matrise(matrise)
    
    return matrise, svar


### MATRISEN

a = [
    
    [1, 2, 2, 2],
    [2, 6, -2, 7],
    [2, -3, 6, 3]

]

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = float(a[i][j])

A = np.array(a)

matrise, svar = gaus_matrise(A)

print('\n',matrise)
print(f"\nLøsninger er: {svar} \n")
