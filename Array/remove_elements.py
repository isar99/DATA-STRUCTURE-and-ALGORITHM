# class Solution:
#     def removeElement(self, nums, val) -> int:
#         new_arr = []
#         k = 0
#         for i in nums:
#             print(i, val)
#             if i != val:
#                 k+=1
#                 new_arr.append(i)
#             else:
#                 new_arr.append("_")
#         return k, new_arr

class Solution:
    def removeElement(self, nums, val) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
            print(k, nums)
        return k

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    sol = Solution()
    k = sol.removeElement(nums, val)
    print(k)
