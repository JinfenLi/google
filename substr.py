#coding=utf-8
# 对于一个给定的 source 字符串和一个 target 字符串，
# 你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。
# 。我之前想的是如果匹配，子串和母串同时移动，如果不匹配，子串返回首位置，母串继续移动，
# 但是就是这出错了，，，比如acactor 和 actor 匹配时，应该进一步修改细节，如果不匹配，
# 这时候如果是因为子串首字母都不匹配，那么原思路是正确的，但是如果匹配了一半不匹配了，
# 此时母串不应该向后移动的。即i++
def substr(source,target):
    if source is None or target is None or len(source)<len(target):
        return -1
    if len(target)==0:
        return 0
    i = 0
    j = 0
    while(True):
        if source[i] == target[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            j = 0
        if j == len(target):
            return i-j
        if i == len(source):
            break
    return -1