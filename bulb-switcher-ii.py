def flipLights(n,m):
    if m == 1:
        if n == 2:
            return 3
        return min(4, 1<<n)
    if m == 2:
        return min(7,1<<n)
    return min(8,1<<n)
print flipLights(6,8)