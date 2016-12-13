
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
            self.code.append(str(self.position))
        return self.position

    def find_allowed_directions(self, current_position):
        row = (current_position - 1) // 3
        column = (current_position - 1) % 3
        directions = {'U': current_position - 3 if row > 0 else current_position,
                      'R': current_position + 1 if column < 2 else current_position,
                      'L': current_position - 1 if column > 0 else current_position,
                      'D': current_position + 3 if row < 2 else current_position}
        return directions

def find_code(instructions):
    key = Keypad()
    for instruction in instructions:
        for command in instruction[:-1]:
            key(command)
        key(instruction[-1], press=True)
    return key.code


if __name__ == '__main__':
    with open('day2_input.dat', 'r') as f:
        instruction_sequence = f.read().split()
    print ("The code to the bathroom is: %s" % (''.join(find_code(instruction_sequence))))
