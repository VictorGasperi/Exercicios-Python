s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
# funcao any() retorna um booleano True se caso dentro de um iteravel existe
# um unico True; se nao houver, retorna False
