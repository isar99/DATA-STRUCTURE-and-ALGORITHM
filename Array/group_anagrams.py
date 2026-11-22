from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs):
#         ana = []
#         visited = set()
#
#         for i in range(len(strs)):
#             if i in visited:
#                 continue
#
#             new_strs = [strs[i]]
#             visited.add(i)
#
#             for j in range(i + 1, len(strs)):
#                 if j not in visited and sorted(strs[i]) == sorted(strs[j]):
#                     new_strs.append(strs[j])
#                     visited.add(j)
#
#             ana.append(new_strs)
#
#         return ana

# class Solution:
#     def groupAnagrams(self, strs):
#         res = defaultdict(list)
#         for s in strs:
#             sortedS = ''.join(sorted(s))
#             res[sortedS].append(s)
#         return list(res.values())

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())



if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]
    sol = Solution()
    k = sol.groupAnagrams(strs)
    print(k)
