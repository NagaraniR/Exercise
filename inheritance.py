class parent:
    parentattr=100
    def __init__(self):
        print "calling parent class constructor"
    def parentmethod(self):
        print "calling parent method"
    def setattr(self,attr):
        parent.parentattr=attr
    def getattr(self):
        print "parent attribute:", parent.parentattr
class child(parent):
    def __init__(self):
        print "print child class constructor"
    def childmetho(self):
        print "child method"
p=parent()
p.parentmethod()
p.setattr(200)
p.getattr()
c=child()
c.parentmethod()
c.setattr(300)
c.getattr()


#output
#calling parent class constructor
#calling parent method
#parent attribute: 200
#print child class constructor
#calling parent method
#parent attribute: 300
