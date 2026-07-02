class addition:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def adding(self):
        c=self.a+self.b
        print(c)
        return c
    def sub(self):
        c=self.a-self.b
        print(c)
        return c

    def multiply(self):
        c=self.a*self.b
        print(c)
        return c

    def divide(self):
        c=self.a/self.b
        print(c)
        return c

addition_obj=addition(10,5)
print(addition_obj.adding())

print(addition_obj.sub())

print(addition_obj.multiply())

print(addition_obj.divide())