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

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
frase = input("Digite a frase: ").replace(" ", "")

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
