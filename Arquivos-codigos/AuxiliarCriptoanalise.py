n, m = map(int, input().split())
frase = input().replace(" ", "")
contfrase = 0
tabela = [[0]*m]*n
print(tabela[0][0])

print(frase)

print(frase[contfrase])
for i in range(n):
    for j in range(m):
        tabela[i][j] = frase[contfrase]
        contfrase += 1
#bug: ta inserindo as letras em todas as listas internas da tabela

