from itertools import combinations

n = int(input())
l = list(input().split(" "))
k = int(input())
comb = list(combinations(l, k))
f = list(filter(lambda c: "a" in c, comb))

x = len(f)/ len(comb)
print("%.4f" %x)
