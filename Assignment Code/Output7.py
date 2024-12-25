def fun(x, n):
    if (n == 0):
        return 1
    elif (n % 2 == 0):
        return fun(x * x, n //2)
    else:
        return x * fun(x * x, (n - 1) // 2)

ans = fun(2, 10)
print(ans)