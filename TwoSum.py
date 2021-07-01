"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

# ip = [2,7,11,15]
# target = 9
#
# compliment_dict = {}
#
# result = []
#
# for idx, num in enumerate(ip):
#     compliment = target - num
#     if num in compliment_dict.keys():
#         result = [compliment_dict.get(num), idx]
#         break
#     else:
#         compliment_dict[target - num] = idx
#
# if result:
#     print(f"found: indexes {result[0]} & {result[1]}: {ip[result[0]]} + {ip[result[1]]} = {target}")
# else:
#     print("No match found")
#
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_dict: dict = {}
        result: List[int] = []

        for idx, num in enumerate(nums):
            compliment = target - num
            if num in compliment_dict.keys():
                result = [compliment_dict.get(num), idx]
                break
            else:
                compliment_dict[compliment] = idx

        return result

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
