n = int(input())
sm = {}
for _ in range(n):
    name, *line = input().split(" ")
    scr = list(map(float, line))
    sm[name] = scr
qn = input()
if qn in sm:
    x = (sm[qn][0] + sm[qn][1] + sm[qn][2])/ 3
    print("%.2f" %x)
