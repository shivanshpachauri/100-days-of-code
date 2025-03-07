class myclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self, a=None, b=None):
        if a is None:
            a = self.a
        if b is None:
            b = self.b
        return a + b

    def mul(self, a=None, b=None):
        if a is None:
            a = self.a
        if b is None:
            b = self.b
        return a * b

    def compound(self):
        b = self.sum(self.sum(self.sum(self.a, self.b), self.b), self.sum(self.a, self.b))
        c = self.mul(self.mul(self.a, self.b), self.mul(self.mul(self.a, self.b), self.a))
        return b, c

Class = myclass(10, 12)
result1, result2 = Class.compound()
print(result1)
print(result2)

# Using instance variables
result = Class.sum()
print(result)  # Output: 22

# Using provided parameters
result = Class.sum(5, 7)
print(result)  # Output: 12