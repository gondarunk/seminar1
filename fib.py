def fib(a):
    if a==1 or a==2:
        return 1
    else:
        return fib(a-1)+fib(a-2)
n=int(input())
print(fib(n))