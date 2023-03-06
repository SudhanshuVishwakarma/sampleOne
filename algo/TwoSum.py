# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def twoSum(nums, target):

    for i in range(0, len(nums), 1):
        for j in range(i + 1, len(nums), 1):
            sum = nums[i] + nums[j]
            if sum == target:
                return i, j


nums = [1, 2, 4, 5, 6, 8, 9]
twoSum(nums, 9)
