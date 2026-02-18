a=[3,5,2,6,7,5,8,1,4]
#print(max(a) , min(a))
def Exta(a):
    Max_val = a[0]
    Min_val = a[0]

    for num in a:
        if Max_val<num:
            Max_val = num
        elif Min_val>num:
            Min_val =num
    return(Max_val,Min_val)
print(Exta(a))
