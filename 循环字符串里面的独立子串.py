#coding=utf-8
# 假设s是一个无限循环的字符串”abcdefghijklmnopqrstuvwxyz”，
# s就是一个”...zabcdefghijklmnopqrstuvwxyza...”这样的字符串，
# 现在给你另外一个字符串p，求p中存在多少个截然不同的子串，
# 使得它们也是s的子串。p只包括英语的小写字母并且p的长度可能大于10000。
# 输入：zab
# 输出：6
# 说明：'z','a','b','za','ab','zab'都是s的子串
#运用哈希表，dp储存26个字母的哈希表，若字串按顺序则pos++,否则pos=1，最后取比较大的每个字母的哈希值相加
def findSubstringInWraproundString(p):
    dp = []
    for i in range(26):
        dp.append(0)
    n = len(p)
    pos = 0
    for i in range(n):
        if (i>0 and ord(p[i])-ord(p[i-1])==1) or (p[i]=='a' and p[i-1]=='z'):
            pos += 1
        else:
            pos = 1
        dp[ord(p[i])-ord('a')] = max(dp[ord(p[i])-ord('a')],pos)
    ans = 0
    for i in range(26):
        ans += dp[i]
    return ans
print findSubstringInWraproundString('abcdpjiegzabc')
