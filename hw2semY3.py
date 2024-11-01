str=input()
## a - половина строки
if len(str)%2==0:
    a=len(str)//2
else:
    a = (len(str) -1)// 2
sp=[]
sp1=[]
for i in range (len(str)):
    sp.append(str[i])
    sp1.append(str[i])
for i in range (len(str)):
    if sp[i]=="E":
        sp[i]="3"
    if sp[i]=="J":
        sp[i]='L'
    if sp[i]=="S":
        sp[i]='2'
    if sp[i]=="Z":
        sp[i]="5"
if len(str)%2==0:
    if sp[:a - 1:-1] == sp[:a] and sp1[:a - 1:-1] == sp1[:a]:  ## усллвие на зеркало
        print(str, " is a mirrored palindrome.")
    elif sp[:a - 1:-1] == sp[:a] and sp1[:a - 1:-1] != sp1[:a]:
        print(str, " EA3 is a mirrored string.")
    elif sp1[:a - 1:-1] == sp1[:a]:
        print(str, "is a regular palindrome")
    elif sp1[:a - 1:-1] != sp1[:a]:
        print(str, "is not a palindrome")
else:
    if sp[:a:-1] == sp[:a] and sp1[:a:-1] == sp1[:a] and sp[a]!="B" and sp[a]!="C" and sp[a]!="D" and sp[a]!="F" and sp[a]!="G" and sp[a]!="K" and sp[a]!="N" and sp[a]!="P" and sp[a]!="Q" and sp[a]!="R" and sp[a]!="9" and sp[a]!="7"  and sp[a]!="6" and sp[a]!="4":  ## усллвие на зеркало
        print(str, " is a mirrored palindrome.")
    elif sp[:a :-1] == sp[:a] and sp1[:a :-1] != sp1[:a] and sp[a]!="B" and sp[a]!="C" and sp[a]!="D" and sp[a]!="F" and sp[a]!="G" and sp[a]!="K" and sp[a]!="N" and sp[a]!="P" and sp[a]!="Q" and sp[a]!="R" and sp[a]!="9" and sp[a]!="7"  and sp[a+1]!="6" and sp[a+1]!="4":
        print(str, " EA3 is a mirrored string.")
    elif sp1[:a :-1] == sp1[:a]:
        print(str, "is a regular palindrome")
    elif sp1[:a :-1] != sp1[:a]:
        print(str, "is not a palindrome")




