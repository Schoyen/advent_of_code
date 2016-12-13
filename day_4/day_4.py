def is_valid_room(name, checksum):
    occurences = [0]*26
    for letter in name:
        if ord(letter) != 45:
            occurences[ord(letter) - 97] += 1

    for check in checksum:
        index = occurences.index(max(occurences))
        occurences[index] = -1
        next_check = chr(index + 97)
        if check != next_check:
            return False
    return True

def decrypt_name(name, sector):
    decrypted_name = ''
    rotation = sector % 26
    for letter in name:
        if letter == '-':
            decrypted_name += ' '
        else:
            decrypted_name += chr(((ord(letter) + rotation) % 97) % 26 + 97)
    return decrypted_name


def separate_encryption(encrypted_string):
    name, number, checksum = '', '', ''

    for letter in encrypted_string[:-11]:
        name += letter
    for num in encrypted_string[-10:-7]:
        number += num
    for check in encrypted_string[-6:-1]:
        checksum += check

    return name, int(number), checksum

if __name__ == '__main__':
    with open('day4_input.dat', 'r') as f:
        encrypted_rooms = [line.rstrip('\n')for line in f]

    sector_sum = 0
    decrypted_names = []
    for room in encrypted_rooms:
        name, number, checksum = separate_encryption(room)
        if is_valid_room(name, checksum):
            sector_sum += number
        decrypted_names.append(decrypt_name(name, number))
        print ("%s (%d)" % (decrypted_names[-1], number))

    print ("The sum of the sectors for real rooms is: %d" % sector_sum)
