class myclass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def following(self,user2):
        user2.a+=1
        user2.b+=1
        self.a+=1
        self.b+=1


instance1=myclass(10,12)
print(instance1.a,instance1.b)
instance2=myclass(20,21)
print(instance2.a,instance2.b)
print("after following")
instance1.following(instance2)
print(instance1.a,instance1.b)
print(instance2.a,instance2.b)
