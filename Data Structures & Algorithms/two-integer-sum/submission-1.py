class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 1
        while nums[index1] + nums[index2] != target:
            if len(nums) == index2 + 1:
                index1 += 1
                index2 = index1 + 1
            else:
                index2 += 1
        return [index1, index2]


        