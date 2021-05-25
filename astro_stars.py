inp=int(input("No of rows:"))
lst=[0]*inp
c=0
for i in lst:
   lst[c]=c+1
   c+=1
t_or_f=int(input("0 or 1:"))
if bool(t_or_f):
    for i in lst:
        j=0
        while j<i:
            print("*",end=' ')
            j+=1
        print()
else:
    lst.reverse()
    for i in lst:
        print("* "*i,end=' ')
        print()
