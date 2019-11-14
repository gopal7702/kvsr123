class kvsr():
    def __init__(self,name):
        self.name=name
        print(self.name)
    def emp(self,name):
        print(name)
class details(kvsr):
    def det(self,a,b):
        print(a,b)
k=details('somu')
k.emp('radhi')
k.det('r','k')



