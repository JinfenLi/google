# coding=utf-8
# dp[i] - 表示子串（0，i）的最小回文切割，则最优解在dp[s.length-1]中。（0,i）的子串中包括了i+1个字符。
#  分几种情况：
#   1.初始化：当字串s.substring(0,i+1)(包括i位置的字符)是回文时，dp[i] = 0(表示不需要分割)；否则，dp[i] = i（表示至多分割i次）;
#   2.对于任意大于1的i，如果s.substring(j,i+1)( 1 =< j <=  i ,即遍历i之前的每个子串)是回文时，dp[i] = min(dp[i], dp[j-1]+1);
#    (注：j不用取0是因为若j == 0，则又表示判断（0，i）)。
def minCut(s):
    if s is None or len(s) == 0:
        return 0
    dp = [0]*len(s)
    dp[0] = 0
    for i in range(1,len(s)):

        if ispalindrome(s[0:i+1]):
            dp[i] = 0
        else:
            dp[i] = i

        for j in range(i,0,-1):
            if ispalindrome(s[j:i+1]):
                dp[i]=min(dp[i],dp[j-1]+1)
    return dp[-1]

def ispalindrome(s):
    begin = 0
    end = len(s)-1
    while begin<end:
        if s[begin]!=s[end]:
            return False
        begin += 1
        end -= 1
    return True
print minCut('abcd')