class BasicMath:
    
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a * b
    
if __name__ == "__main__":
    print ("BasicMath | Add Operation {a} + {b} = {res}".format(a = 5,b = 5, res = BasicMath().add(5,5)))
    print ("BasicMath | Subtract Operation {a} - {b} = {res}".format(a = 5,b = 5,res = BasicMath().sub(5,5)))
    print ("BasicMath | Multiply Operation {a} * {b} = {res}".format(a = 5,b = 5,res = BasicMath().mult(5,5)))
    print ("BasicMath | Divide Operation {a} / {b} = {res}".format(a = 5,b = 5,res = BasicMath().div(5,5))) 


