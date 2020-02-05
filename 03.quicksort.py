def quicksort(items,low,high):
    #base case
    if(low>=high):
        return
    #use quick sort and arrange them / recursion
    #find the pivot
    p = pivot(items,low,high)
    #left of pivot
    quicksort(items,low,p-1)
    #right of pivot
    quicksort(items,p+1,high)
    return items

def pivot(items,low,high):
    p = high
    i = low
    while(i<p):
        if(items[i]>=items[p]):
            temp = items[i]
            items[i] = items[p-1]
            items[p-1] = items[p]
            items[p] = temp
            p = p-1
        else:
            i = i+1
    return p

items = [11,5,3,6,10,2]
print(quicksort(items,0,len(items)-1))