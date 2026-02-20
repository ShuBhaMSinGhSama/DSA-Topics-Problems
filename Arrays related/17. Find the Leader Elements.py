a=[3,4,5,2,10,5,6,9]
def find_leaders(a):
    n = len(a)
    leaders = []
    
    m = a[-1]
    leaders.append(m)
    
    for i in range(n-2, -1, -1):
        if a[i] > m:
            m = arr[i]
            leaders.append(a[i])
    
    return leaders[::-1]   

print(find_leaders(a))
