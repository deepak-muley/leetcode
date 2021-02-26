from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        idx = 0
        while idx < len(nums):
            complement = target - nums[idx]
            if complement in map:
                return [map[complement], idx]
            map[nums[idx]] = idx
            idx += 1


soln = Solution()

nums = [2, 7, 11, 15]
target = 9
print("nums={} target={} indexes={}".format(nums, target, soln.twoSum(nums, target)))

nums = [3, 2, 4]
target = 6
print("nums={} target={} indexes={}".format(nums, target, soln.twoSum(nums, target)))

nums = [3, 3]
target = 6
print("nums={} target={} indexes={}".format(nums, target, soln.twoSum(nums, target)))

nums = [3, 4, 9, 100]
target = 12
print("nums={} target={} indexes={}".format(nums, target, soln.twoSum(nums, target)))