from collections import Counter as c

def main():
    s = input()
    counter = c(sorted(s))
    sorted_counter = counter.most_common()
    for i in range(3):
        print("%s %i" %(sorted_counter[i][0], sorted_counter[i][1]))

    """ char_list = []
    rep_list = [0]
    s = "".join(sorted(input()))
    print(s)
    counter = c(s)
    for char in s:
        if counter[char] > rep_list[0]:
            rep_list[0] = counter[char]
            char_list[0] = char
        if counter[char] == rep_list[0]:
            char_list.append(char)
            rep_list.append(counter[char])

    print("%s %i" %(char_list[0], rep_list[0])) """

main()