
class Keypad:
    """Object simulating a keypad with layout as shown below.

               |1 2 3|
               |4 5 6|
               |7 8 9|

    The class contains variables to show the current button we are pointing at
    and methods for moving to a different button and storing the code sequence.
    """

    def __init__(self, start_position='5'):
        self.position = start_position
        self.code = []

    def __call__(self, direction, press=False):
        pass

if __name__ == '__main__':
    with open('day2_input.dat', 'r') as f:
        instruction_sequence = f.read()
