# coding=utf-8
# 给定一个数组，数组中只包含0和1。请找到一个最长的子序列，其中0和1的数量是相同的。
# dp表示前i个串的和，0表示-1，找出最长的和为0的串，分从头开始或者非从头开始
def max01(str):
    length=len(str)
    dp = [0]*(length+1)
    dp[1] = -1 if str[0]=='0' else 1
    for i in range(2,length+1):
        dp[i] = -1 if str[i-1]=='0' else 1
        dp[i] += dp[i-1]
    # 统计最大01字串
    start = 0
    max = 0
    m ={}
    print dp
    # 如果从头开始，即最后一个值是0，并且长度是偶数位
    for i in range(length,0,-1):
        if dp[i] == 0 and i%2 == 0:
            return str[0:i]
    # 非从头开始，同样key值的最大差
    for i in range(1,length+1):
        if dp[i] not in m.keys():
            m[dp[i]] = i
        begin = m[dp[i]]

        if i-begin>max:
            max = i-begin
            start = begin
    return str[start:max+1]
print max01('1101000')

