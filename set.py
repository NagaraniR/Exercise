x = set(["Postcard", "Radio", "Telegram","Postcard"])
print(x)
y = {"Postcard","Radio","Telegram"}
print(y)
x.add("Telephone")
print(x)
print( x.difference(y) )
print( y.difference(x) )
print( x.issubset(y) )
print( x.issuperset(y) )
print( y.issubset(x) )
print( y.issuperset(x) )
print( x.intersection(y) )
