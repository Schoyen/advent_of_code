
class Display:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = [['.' for i in range(self.width)] for j in range(self.height)]

    def __call__(self, command, A, B):
        function = getattr(self, '_'.join(command.split()), None)
        self.screen = function(A, B, self.screen) if function else self.screen

    def rect(self, A, B, screen):
        if A > len(screen[0]) or B > len(screen):
            return screen

        for i in range(B):
            for j in range(A):
                screen[i][j] = '#'

        return screen

    def rotate_row(self, A, B, screen):
        if A > len(screen):
            return screen

        new_screen = [[element if i != A else '.' for element in screen[i]] for i in range(len(screen))]
        for i in range(len(screen[0])):
            new_screen[A][(i + B) % len(screen[0])] = screen[A][i]

        return new_screen

    def rotate_column(self, A, B, screen):
        new_screen = self.rotate_row(A, B, [[screen[j][i] for j in range(self.height)] for i in range(self.width)])
        return [[new_screen[j][i] for j in range(self.width)] for i in range(self.height)]

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.screen])

    def count_pixels(self):
        return sum([sum([element == '#' for element in row]) for row in self.screen])

def split_data_string(data):
    commands = []
    for line in data:

        current_line = line.split()

        if len(current_line) == 2:
            commands.append([current_line[0], split_rect(current_line[1])])
        else:
            commands.append([current_line[0] + ' ' + current_line[1], split_row_col(current_line[2:])])

    return commands

def split_row_col(line):
    return [int(line[0][2:]), int(line[-1])]

def split_rect(line):
    variables = ['', ''] # [A, B]
    index = 0
    for i in line:
        if i == 'x':
            index += 1
            continue
        variables[index] += i
    return map(int, variables)

if __name__ == '__main__':
    with open('day8_input.dat', 'r') as f:
        data = [line.rstrip('\n') for line in f]

    commands = split_data_string(data)
    print (commands)
    display = Display(50, 6)
    for command in commands:
        __import__('os').system('clear')
        display(command[0], *command[1])
        print (display)

    print ("The number of pixels is: %d" % display.count_pixels())
