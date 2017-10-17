class Father:
    name="humans"
    def father(self,action):
        print "father is",action
class Mother(Father):       
    def mother(self,action):
        print "mother is",action
class Baby(Mother):
    def baby(self,action):
        print "baby is",action
obj=Baby()
print obj.name
obj.father("talking")
obj.mother("laughing")
obj.baby("sleeping")
obj1=Mother()
obj1.father("talking")
obj1.mother("laughing")
obj2=Father()
obj2.father("talking")

#output
#============= RESTART: /home/linuxuser/multilevelInheritance.py =============
#humans
#father is talking
#mother is laughing
#baby is sleeping
#father is talking
#mother is laughing
#father is talking
