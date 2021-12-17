class Solution(object):

    def twoSum(self , nums , target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        """
        dictionary = {}
        i = 0
        while i<len(nums):
            if (target - nums[i]) not in dictionary:
                dictionary[nums[i]] = i
                i+=1
            else:
                return(dictionary[target-nums[i]], i)



    def twoSumOriginal(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j])==target:
                    return(i, j)

    def reverseNum(self , x):
        """
        :type x: int
        :rtype: int
        """
        if ((x > 2 ** 31 - 1) or (x < -2 ** 31)):
            return 0

        negFlag = -1 if x < 0 else 1
        x = abs(x)
        revDict = {}
        divisor = 1

        while (x > 0):
            remainder = x % 10
            revDict.update({divisor: remainder})
            x = (x - remainder) // 10
            divisor *= 10

        multipliers = list(revDict.keys())
        multipliers.reverse()

        res = [ x * y for x , y in zip(multipliers , revDict.values()) ]

        if((out>2**31-1) or (out<-2**31)):
            return 0
        else:
            return out