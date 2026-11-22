class Solution:
    def longestConsecutive1(self, nums):
        # TC -> O(n*logn) {for sorting},
        # SC -> O(n)
        nums = sorted(set(nums))
        len_nums = len(nums)
        if len_nums < 1:
            return 0
        x = []
        i = 0
        while i < len_nums:
            r = [nums[i]]
            j = i + 1

            while j < len_nums and (nums[j] == nums[j-1]+1):
                r.append(nums[j])
                j += 1
            x.append(r)
            i = j
        x_len = []
        for num in x:
            x_len.append(len(num))
        return max(x_len)

class Solution:
    def longestConsecutive2(self, nums):
        sorted_nums = sorted(set(nums))
        if not sorted_nums:
            return 0

        longest = 1
        count = 1
        for i in range(1,len(sorted_nums)):
            if (sorted_nums[i] == sorted_nums[i-1]+1):
                count +=1
            else:
                longest = max(longest,count)
                count = 1
        return max(longest, count)



if __name__ == "__main__":
    nums = [0,3,2,5,4,6,1,1]
    sol = Solution()
    t = sol.longestConsecutive2(nums)
    print(t)