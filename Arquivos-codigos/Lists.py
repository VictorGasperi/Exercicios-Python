l = []
n = int(input())
for i in range(n):
    all = input().split(" ")
    cmd = all[0]
    num = all[1:]
    if cmd != "print":
        cmd += "(" + ",".join(num) + ")"
        eval("l."+cmd)
    else:
        print(list(l))

