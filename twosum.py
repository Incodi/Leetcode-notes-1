class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Best solution for twosum
        hash = dict()
        # enumerate() allows us to get the index and item of a list easily
        for i, num in enumerate(nums):
            sum = target - num

            if sum in hash:
                return [i, hash[sum]]
            else:
                hash[num] = i