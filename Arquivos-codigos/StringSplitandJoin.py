s = input()
def splitandjoin(s):
    s = s.split(" ")
    s = "-".join(s)
    return s
print(splitandjoin(s))