def decisionMaking(num):
    pair = list(filter(lambda n: n % 2 == 0, num))
    odd = list(filter(lambda n: n % 2 != 0, num))
    return {'pair': pair, 'odd': odd}
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = decisionMaking(n)
print(s)