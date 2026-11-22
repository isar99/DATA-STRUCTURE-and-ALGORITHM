class Solution:
    def countSeniors(self, details):
        count = 0
        for i in details:
            age = int(i[11:13])
            if age > 60:
                count+=1
        return count


if __name__ == "__main__":
    nums = ["1313579440F2036","2921522980M5644"]
    sol = Solution()
    k = sol.countSeniors(nums)
    print(k)