"""
Point Addition
Elliptic curves are useful because of something called point addition. Point addition is
where we can do an operation on two of the points on the curve and get a third point,
also on the curve. This is called addition because the operation has a lot of the intuitions
we associate with the mathematical operation of addition. For example, point
addition is commutative. That is, adding point A to point B is the same as adding
point B to point A.

We can define point addition using the fact that lines intersect one or three times with
the elliptic curve. Two points define a line, so since that line must intersect the curve
one more time, that third point reflected over the x-axis is the result of the point
addition.

So, for any two points P1 = (x1,y1) and P2 = (x2,y2), we get P1 + P2 as follows:
    • Find the point intersecting the elliptic curve a third time by drawing a line through P1 and P2
    • Reflect the resulting point over the x-axis
    
We first draw a line through the two points we’re adding (A and B). The third inter‐
section point is C. We then reflect that point over the x-axis, which puts us at the A + B point in Figure 2-14.
One of the properties that we are going to use is that point addition is not easily predictable. 
We can calculate point addition easily enough with a formula, but intuitively,
the result of point addition can be almost anywhere given two points on the curve.
Going back to Figure 2-14, A + B is to the right of both points, A + C would be somewhere
between A and C on the x-axis, and B + C would be to the left of both points.
In mathematics parlance, point addition is nonlinear.
"""

class Point:
    def __call__(self, x,y,a,b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b
            
    def __ne__(self, other: object) -> bool:
        return self.x != other.x or self.y != other.y \
            or self.a != other.a or self.b != other.b
            
    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format
                (self, other))
        
        #  other.x being None means that other is the point at infinity, or the additive identity. Thus, we return self
        if other is None:
            return self 
        # self.x being None means that self is the point at infinity, or the additive identity. Thus, we return other.
        if self is None:
            return other
        
        if self.x == other.x and self.y != other.y:
            # Vertical Line returns the point at infinity
            return self.__class__(None, None, self.a, self.b)
        
        if self.x != other.x:
            slope = (other.y - self.y) / (other.x - self.x)
            x3 = slope ** 2 -self.x - other.x
            y3 = slope * (self.x-x3) - self.y
            
            return self.__class__(x3, y3, self.a, self.b)
        
        if self == other:
            slope = (3 * self.x + self.a) / (2 * self.y)
            x3 = slope**2 - 2 * self.x
            y3 = slope * (self.x-x3) - self.y
            return self.__class__(x3,y3, self.a, self.b)
        
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)
    