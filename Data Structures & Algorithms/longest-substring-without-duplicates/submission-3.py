class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}       # dictionary: character -> the index where we last saw it
        left = 0        # left edge of our current window
        max_len = 0      # best (longest) window length found so far

        for right in range(len(s)):
            char = s[right]

        
            if char in seen and seen[char] >= left:
                left = seen[char] + 1   

            seen[char] = right           
            max_len = max(max_len, right - left + 1)  

        return max_len
