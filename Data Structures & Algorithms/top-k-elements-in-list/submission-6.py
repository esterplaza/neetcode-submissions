class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        output = []
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        if len(frequency) == k:
            for key in frequency.keys():
                output.append(key)
            return output
        else:
            for i in range(k):
                previous = 0
                for key, value in frequency.items():
                    if value >= previous:
                        max_frequency = value 
                        max_num = key
                    previous = max_frequency
                output.append(max_num)
                frequency.pop(max_num)
            return output
            


        