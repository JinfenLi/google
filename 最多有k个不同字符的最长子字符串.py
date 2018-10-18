# coding=utf-8
def lengthoflongestsubstringkdistrinct(s,k):
    ret = 0
    start = 0
    # map存储k个不同key的值，
    map = {}
    for i in range(len(s)):
        if map.has_key(s[i]):
            map[s[i]] += 1
        else:
            map[s[i]] =1

        end = i
        # 只留下k个不同key的值
        while len(map)>k:
            map[s[start]] -= 1
            # 将没有Key的值移除map
            if map[s[start]] == 0:
                map.__delitem__(s[start])
            start += 1
        ret = max(ret,end-start+1)
    return ret

print lengthoflongestsubstringkdistrinct('bbaece',2)