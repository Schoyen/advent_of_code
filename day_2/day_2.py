
class Keypad:
    """Object simulating a keypad with layout as shown below.

               |1 2 3|
               |4 5 6|
               |7 8 9|

    The class contains variables to show the current button we are pointing at
    and methods for moving to a different button and storing the code sequence.
    """

    def __init__(self, start_position=5):
        self.position = start_position
        self.code = []
        self.direction_value = {'U': 3, 'R': 1, 'L': -1, 'D': -3}
        self.keypad = [1, 2, 3,
                       4, 5, 6,
                       7, 8, 9]

    def __call__(self, direction, press=False):
        allowed_directions = self.find_allowed_directions(self.position)
        position = self.position + self.direction_value[direction]
        if position < 1 or position > 9:
            position = self.position

    def find_allowed_directions(self, current_position):
        directions = {}
        index = self.keypad.index(current_position)

if __name__ == '__main__':
    with open('day2_input.dat', 'r') as f:
        instruction_sequence = f.read()
    key = Keypad()
    key.find_allowed_directions(8)
