# class Solution:
#     def findMaxConsecutiveOnes(self, nums):
#         n, max_cnt = len(nums), 0
#         for i in range(n):
#             cnt = 0
#             for j in range(i,n):
#                 if nums[j] == 0:
#                     break
#                 cnt+=1
#             max_cnt = max(max_cnt, cnt)
#         return max_cnt

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        res = cnt = 0
        for num in nums:
            if num == 0:
                res = max(res, cnt)
                cnt = 0
            else:
                cnt+=1
        return max(res, cnt)


if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    sol = Solution()
    k = sol.findMaxConsecutiveOnes(nums)
    print(k)
