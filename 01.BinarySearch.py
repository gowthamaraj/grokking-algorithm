def bs(items,item):
    start = 0
    end = len(items)-1

    while(start<=end):
        mid = (start+end)//2
        guess = items[mid]
        if guess == item:
            return mid
        elif guess > item:
            end = mid-1
        else:
            start = mid+1
    return -1

items = [1,3]
inp = int(input())
print(bs(items,inp)+1)