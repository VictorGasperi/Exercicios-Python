#n, m = map(int, input().split())
#frase = input().replace(" ", "")
#contfrase = 0
#tabela = [[0]*m]*n
#print(tabela[0][0])

#print(frase)

#print(frase[contfrase])
#for i in range(n):
#    for j in range(m):
#        tabela[i][j] = frase[contfrase]
#        contfrase += 1
#bug: ta inserindo as letras em todas as listas internas da tabela

import itertools as it

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
frase = input("Digite a frase: ").replace(" ", "")
primos = [2, 3, 5, 7, 11, 13, 17, 19]

def MontaMatriz(s):
    decomposicao = []
    tamanho = len(s)
    for number in primos:
        while (tamanho % number == 0):
            decomposicao.append(number)
            tamanho /= number
    if len(decomposicao) > 2:
        possiveismult = it.combinations(decomposicao)
        mult = list(map(lambda x, y: x * y, possiveismult))
        print(mult)

def transpor(m):
    t = []
    for i in range(len(m[0])): # i == colunas
        aux = []
        for j in range(len(m)): # j == linhas
            aux.append(m[j][i])
        t.append(aux)
    return t

def exibeMatrizemLinha(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")

m = []
k = 0
for j in range(linhas):
    aux = []
    for i in range(colunas):
        aux.append(frase[k])
        k += 1
    m.append(aux)

t = transpor(m)
exibeMatrizemLinha(t)

# pensar numa maneira de trazer a funcao montamatriz para esse script e realizar todas as possiveis montagens de matrizes
# exibindo os resultados linha a linha