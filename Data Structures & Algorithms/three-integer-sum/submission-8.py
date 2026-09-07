class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        index1 = 0
        index2 = 1
        index3 = len(nums) - 1
        stack = []
        if len(nums) < 3:
            return stack
        nums.sort()
        for index1 in range(len(nums) - 2):
            index2 = index1 + 1
            index3 = len(nums) - 1
            while True:
                test = nums[index2] + nums[index3]
                if nums[index1] < -(nums[index2] + nums[index3]):
                    index2 += 1
                    if index2 == index3:
                        break
                elif nums[index1] > -(nums[index2] + nums[index3]):
                    index3 -= 1
                    if index2 == index3:
                        break
                else:
                    suma_zero = []
                    suma_zero.append(nums[index1])
                    suma_zero.append(nums[index2])
                    suma_zero.append(nums[index3])
                    suma_zero.sort()
                    if suma_zero not in stack:
                        stack.append(suma_zero) 
                    index3 -= 1
                    if index3 == index2:
                        break
        return stack


            
        