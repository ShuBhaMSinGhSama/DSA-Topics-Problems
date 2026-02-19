a=[3,5,2,6,7,5,8,1,4,8,5,2]

x = set()
result = []

for num in a:
    if num not in x:
        x.add(num)
        result.append(num)

print(result)
