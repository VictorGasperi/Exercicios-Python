string = input()
def swap_case(s):
    l = ""
    for i in s:
        if i == i.upper():
            l += i.lower()
        else:
            l += i.upper()
    return l
print(swap_case(string))

