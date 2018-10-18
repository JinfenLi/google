#coding=utf-8
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None:
            return 0
        mod = 1000000007
        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1, n + 1):
            # s[i-1]=='*'：s[i-1]可以解码成一个字符而且有9种可能，对于每一种可能，
            # 前i-1位都有f[i-1]中解码方式，故这种情况共有9*f[i-1]中解码方式。
            if s[i - 1] == '*':
                f[i] = (f[i] + 9 * f[i - 1]) % mod
                if i >= 2:
                    t = 0
                    # 若s[i-2]和s[i-1]均为'*'："**"，由于'*'可以表示为1到9，
                    # 而要解码成一个字符要求数字范围在10~26，故解码成一个字符的方法有15种，
                    # 即11~19以及21~26，对f[i]的贡献为15*f[i-2]。
                    if s[i - 2] == '*':
                        f[i] = (f[i] + 15 * f[i - 2]) % mod
                    # 若s[i-2]=='1'，则"1*"可以表示成"11"、"12"、……、"19"，解码为"K"到"S"，共9种可能
                    elif s[i - 2] == '1':
                        f[i] = (f[i] + 9 * f[i - 2]) % mod
                    # 则"2*"可以表示成"21"、"22"、"23"、"24"、"25"、"26"可以解码成一个字符，共6种可能
                    elif s[i - 2] == '2':
                        f[i] = (f[i] + 6 * f[i - 2]) % mod
            else:
                # 若s[i-1]!='0'，则s[i-1]可以解码为一个字符，同时，前i-1位有f[i-1]种解码方式，这种情况对f[i]的贡献为f[i-1]。
                if s[i - 1] >= '1' and s[i - 1] <= '9':
                    f[i] = (f[i] + f[i - 1]) % mod
                if i >= 2:
                    if s[i - 2] == '*':
                        t = 0
                        # 若s[i-2]=='*'，s[i-1]为数字字符：同样考虑这两位形成的数字可能的范围(10~26)。
                        # 若s[i-1]在'0'到'6'之间，那么s[i-2]可以取'1'或'2'两种可能，对f[i]的贡献为2*f[i-2]
                        if s[i - 1] >= '0' and s[i - 1] <= '6':
                            f[i] = (f[i] + 2 * f[i - 2]) % mod
                        # 若s[i-1]在'7'到’9‘之间，那么s[i-1]只能取'1'
                        elif s[i - 1] >= '7' and s[i - 1] <= '9':
                            f[i] = (f[i] + f[i - 2]) % mod
                    else:
                        twoDigits = int(s[i - 2 : i])
                        # s[i-2]和s[i-1]可以一起解码成一个字符，对f[i]的贡献为f[i-2]。
                        # 否则则s[i-2]和s[i-1]不能一起解码成一个字符，对f[i]的贡献为0
                        if twoDigits >= 10 and twoDigits <= 26:
                            f[i] = (f[i] + f[i - 2]) % mod
        return f[n]
s = Solution()
print s.numDecodings('**')