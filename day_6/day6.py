class DecodeRepetition:

    def __init__(self, data):
        self.data = data

    def __call__(self):
        occurences = self._find_occurences(len(self.data[0]))
        return self._generate_message(occurences)

    def _find_occurences(self, length):
        occurences = [[0]*26]*length
        for signal in self.data:
            for i, letter in enumerate(signal):
                occurences[i][ord(letter) - 97] += 1
        return occurences

    def _generate_message(self, occurences):
        pass


def read_data(filename):
    """Read all data from filename and use split to create a list.

    Input:
        filename:                   The filename of the input data file.

    Returns:
        list:                       A list with all the data. The elements are
                                    separated strings in the original file.
    """
    with open(filename, 'r') as f:
        return f.read().split()

if __name__ == '__main__':
    data = read_data("day6_example_input.dat")
