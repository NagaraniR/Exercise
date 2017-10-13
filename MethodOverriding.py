class MethodOverriding:
    def methodOne(self,arg):
        print "value of parent: %d "%arg
class MethodOverridingOne(MethodOverriding):
    def methodOne(self,arg2):
        print "value of child: %d "%arg2
obj=MethodOverriding()        
obj.methodOne(100)
obj1=MethodOverridingOne()
obj1.methodOne(200)


#output
#value of parent: 100 
#value of child: 200 
