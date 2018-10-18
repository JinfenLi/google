# coding=utf-8
# 主串T，比较串P，
# 由于KMP算法的思想是主串不回溯的简化算法，执行的时候呢在串比较的扫描里面要么执行POST和POSP，
# 要么执行NEXT[]数组的右移，然后比较，所以字符比较最多就是为O（LenthT）,即不会超过O（n）
def cal_next(str,len):
    # next[0]初始化为-1，-1表示不存在相同的最大前缀和最大后缀，k表示长度
    next = [-1]*len
    next[0] = -1
    k = -1
    for q in range(1,len):
        # 如果下一个不同，那么k就变成next[k]，注意next[k]是小于k的，无论k取任何值。
        while k > -1 and str[k + 1] != str[q]:
            # 往前回溯
            k = next[k]
        # 如果相同，k++
        if str[k + 1] == str[q]:

            k +=1
        # 这个是把算的k的值（就是相同的最大前缀和最大后缀长）赋给next[q]
        next[q] = k
    return next
print cal_next('ababaca',7)

def KMP(str, slen, ptr, plen):
    next = cal_next(ptr,plen)
    k = -1
    for i in range(slen):
        # ptr和str不匹配，且k>-1（表示ptr和str有部分匹配）
        while k >-1 and  ptr[k + 1] != str[i]:
            k = next[k]
        if ptr[k + 1] == str[i]:
            k += 1
        if k == plen-1:

            # cout << "在位置" << i-plen+1<< endl;
            # k = -1;//重新初始化，寻找下一个
            # i = i - plen + 2;//i定位到找到位置处的下一个位置（这里默认存在两个匹配字符串可以部分重叠）
            return i-plen+1
    return -1
print KMP('bacbababadababacambabacaddababacasdsd',36,'ababaca',7)


