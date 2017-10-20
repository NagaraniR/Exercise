l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print ','.join(l)
d=dict()
n=int(raw_input("enter number:"))
for key in range(n+1):
  d[key]=key*key
print d 

list=[x for x in raw_input("Enter data:").split('-')]
list.sort()
print ','.join(list)
