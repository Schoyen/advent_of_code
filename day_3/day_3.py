
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

def count_triangles(triangles):
    counter = 0
    for triangle in triangles:
        counter += triangle()
    return counter

if __name__ == '__main__':
    with open('day3_input.dat', 'r') as f:
        triangles = [Triangle(map(int, line.split())) for line in f]

    print ("The number of valid triangles is: %d" % (count_triangles(triangles)))

    triangles = []
    with open('day3_input.dat', 'r') as f:
        tmp = [[], [], []]
        for line in f:
            side_1, side_2, side_3 = map(int, line.split())
            tmp[0].append(side_1)
            tmp[1].append(side_2)
            tmp[2].append(side_3)
            if len(tmp[0]) % 3 == 0:
                triangles.extend(map(Triangle, tmp))
                tmp = [[], [], []]

    print ("The number of valid triangles is: %d" % (count_triangles(triangles)))
