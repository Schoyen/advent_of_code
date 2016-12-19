
class Display:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = [['.']*self.width]*self.height

    def __call__(self, command, A, B):
        function = getattr(self, command, None)
        self.screen = function(A, B) if isinstance(function, callable) else self.screen

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.screen])

if __name__ == '__main__':
    with open('day8_input.dat', 'r') as f:
        data = [line.rstrip('\n') for line in f]

    display = Display(50, 6)
    print (display)
