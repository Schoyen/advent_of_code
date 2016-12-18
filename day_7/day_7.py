import re

def determine_ABBA(addresses):
    return sum([_determine_ABBA(address) for address in addresses])

def _determine_ABBA(ipv7_address):
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

def test_example_values():
    example_data = [
            "abba[mnop]qrst",
            "abcd[bddb]xyyx",
            "aaaa[qwer]tyui",
            "ioxxoj[asdfgh]zxcvbn"
            ]
    expected_result = [
            True,
            False,
            False,
            True
            ]

    for expected, data in zip(expected_result, example_data):
        assert expected == _determine_ABBA(data)

    assert sum(expected_result) == determine_ABBA(example_data)

def test_example_values_2():
    example_data = ["aba[bab]xyz", "xyx[xyx]xyx", "aaa[kek]eke", "zazbz[bzb]cdb"]
    assert 3 == determine_SSL(example_data)

def determine_SSL(addresses):
    counter = 0
    for address in addresses:
        hypernet, supernet = _separate_super_hyper(address)
        counter += is_SSL_compatible(hypernet, supernet)
    return counter

def _separate_super_hyper(address):
    return re.findall('(?<=\[)\w+(?=\])', address), re.findall('\w+(?=\[|$)', address)

def is_SSL_compatible(hypernet, supernet):
    hyper_BAB = []
    for string in hypernet:
        hyper_BAB.extend(find_ABA(string))

    super_ABA = []
    for string in supernet:
        super_ABA.extend(find_ABA(string))

    for ABA in super_ABA:
        if ABA[1] + ABA[0] + ABA[1] in hyper_BAB:
            return True
    return False

def find_ABA(string):
    match = []

    if len(string) < 3:
        return match

    for i in range(len(string) - 2):
        if string[i] == string[i+2] and string[i] != string[i+1]:
            match.append(string[i] + string[i+1] + string[i+2])
    return match

if __name__ == '__main__':
    with open('day7_input.dat', 'r') as f:
        data = f.read().split()
    print ("The number of IPv7-addresses that support TLS is: %d" % determine_ABBA(data))
    print ("The number of IPv7-addresses that support SSL is: %d" % determine_SSL(data))
