# Flight and Hotel Price Matching
# If you're booking a trip and have two sorted lists: one with flight prices and
# another with hotel prices, you may want to find the best combination that stays
# closest to your budget.

import sys


def findClosest(flights, hotels, x):
    minDiff = sys.maxsize
    ans_l = 0
    ans_r = 0
    left, right = 0, len(hotels)-1
    while left < len(flights) and right >= 0:
        total = flights[left] + hotels[right]
        diff = abs(total - x)
        if diff < minDiff:
            ans_l = flights[left]
            ans_r = hotels[right]
            minDiff = diff
        if total > x:
            right -= 1
        else:
            left += 1
    return [ans_l, ans_r]


print(findClosest([100, 120, 155, 210], [85, 110, 130, 140], 250))
