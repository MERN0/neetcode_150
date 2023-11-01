class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        sorted_elements = sorted(freq_dict.keys(), key = lambda x: freq_dict[x], reverse=True)

        return sorted_elements[:k]
