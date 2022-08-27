import itertools as it

frase = "ODLIPTDDEEEQVAMOELEOIANSPUEMEBOESDFDUIREEALRBIAAIENSOAARHARRRSCSCTVCCEOSAODAUEAEAHOLRISAESLLDDRARO"

primos = [2, 3, 5, 7, 11, 13, 17, 19]

def MontaMatriz(s):
    decomposicao = []
    auxiliar = []
    tamanho = len(s)
    for number in primos:
        while (tamanho % number == 0):
            decomposicao.append(number)
            tamanho /= number
    
    if len(decomposicao) > 2:
        possiveismult = list(it.combinations(decomposicao, 2))
        mult = list(map(lambda x: x[0] * x[1], possiveismult))
        auxiliar_reverso = list(reversed(decomposicao))
        auxiliar1_tamanhoMatriz = [(i, j) for i in mult for j in auxiliar_reverso if mult.index(i) == auxiliar_reverso.index(j)]
        auxiliar2_tamanhoMatriz = [(i, j) for i in auxiliar_reverso for j in mult if mult.index(j) == auxiliar_reverso.index(i)]
        auxiliar1_tamanhoMatriz += auxiliar2_tamanhoMatriz
        possiveisTamanhoMatriz = list(set([i for i in auxiliar1_tamanhoMatriz]))
        
        return possiveisTamanhoMatriz
    else:
        return decomposicao
        
MontaMatriz(frase)