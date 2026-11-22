from collections import defaultdict

# This is bucket sort
class Solution:
    def topKFrequent1(self, nums, k):
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] += 1
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

class Solution:
    def topKFrequent(self, nums, k: int):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

if __name__ == "__main__":
    nums=[1,2,2,3,3,3]
    k = 2
    sol = Solution()
    t = sol.topKFrequent1(nums, k)
    print(t)