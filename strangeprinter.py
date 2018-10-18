#coding=utf8
# 假设某一次打印机打印了若干个'a'，像这样：”aaaaaa”，在这之后打印的字符，无非是三种情况：
#  在这段字符串的内部打印，但是不覆盖这段字符串的一端，例如”abbbaa”、”abbada”。
# 在这段字符串的外部打印，完全不覆盖这段字符串，例如”bbaaaaaa”、”bbaaaaaaccc”。
# 覆盖这段字符串的一端，例如”baaaaa”、”baaacccccc”。
def starngeprinter(s):
    if s is None or len(s)==0:
        return 0
    n = len(s)
    f= [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        f[i][i] = 1
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            # L=1时，s[0]==s[L-1]必然成立，这时的答案为1 + s[1 ~ N-1]的最小打印次数；
            f[i][j] = 1 +f[i+1][j]
            for k in range(i+1,j):
                # s[0 ~ L-1]的最少打印次数实际等于 s[1 ~ L-1]的最少打印次数（也等于s[0 ~ L-2]的最少打印次数）如果中间有相等的
                if s[i] == s[k]:
                    f[i][j] = f[i+1][k]+f[k+1][j]
            # s[0 ~ L-1]的最少打印次数实际等于 s[1 ~ L-1]的最少打印次数（也等于s[0 ~ L-2]的最少打印次数）
            if s[i] == s[j]:
                f[i][j] = f[i+1][j]
    return f[0][n-1]

print starngeprinter('aabaac')