a=[3,5,2,6,7,5,8,1,4,8,5,2]
frequency= {}
for i in a:
    frequency[i]=frequency.get(i,0)+1
print(frequency)

