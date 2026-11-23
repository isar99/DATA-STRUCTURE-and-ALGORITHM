class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = list(s)
        max_len = 1
        for i in range(len(x)):
            count = 1
            j = i+1
            while j < len(x)-1:
                if x[j] == x[j+1]:
                    break
                else:
                    count += 1
                print(x[i], x[j], max_len, count)
                j += 1
                max_len = max(max_len, count)
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

if __name__ == "__main__":
    s = "pwwkew"
    sol = Solution()
    result = sol.lengthOfLongestSubstring2(s)
    print(result)