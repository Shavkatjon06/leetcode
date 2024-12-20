# Binary search approach
def insertPosition(nums, target):
    head = 0
    tail = len(nums) - 1
    while head <= tail:
        mid = (head + tail) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            head = mid + 1
        else:
            tail = mid - 1
    return head

print(insertPosition([1,3,10,11], 4))
print(insertPosition([1,3,10,11],0))
print(insertPosition([0,3,8,16,20], 21))