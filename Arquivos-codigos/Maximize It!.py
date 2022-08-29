from itertools import product as p

def main():
    arr = []
    arr_results = []
    k, m = map(int, input().split())
    # recebendo os valores de k, referente a quantas listas serao; e m, referente ao calculo do mod
    for _ in range(k):
        arr.append(list(map(int, input().split()))[1:])
        # adicionando na lista arr as sublistas adicionadas pelo input(), partindo do index 1
    arr = list(p(*arr))
    # achando o produto cartesiano das sublistas. eh importante relembrar o papel do "*", que funciona como uma "chave"
    # para abrir a nasted list e acessar as sublistas. Assim ele cria diversas combinacoes com os numeros das listas 
    # passadas.
    for tup in arr:
        # para cada tupla na lista com os produtos cartesianos
        sum = 0
        for item in tup:
            # para cada numero presente nas tuplas presentes na lista com os produtos cartesianos
            sum += item**2
            # adiciona ao sum, que inicialmente eh zero, o quadrado do item
        arr_results.append(sum % m)
        # aqui ele cria uma lista com todos os valores ja encontrados, apos realizar o calculo do quociente da divisao
        # inteira
    print(max(arr_results))
    # aqui ele simplesmente usa o metodo print no maior valor encontrado dentro da lista com todos os valores possiveis
    # do mod
main()
