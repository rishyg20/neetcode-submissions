class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue           # skip duplicate anchors
            if nums[i] > 0:
                break               # sorted + positive anchor -> nothing further can sum to 0

            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1     # skip duplicate lefts
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1    # skip duplicate rights
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result