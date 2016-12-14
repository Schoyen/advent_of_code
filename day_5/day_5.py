from hashlib import md5

def is_valid(door_ID, integer_index):
    md5_checksum = md5("%s%d" % (door_ID, integer_index)).hexdigest()
    return int(md5_checksum, 16) >> 108 == 0

def find_five_leading_zeros(door_ID, integer_index=0):
    while not is_valid(door_ID, integer_index):
        integer_index += 1
    return md5("%s%d" % (door_ID, integer_index)).hexdigest(), (integer_index + 1)

if __name__ == '__main__':
    door_ID = "wtnhxymk"
    #door_ID = "abc"
    #password = ""
    password_list = ['_']*8
    index = 0
    while '_' in password_list:
        key, index = find_five_leading_zeros(door_ID, index)
        if 0 <= int(key[5], base=16) <= 7 and '_' == password_list[int(key[5], base=16)]:
            print ("Found key %s at index %d" % (key, index - 1))
            password_list[int(key[5], base=16)] = str(key[6])
    print ("The password to the door with ID %s is: %s" % (door_ID, ''.join(password_list)))
#    while len(password) < 8:
#        key, index = find_five_leading_zeros(door_ID, index)
#        password += str(key[5])
#    print ("The password to the door with ID %s is: %s" % (door_ID, password))
