def singleNumber(nums):
    if len(nums) <= 1:  # just return a single element
        return nums[0]
    bag = {}  # to save number: amounts
    for i in nums:
        if i in bag:  # if it's already in our bag
            bag[i] += 1  # increment by one
        else:
            bag[i] = 1  # if not, then add and give value 1
    for i, x in bag.items():  # i = key, x = value
        if x == 1:  # if our amount (value) is 1
            return i  # return its key

print(singleNumber([4,1,3,1,3]))
