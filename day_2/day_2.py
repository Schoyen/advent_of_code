
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

    def __call__(self, direction, press=False):
        allowed_directions = self.find_allowed_directions(self.position)
        self.position = allowed_directions[direction]
        if press:
            self.append_code(self.position)
        return self.position

    def append_code(self, position):
        self.code.append(str(position))

    def find_allowed_directions(self, current_position):
        row = (current_position - 1) // 3
        column = (current_position - 1) % 3
        directions = {'U': current_position - 3 if row > 0 else current_position,
                      'R': current_position + 1 if column < 2 else current_position,
                      'L': current_position - 1 if column > 0 else current_position,
                      'D': current_position + 3 if row < 2 else current_position}
        return directions

class ExtendedKeypad(Keypad):
    """Object simulating a keypad with layout as shown below.

               |    1    |
               |  2 3 4  |
               |5 6 7 8 9|
               |  A B C  |
               |    D    |

    This class is a subclass of the Keypad-class.
    """
    def __init__(self, start_position=5):
        Keypad.__init__(self, start_position)
        self.alpha = ['A', 'B', 'C', 'D']
        self.directions = {1: {'D': 2},
                           2: {'R': 1, 'D': 4},
                           3: {'U': -2, 'R': 1, 'L': -1, 'D': 4},
                           4: {'L': -1, 'D': 4},
                           5: {'R': 1},
                           6: {'U': -4, 'R': 1, 'L': -1, 'D': 4},
                           7: {'U': -4, 'R': 1, 'L': -1, 'D': 4},
                           8: {'U': -4, 'R': 1, 'L': -1, 'D': 4},
                           9: {'L': -1},
                           10: {'U': -4, 'R': 1},
                           11: {'U': -4, 'R': 1, 'L': -1, 'D': 2},
                           12: {'U': -4, 'L': -1},
                           13: {'U': -2}}

    def find_allowed_directions(self, current_position):
        directions = {i: current_position for i in ['U', 'R', 'L', 'D']}
        for key in self.directions[current_position]:
            directions[key] += self.directions[current_position][key]
        return directions

    def append_code(self, position):
        if position > 9:
            position = self.alpha[position % 10]
        self.code.append(str(position))

def find_code(instructions, keypad=Keypad):
    key = keypad()
    for instruction in instructions:
        for command in instruction[:-1]:
            key(command)
        key(instruction[-1], press=True)
    return key.code


if __name__ == '__main__':
    with open('day2_input.dat', 'r') as f:
        instruction_sequence = f.read().split()

    key_1 = find_code(instruction_sequence)
    key_2 = find_code(instruction_sequence, keypad=ExtendedKeypad)
    print ("The code to the bathroom (for part 1) is: %s" % (''.join(key_1)))
    print ("The code to the bathroom (for part 2) is: %s" % (''.join(key_2)))
