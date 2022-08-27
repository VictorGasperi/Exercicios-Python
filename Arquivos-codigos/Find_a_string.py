string = input()
substring = input()

def count_substring(string, substring):
    """
    Recebe os parametros e converte para uppercase
    O contador comeca com zero
    para i no tamanho da string
    se a string no index i ate o final dessa (end como padrao vai ate o final da string) comecar com a substring
    entao adicionar um no contador
    retornar o contador
    
    """
    string.upper()
    substring.upper()
    contador = 0
    for i in range(len(string)):
        if string[i:].startswith(substring): 
            contador += 1
    return contador
count_substring(string, substring)

# pesquisar sobre substrings --> string[start:end:step]
# padroes: start = 0; end = length of string; step = 1 