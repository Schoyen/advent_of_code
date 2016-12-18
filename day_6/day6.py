class DecodeRepetition:
    """Object used for decoding a simple repetition signal.
    """

    def __init__(self, data):
        """Constructor storing the data to decode.

        Input:
            data:                       A list with strings containing the
                                        repetition signal.
        """
        self.data = data

    def __call__(self, criteria=max):
        """Call-method calling appropriate methods in order to decode the signal.

        Input:
            criteria:                   The method used to decode the signal.

        Returns:
            str:                        The decoded message.
        """
        columns = self._separate_columns(max(map(len, self.data)))
        occurences = []
        for i in range(len(columns)):
            occurences.append(self._find_occurence(columns[i]))
        return self._generate_message(occurences, criteria=criteria)

    def _separate_columns(self, length):
        """Private method used to read data column-wise and store in this in a
        list.

        Input:
            length:                     The length of the longest string in
                                        self.data.

        Returns:
            columns:                    A list of strings containing the
                                        "vertical" characters in self.data.
        """
        columns = ['']*length
        for signal in self.data:
            for i, char in enumerate(signal):
                columns[i] += char
        return columns

    def _find_occurence(self, column):
        """Private method used to count the occurences of the characters in the
        string column.

        Input:
            column:                     A string containing lower-case
                                        characters.

        Returns:
            occurece:                   A list where the index corresponds to a
                                        character and the elements are the
                                        number of occurences of each character.
        """
        occurence = [0]*26
        for letter in column:
            occurence[ord(letter) - 97] += 1
        return occurence

    def _generate_message(self, occurences, criteria=max):
        """Private method used to generate the decoded message.

        Input:
            occurences:                 A list of lists containing the number of
                                        occurences of each character in
                                        self.data.
            criteria:                   The method used to decode the signal.

        Returns:
            message:                    The decoded string.
        """
        message = ''
        for occurence in occurences:
            message += chr(occurence.index(criteria(occurence)) + 97)
        return message


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
    data = read_data("day6_input.dat")
    DR = DecodeRepetition(data)
    print ("The decoded signal for part 1 is: %s" % DR())
    print ("The decoded signal for part 2 is: %s" % DR(criteria=min))
