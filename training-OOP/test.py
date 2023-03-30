from functools import reduce
class Math:
    
    def __init__(self, number):
       self.number = number
    
    def get_factorial(self): 
        fact = 1 
        a = self.number 
        while a > 1: 
            fact *= a 
            a -= 1 
        return fact
    
    def get_sum(self): 
        x = sum([int(y) for y in str(self.number)]) 
        return x

    def get_mul_table(self):
        for x in range(0, 11):
            res = (f'{self.number} * {x} = {self.number*x}')
            return res

n1 = Math(12)
print(n1.get_factorial())
print(n1.get_sum())
print(n1.get_mul_table())

