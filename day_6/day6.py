
def read_data(filename):
    with open(filename, 'r') as f:
        return f.read().split()

if __name__ == '__main__':
    data = read_data("day6_example_input.dat")
