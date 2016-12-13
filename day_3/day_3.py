
class Triangle:

    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return self.valid_triangle(self.sides)

    def valid_triangle(self, sides):
        for i in range(3):
            side = sides.pop()
            if side >= sum(sides):
                return False
            sides.insert(0, side)
        return True

if __name__ == '__main__':
    with open('day3_input.dat', 'r') as f:
        triangles = [Triangle(map(int, line.split())) for line in f]
    counter = 0
    for triangle in triangles:
        counter += triangle()
    print ("The number of valid triangles is: %d" % (counter))
