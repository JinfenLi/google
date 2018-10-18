def maxCoins(nums):
    n = len(nums)
    dp = [[0]*(n+2)]*(n+2)
    visit = [[0]*(n+2)]*(n+2)
    arr = [1]
    for i in range(1,n+1):
        arr.append(nums[i-1])
    arr[n+1]=1
    return search(arr,dp,visit,1,n)

def search(arr,dp,visit,left,right):
    if visit[left][right] == 1:
        return dp[left][right]
    res = 0
    for k in range(left,right+1):
        midValue = arr[left-1]*arr[k]*arr[right+1]
        leftValue = search(arr,dp,visit,left,k-1)
        rightValue = search(arr,dp,visit,k+1,right)
        res = max(res,leftValue+midValue+rightValue)
    visit[left][right] = 1
    dp[left][right] = res
    return res