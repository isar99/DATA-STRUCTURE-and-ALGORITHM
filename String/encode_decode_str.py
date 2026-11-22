class Solution:

    # def encode(self, strs):
    #     enc_str = ""
    #     len_strs = len(strs)
    #     if len_strs < 1:
    #         return enc_str
    #     for str in strs[:len_strs-1]:
    #         enc_str += str+":;"
    #     enc_str = enc_str+strs[-1]
    #     return enc_str

    # def encode(self, strs):
    #     enc_str = ""
    #     len_strs = len(strs)
    #     if len_strs < 1:
    #         return enc_str
    #     i = 0
    #     while i < len_strs-1:
    #         enc_str += strs[i]+":;"
    #         i += 1
    #     enc_str = enc_str+strs[-1]
    #     return enc_str

    def encode(self, strs):
        enc_string = ""
        for x in strs:
            enc_string += str(len(x))+"#"+x
        return enc_string


    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            res.append(s[j+1:j+1+word_len])
            i = j+1+word_len
        return res



strs = ["hello","ai","ia","are"]
sol = Solution()

encoded_str = sol.encode(strs) # string
print(encoded_str)

decoded_Strs = sol.decode(encoded_str) # List
print(decoded_Strs)