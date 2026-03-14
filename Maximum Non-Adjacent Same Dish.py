#It works very well but dont know if it is optimal or not.....tried my best 

#Ramu has N dishes of different types arranged in a row: A1,A2,…,AN where Ai denotes the type of the ith dish.
#He wants to choose as many dishes as possible from the given list but while sa sfying two conditions:
#•	He can choose only one type of dish.
#•	No two chosen dishes should be adjacent to each other.


def sol():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        last = {}
        count = {}
        
        for i, x in enumerate(arr):
            
            if x not in last:
                last[x] = -2
                count[x] = 0
            
            if i != last[x] + 1:
                count[x] += 1
                last[x] = i
        
        ans = min(count, key=lambda k: (-count[k], k))
        print(ans)
