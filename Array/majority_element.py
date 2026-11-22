# class Solution:
#     def majorityElement(self, nums) -> int:
#         new_dict = {}
#         majority_element = len(nums)//2
#         for i in nums:
#             if i not in new_dict:
#                 new_dict[i] = 1
#             else:
#                 new_dict[i] += 1
#         for j in new_dict:
#             if new_dict[j] > majority_element:
#                 return j

class Solution:
    def majorityElement(self, nums) -> int:
        major_ele = len(nums)//2
        for i in nums:
            if nums.count(i) > major_ele:
                return i
        return 0


if __name__ == "__main__":
    nums = [2,2,2]
    sol = Solution()
    k = sol.majorityElement(nums)
    print(k)