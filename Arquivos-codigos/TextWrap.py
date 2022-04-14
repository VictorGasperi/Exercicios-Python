import textwrap

string, max_width = input(), int(input())

def wrap(s, mW):
    wordl = textwrap.wrap(s, mW) #cria uma lista de elementos do texto s de um tamanho width
    return "\n".join(wordl) # junta os elementos da lista wordl com um break line

result = wrap(string, max_width)   
print(result)