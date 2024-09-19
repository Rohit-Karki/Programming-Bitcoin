class FieldElement:
    
    def __init__(self, number, prime):
        if number <= prime - 1 and number >= 0:
            self.number = number
            self.prime = prime
        else:
            error = 'Num {} not in field range 0 to {}'.format(
            number, prime - 1)
            raise ValueError(error)
        
    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.number)
        
    def __eq__(self, other):
        if other is None:
            return False
        else: 
            return self.number == other.number and self.prime == other.prime
    
    def __ne__(self, other: object) -> bool:
        if other is None:
            return False
        else:
            return self.number != other.number and self.prime != other.prime
        
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)
        
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)
    
    def __mul__(self, other):
        if self.prime != other.prime:
            return TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num,self.prime)
    
    def __pow__(self, exponent):
        num = pow(self.num, exponent, self.prime)
        return self.__class__(num, self.prime)
    
            