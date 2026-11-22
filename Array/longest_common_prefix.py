# class Solution:
#     def longestCommonPrefix(self, strs):
#         prefix = strs[0]
#         for i in range(1, len(strs)):
#             j = 0
#             while j < min(len(prefix), len(strs[i])):
#                 if prefix[j] != strs[i][j]:
#                     break
#                 j += 1
#             prefix = prefix[:j]
#         return prefix

class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

if __name__ == "__main__":
    strs = ["bat","bag","bank","band"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))