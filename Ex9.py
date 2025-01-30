def filterTuples(tuplas):
    means = list(map(lambda x: sum(x) // len(x), tuplas))
    filtredTred = list(filter(lambda x: x > 5, means))
    return filtredTred
def filterTuples1(tuplas):
    return list(filter(lambda x: sum(x) // len(x) > 5, tuplas))
n = [(8, 8), (5, 6, 7), (1, 2)]
print('Média maiores que 5: ', filterTuples(n))
print('Quais são maiores que 5: ', filterTuples1(n))