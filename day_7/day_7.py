def determine_ABBA(addresses):
    pass

def _determine_ABBA(ipv7_address):
    import re
    address_sections = re.findall("\w+", ipv7_address)
    success = []
    for i, section in enumerate(address_sections):
        if i & 0x1 == 0: # Even number
            success.append(_determine_symmetric_string(section))
        else:
            if _determine_symmetric_string(section):
                return False
    return True in success

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
