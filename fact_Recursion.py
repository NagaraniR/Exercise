import sys
sys.setrecursionlimit(2200)
def fact(num):
    if num==1:
     return 1
    else: 
     return num*fact(num-1)
print fact(1067)    

#output
#3628800
