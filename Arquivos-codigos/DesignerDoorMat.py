n, m = map(int, input().split(" "))

p = [((".|." * (2 * i + 1)).join("")).center(n, "-") for i in range(m)]
x = int(((n - 1)/ 2) + 1)
p[x] = "WELCOME"
for i in range(n):
    print(p[i])
# nao esta terminado
