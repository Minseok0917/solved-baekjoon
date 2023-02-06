class Solution(object):
    def runningSum(self, nums):
        answer = []
        for i in range(len(nums)):
            value = nums[i]
            if i == 0:
                answer.append(value)
            else:
                answer.append(value+answer[i-1])
        return answer