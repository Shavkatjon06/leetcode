def topKFrequent(nums, k):
    bag = {}  # to keep count how many of each element we have
    for i in nums:  # loop through nums
        if i in bag:
            bag[i] += 1  # if, let's say, 3 is in our bag 3: 1, we will increment by 1 => 3: 2
        else:
            bag[i] = 1  # else, assign new key:value and give 1

    freq = [[] for i in range(len(nums) + 1)]  # a list of empty lists to keep elements based on frequency
    # freq = [[], [], [], [], [], [], []]
    for i, x in bag.items():  # i is number, x is frequency => {1: 2, 2: 1, 3: 3}
        freq[x].append(i)  # let's say nums = [1,1,2,3,3,3]
        # freq[2].append(1)
        # freq[1].append(2)
        # freq[3].append(3)
    # after loop, freq = [[], [2], [1], [3], [], [], [], []]
    # 2 appears once, 1 appears twice, 3 appears 3 times.

    ans = []  # store k most frequent elements
    for i in range(len(freq)-1, 0, -1):  # loop through frequency lists from highest to lowest frequency
        for x in freq[i]:  # loop through each element in the current frequency list
            ans.append(x)  # append element to ans
            if len(ans) == k:  # if we reach k elements
                return ans  # return


print(topKFrequent([1,1,2,3,3,3], 2))