from functools import reduce

def weightAverage(st):
    def meansCalculat(nw):
        notes = nw[:-1]
        weight = nw[-1]
        sum = reduce(lambda x, y: x + y, notes) 
        return sum / len(notes)

    return {name: meansCalculat(nw) for name, nw in st.items()}

studens = {
    'João': [8, 7, 9, 2], #notas 8, 7, 9, peso 2
    'Ana': [5, 6, 7, 3] #notas 5, 6, 7, peso 3
}

print(weightAverage(studens))