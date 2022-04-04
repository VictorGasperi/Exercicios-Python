n = int(input())

nl = [[input(), float(input())] for _ in range(n)]

mv = sorted(set(list((nl[i][1]) for i in range(n))))

lg = mv[1]

an = []

for i in range(n):
    if (lg == nl[i][1]):
        an.append(nl[i][0])
an.sort()        
for i in range(len(an)):
    print(an[i])

