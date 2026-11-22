class Solution:
    def threeSum(self, nums):
        # Inefficient code time complexity is high
        three_sums = []
        for i in range(len(nums)-2):
            diff1 = 0 - nums[i]
            for j in range(i+1,len(nums)):
                diff2 = diff1 -nums[j]
                if diff2 in nums[j+1:]:
                    x = [nums[i], diff2,nums[j]]
                    if sorted(x) not in three_sums:
                        three_sums.append(sorted(x))
        return three_sums

    def threeSum2(self,nums):
        nums.sort()
        three_sums = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    x = [nums[i], nums[left], nums[right]]
                    three_sums.append(x)
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return three_sums


if __name__ == "__main__":
    nums=[-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum2(nums))
