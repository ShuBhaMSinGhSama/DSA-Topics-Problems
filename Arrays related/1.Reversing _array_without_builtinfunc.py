a=[3,5,2,6,7,5,8,1,4]

def reversing(a):
    i=0
    j=len(a)-1
    
    while i<j:
        a[i],a[j] = a[j],a[i]

        i+=1
        j-=1
    return(a)
print(reversing(a))
