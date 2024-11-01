for i in range (len(sp1)):
    if sp[:a]==sp[:a:-1]  and sp1[i]!="A" and sp1[i]!="H" and sp1[i]!="I" and sp1[i]!="M" and sp1[i]!="O" and sp1[i]!="T" and sp1[i]!="U" and sp1[i]!="V" and sp1[i]!="W"  and sp1[i]!="X" and sp1[i]!="Y" and sp1[i]!="1" and sp1[i]!="8" and sp1[i]!="E" and sp1[i]!="J" and sp1[i]!="S" and sp1[i]!="Z":
       u+=1
    else:
      if   sp[i]=="3" or sp[i]=="L" or sp[i]=="2" or sp[i]=="5':":
        t+=1
if u>0: ##тогда е зеркало
    if sp[:a]==sp[:a:-1]:
        print(str,"  is a regular palindrome." )
    else:
        print(str, " is not a palindrome.")
else:
    if t>0 and sp[:a]==sp[:a:-1]:
        print(str, "is a mirrored string.")
    elif t==0 and sp[:a]==sp[:a:-1]:
        print(str, "is a mirrored palindrome")
    elif sp[:a]!=sp[:a:-1]:
        print(str, "is not a palindrome")