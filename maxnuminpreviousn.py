
a=[6,6,7,8,4,3]
before=[0]*(len(a)+1)
after=[0]*(len(a)+1)
# 前i个数的最大值
for i in range(1,len(a)+1):
    before[i]=max(a[i-1],before[i-1])
print before
# 后i个数的最大值
for i in range(1,len(after)):
    after[i] = max(a[len(a)-i],after[i-1])
print after