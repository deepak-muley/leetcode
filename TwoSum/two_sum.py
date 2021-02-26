from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapTargetTo2IndicesList = {}
        idx = 0
        while idx < len(nums) - 1:
            first = nums[idx]
            second = nums[idx + 1]
            sum = first + second
            mapTargetTo2IndicesList[sum] = [idx, idx + 1]
            idx += 1

        if target in mapTargetTo2IndicesList:
            return mapTargetTo2IndicesList[target]


soln = Solution()

nums = [2, 7, 11, 15]
target = 9
print("nums={} target={} indexes{}".format(nums, target, soln.twoSum(nums, target)))

nums = [3, 2, 4]
target = 6
print("nums={} target={} indexes{}".format(nums, target, soln.twoSum(nums, target)))

nums = [3, 3]
target = 6
print("nums={} target={} indexes{}".format(nums, target, soln.twoSum(nums, target)))