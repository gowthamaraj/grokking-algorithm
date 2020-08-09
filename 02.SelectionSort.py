def small(items):
    small = items[0]
    index = 0
    for i in range(1,len(items)):
        if items[i]<small:
            index = i
            small = items[i]
    return index

def selectionSort(items):
    output = []
    for i in range(len(items)):
        output.append(items.pop(small(items)))
    return output

print(selectionSort([5,3,6,2,10]))