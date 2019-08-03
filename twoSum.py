class Solution:
    def twoSum(self, nums, target):
        """
        target = 9
        array = [2,7,8,6,5]
        result = [0,1] hence 2 +7 = 9

        target = 6
        array = [3,3,8,9]
        res = [0,1]

        target = 6
        array = [3,2,3,8,9]
        res = [0,2]

        target = 0
        array = [3,0,6,0,8,9]
        res = [1,3]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
