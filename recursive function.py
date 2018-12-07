def a(n):
    try:
        if n > 10:
            return n * a(n - 1)


print(a(5))
