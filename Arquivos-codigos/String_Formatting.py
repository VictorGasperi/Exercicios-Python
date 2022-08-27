decimal = [x for x in range((int(input())) + 1) if x != 0]
octal = list(map(lambda x: format(x, 'o'), decimal))
hexadecimal = list(map(lambda x: format(x, 'X'), decimal))
binario = list(map(lambda x: format(x, 'b'), decimal))

print()
