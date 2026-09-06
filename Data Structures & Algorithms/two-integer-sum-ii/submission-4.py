class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        while index2 > index1:
            two_sum = numbers[index1] + numbers[index2]
            if two_sum == target:
                break
            elif two_sum > target:
                index2 -= 1
                counter = index1
            else:
                index1 += 1
                if index1 == index2:
                    index1 = counter + 1
                    index2 -= 1
        output = []
        output.append(index1 + 1)
        output.append(index2 + 1)
        return output
        