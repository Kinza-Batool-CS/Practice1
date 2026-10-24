class point:
    def __init__(self , x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return point(self.x+other.x , self.y+other.y)
    def __eq__(self ,other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"
p=point(1,2) +point(3,4)

print(p)
print(p==point(4,6) , p==point(0,0))


    