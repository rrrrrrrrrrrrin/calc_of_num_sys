def to_decimal(new_num, system, num):
    for index, i in enumerate(num[::-1]):
        i = ord(i) - 55 if not i.isdigit() else int(i)
        new_num += i * system ** index
    print(new_num)


def from_decimal(new_num, system_num, num):
    while num >= 1:
        remainder = num % system_num
        new_num.append(chr(remainder + 55)) if remainder >= 10 else new_num.append(remainder)
        num //= system_num
    print(*new_num[::-1], sep='')


system = int(input('Enter a numeral system you need to translate from: '))

if not system == 10:
    new_num = 0
    to_decimal(new_num, system, input('Enter a number to translate to the decimal numeral system: '))
else:
    new_num = []
    system_num = int(input('Enter a numeral system you need to translate to: '))
    from_decimal(new_num, system_num, int(input(f'Enter a number to translate to the "{system_num}" numeral system: ')))

# if indeed, a user can translate, for example, a number from the binary numeral system to the hexadecimal one
# by calculating its value in a decimal state first
