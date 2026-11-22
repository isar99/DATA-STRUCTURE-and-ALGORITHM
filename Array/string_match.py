class Solution:
    def stringMatching(self, words):
        words_len = len(words)
        new_words = []
        for n in range(words_len):
            new_ls = words[:n]+words[n+1:]
            for j in new_ls:
                if words[n] in j:
                    new_words.append(words[n])
        return set(new_words)



if __name__ == "__main__":
    words=["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    sol = Solution()
    k = sol.stringMatching(words)
    print(k)