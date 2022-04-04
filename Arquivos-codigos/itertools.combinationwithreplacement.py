from itertools import combinations_with_replacement
s, n = input().split(" ")
n = int(n)
s = str(s)

l = list(combinations_with_replacement(sorted(s), n))

tuplas = [''.join(i) for i in l]
for i in range(len(l)):
    print(tuplas[i])
