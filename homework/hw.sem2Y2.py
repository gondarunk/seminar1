sp = input().split()
a = int(sp[0])
str = sp[1]
str1=""
for i in range (len(str)//a):
    str1 += ''.join(reversed(str[i * a:(i + 1) * a]))
print(str1)