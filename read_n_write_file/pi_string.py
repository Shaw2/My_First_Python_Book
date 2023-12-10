# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# print(pi_string)
# print(len(pi_string))

###===================================

filename = '../ehmatthes-pcc_2e-078318e/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines :
    pi_string += line.strip()

print(f'{pi_string[:52]}...')
print(len(pi_string))

birthday = '940111'

if birthday in pi_string:
    print("Oh, my birthday is in the pi number")