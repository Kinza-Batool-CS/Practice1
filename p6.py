class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
      return self.width * self.height

    def perimeter(self):
       return 2 *(self.width+self.height)
    def is_square(self):
       return self.width==self.height

    def __str__(self):
       return f"Rectangle( {self.width} X {self.height})"
r=rectangle(4,6)
print(r , r.area(), r.perimeter(), r.is_square())
r2=rectangle(5,5)
print(r2.is_square())

    
    


