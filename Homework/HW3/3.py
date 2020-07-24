a_size = input('Enter an integer number <between 0 and 30>: ')

print(' ' + '*' * int(a_size) + ' ')

for i in range(int(a_size) - 1):
    print('*' + ' ' * int(a_size) + '*')

print('*' * (int(a_size) + 2))

for i in range(int(a_size)):
    print('*' + ' ' * int(a_size) + '*')