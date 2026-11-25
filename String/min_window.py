class Solution:
    def minWindow(self, s, t):
        if t == "": return ""
        window = {}
        countT = {}
        for i in t:
            countT[i] = countT.get(i,0) + 1

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            print(c,window, l, r)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have ==  need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    result = sol.minWindow(s,t)
    print(result)