
def determine_ABBA_(ipv7_address):
    pass

def _determine_symmetric_string(string):
    if len(string) < 4:
        return False

    for i in range(len(string) - 3):
        if string[i] != string[i+1] and string[i] == string[i+3] and string[i+1] == string[i+2]:
            return True

    return False

if __name__ == '__main__':
    with open('day7_input.dat', 'r') as f:
        data = f.read().split()
