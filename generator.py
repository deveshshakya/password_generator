import random

chars = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+{}|[]\;:,./<>?-'"
password = ''

num = int(input('Enter Number of Password: '))
length = int(input('Enter Length (Minimum 8 Characters): '))
if length < 8:
    raise ValueError('Entered length should be equal or greater than 8.')

for i in range(1, num + 1):
    for _ in range(length):
        password += random.choice(chars)
    print(str(i) + ' -> ' + password)
    password = ''