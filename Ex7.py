def decisionMaking(Z):
    positive = list(map(lambda n: n, filter(lambda n: n > 0, Z)))
    negative = list(map (lambda n: n, filter(lambda n: n < 0, Z)))
    neutral = list(map (lambda n: n, filter(lambda n: n == 0, Z)))
    return {'positive': positive, 'negative': negative, 'neutral': neutral}
n = [1, -2, 0, 3, -5, 0]
s = decisionMaking(n)
print(s)