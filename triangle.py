s=input()
h=int(input())
def tri (h, depth=1, symbol=s):
    if h%2!=0 and depth==h//2+1:
        print (symbol*depth)
        return
    if h%2==0 and depth==h//2:
        print(symbol*depth)
        print(symbol * depth)
        return
    print(symbol * depth)
    tri(h, depth=depth+1)
    print(symbol*depth)
    return
print (tri (h))
