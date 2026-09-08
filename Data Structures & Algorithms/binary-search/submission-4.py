class Solution:
    def search(self, nums: List[int], target: int) -> int:
        indexleft = 0
        indexright = len(nums) - 1
        index = (indexright - indexleft) // 2
        if nums[indexright] < target:
            return -1
        elif nums[indexright] == target:
            return indexright    
        if nums[indexleft] > target:
            return -1
        elif nums[indexleft] == target:
            return indexleft 
        while nums[index] != target:
            if nums[index] < target:
                indexleft = index
                index = index + (indexright - indexleft) // 2               
            elif nums[index] > target:
                indexright = index
                index = (indexright - indexleft) // 2
            if (indexright - indexleft) // 2 == 0:
                    return -1
        return index
                


        