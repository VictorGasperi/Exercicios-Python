n = input().split(" ")
ar = input().split(" ")
a = set(input().split(" "))
b = set(input().split(" "))
happ = sum((i in a) - (i in b) for i in ar)
print(happ)
# o filter compara se os itens de a ou b sao iguais aos de ar ?
