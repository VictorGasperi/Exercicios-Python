n = int(input())
arr = list(map(int, input().split()))
def average(array):
    avr = ((sum(set(array)))/ len(set(array)))
    return "%.2f" %avr

result = average(arr)
print(result)