class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]  +=1
            else:
                freq[num] =  1
        freq_list = sorted(freq.items(), key = lambda item: item[1], reverse = True)
        return [pair[0] for pair in freq_list][:k]