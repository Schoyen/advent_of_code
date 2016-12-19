
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
        pass

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.screen])

if __name__ == '__main__':
    with open('day8_input.dat', 'r') as f:
        data = [line.rstrip('\n') for line in f]

    display = Display(50, 6)
