"""
lower = 10
upper = 100
print("Enter a number ({}-{})".format(lower,upper))
for i in range(10, 120, 11):
          print("{} {}".format(i, chr(i)))
"""


def get_number():
    while True:
        try:
            upper_number = int(input("Enter a number: "))
        except ValueError:
            print("invalid integer")
            continue
        else:
            return upper_number


number = 'number'
character = 'Char'
print("{:^8s}".format(number, character))
for i in range(0, get_number()):
    print("{:^8d} {:^8s}".format(i, chr(i)))