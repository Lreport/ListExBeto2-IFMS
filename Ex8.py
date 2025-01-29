from functools import reduce

def wordSum(text):
    return reduce(lambda x, y: x + y, map(len, text))

words = ['casa', 'python', 'lambda']
#s = wordSum(words)
print(wordSum(words))