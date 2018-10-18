# coding=utf-8
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l = len(s)
        next = [-1 for i in range(l)]
        j = -1
        for i in range(1, l):
            while j >= 0 and s[i] != s[j + 1]:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
            next[i] = j
        lenSub = l - 1 - next[- 1]
        # 对于字符串s，如果j满足，0<=j<=n-1，且s(0，j) = s(n-1-j，n-1)，
        # 令k=n-1-j，若k整除n，不妨设n=mk，则s(0，(m-1)k - 1) = s(k，mk - 1)，
        # 即s(0，k-1) = s(k，2k-1) = …… = s((m-1)k - 1，mk - 1)，即s满足题设条件。
        # 故要判断s是否为重复子串组成，只需找到满足上述条件的j，且k整除n，即说明s满足条件，否则不满足。
        print next
        print lenSub
        return lenSub != l and l % lenSub == 0
s = Solution()
s.repeatedSubstringPattern('abcabcabcabc')
