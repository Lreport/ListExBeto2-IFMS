def namePlus5(nameList):
    return list(filter(lambda name: len(name) > 5, nameList))

name = ['Messi', 'Ronaldo', 'Gabriel', 'Ovo', 'João']
print(namePlus5(name))