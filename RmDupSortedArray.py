class Solution:
    def removeDuplicates(self, nums):
        fast_slow = []
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                fast_slow.append( (fast,slow) )

                if nums[fast] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[fast]
                    print(nums, 'slow=%d' % slow, 'fast=%d' % fast)
            return [ slow + 1, fast_slow]
        else:
            return [ 0 ]
