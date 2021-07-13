
def squared(x):
    x **= 2
    return x


x = [3, 2, 4, 5]
print(list(map(squared, x)))
