class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        leftSum = 0
        for (i,v) in enumerate(nums):
            if  leftSum == total-v:
                return i
            leftSum+=v
            total-=v
            print(leftSum,total)
        return -1