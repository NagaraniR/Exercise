def sum(list):
    if len(list)==1:
     return list[0]
    else:
      return list[0]+sum(list[1:])
print sum([1,2,3,4,5])    

#output
#15
