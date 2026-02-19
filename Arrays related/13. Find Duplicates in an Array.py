a=[3,5,2,6,7,5,8,1,4,8,5,2]
x = set()
duplicate = set()

for num in a:
    if num in x:
        duplicate.add(num)
    else:
        x.add(num)

print(list(duplicate))
