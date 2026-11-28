class Solution:
    def search(self, nums, target):
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (r+l)//2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return -1



if __name__ == "__main__":
    nums = [5, 6, 1, 2, 3, 4]
    target = 3
    sol = Solution()
    result = sol.search(nums, target)
    print(result)