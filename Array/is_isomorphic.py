class Solution:
    def isIsomorphic(self, s: str, t: str):
        s = s.lower()
        t = t.lower()

        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i, j in zip(s, t):
            if i in s_to_t and s_to_t[i] != j:
                return False

            if j in t_to_s and t_to_s[j] != i:
                return False

            s_to_t[i] = j
            t_to_s[j] = i

        return True



if __name__ == "__main__":
    s = "foo"
    t = "bar"
    sol = Solution()
    k = sol.isIsomorphic(s, t)
    print(k)

