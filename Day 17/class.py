class myclass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self,a,b):
        return a+b
    def mul(self,a,b):
        return a*b
    def optional(self ,*args, **kwargs):
        for ar in args:
            print (ar)
    def compound(self):
        b=self.sum(self.sum(self.sum(self.a,self.b),self.b),self.sum(self.a,self.b))
        c=self.mul(self.mul(self.a,self.b),self.mul(self.mul(self.a,self.b),self.a))
        return b,c
Class=myclass(10,12)
result1,result2=Class.compound()
result3=Class.optional(12,13,14,15,16,17)
print(result1)
print(result2)
