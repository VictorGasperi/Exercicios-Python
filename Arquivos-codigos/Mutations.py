string = input()
value, char = input().split(" ")
value = int(value)
char = str(char)
def mutate_string(s, v, c):
    s = list(s)
    s[v] = c
    s = "".join(s)
    return s
print(mutate_string(string, value, char))