from hashlib import md5

def is_valid(door_ID, integer_index):
    md5_checksum = md5("%s%d" % (door_ID, integer_index)).hexdigest()
    return int(md5_checksum, 16) >> 108 == 0

def find_five_leading_zeros(door_ID, integer_index=0):
    while not is_valid(door_ID, integer_index):
        integer_index += 1
    return md5("%s%d" % (door_ID, integer_index)).hexdigest()[5], (integer_index + 1)

if __name__ == '__main__':
    door_ID = "wtnhxymk"
    #door_ID = "abc"
    password = ""
    index = 0
    while len(password) < 8:
        key, index = find_five_leading_zeros(door_ID, index)
        password += str(key)
    print ("The password to the door with ID %s is: %s" % (door_ID, password))
