class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vektor ({self.x}, {self.y})"
    
    def __add__(self, other):
        x = self.x

    if __name__ == "__main__":
        v1 = Vector(1,2)
        v2 = Vector(3,4)

        v3 = v1 + v2
        print(v3)

        v4 = v1 * 3
        print(v4)
