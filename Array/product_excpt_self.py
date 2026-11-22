from functools import reduce
class Solution:
    # This solution is correct but inefficient.
    def productExceptSelf1(self, nums):
        new_ls = []
        for num in range(len(nums)):
            nums_cp = nums.copy()
            nums_cp.pop(num)
            multiply = reduce(lambda x,y: x*y, nums_cp)
            new_ls.append(multiply)
        return new_ls

    def productExceptSelf2(self, nums):
        # Solution is correct, but time limit exceed.
        new_ls = []
        for num in range(len(nums)):
            mulx = 1
            for j in range(len(nums)):
                if j != num:
                    mulx *= nums[j]
            new_ls.append(mulx)
        return new_ls

    def productExceptSelf3(self, nums):
        # Most efficient one.
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

if __name__ == "__main__":
    nums=[1, 2, 3, 4]
    sol = Solution()
    t = sol.productExceptSelf3(nums)
    print(t)