class EasterBunnyMap:

    def __init__(self, directions):
        self.directions = directions
        self.allowed_directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        self.allowed_directions_keys = ['N', 'E', 'S', 'W']
        self.current_direction = 'N'
        self.current_position = [[0, 0]]

    def do_step(self, direction, steps):
        rotation = 1 if direction == 'R' else -1
        self.current_direction = self.allowed_directions_keys[(self.allowed_directions_keys.index(self.current_direction) + rotation) % 4]
        movement = self.allowed_directions[self.current_direction]
        for step in range(steps):
            self.current_position.append([movement[0] + self.current_position[-1][0], movement[1] + self.current_position[-1][1]])

    def walk_the_walk(self):
        for direction in self.directions:
            self.do_step(direction[0], int(direction[1:]))

    def find_crossing(self):
        crossing = []
        for position in self.current_position:
            crossing.append(position)
            if position in crossing[:-1]:
                break
        return crossing[-1]

if __name__ == '__main__':
    with open('day1_input.dat', 'r') as f:
        directions = f.read().replace(',','').split()

    ebm = EasterBunnyMap(directions)
    ebm.walk_the_walk()
    print ("Steps from Easter Bunny Headquarters: %d" % (abs(ebm.current_position[-1][0]) + abs(ebm.current_position[-1][1])))
    crossing = ebm.find_crossing()
    print ("Steps from first crossing: %d" % (abs(crossing[0]) + abs(crossing[1])))
