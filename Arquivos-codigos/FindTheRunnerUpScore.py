n = int(input())
l = sorted(list(map(int, input().split())))
n1 = len(l) - len(set(l))
print(l[(n- n1) - 2])
