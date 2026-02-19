nums=[2,3,8,4,7,6,5,8]
target= 9
def ts (nums, target):
    hash_map={}

    for i, num in enumerate(nums):
        ans= target-num
        if ans in hash_map:
            return(ans,num)
        hash_map[num]= i

print(ts(nums,target))
