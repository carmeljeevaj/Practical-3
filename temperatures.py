def celsius_to_fahrenheit():
    while True:
        try:
            user_input=float(input("Enter celsius value: "))
        except ValueError:
            print("invalid integer")
            continue
        else:
            return (user_input*9/5)+32

def fahrenheit_to_celsius():
    while True:
        try:
            user_input = float(input("Enter Fahrenheit value: "))
        except ValueError:
            print("invalid integer")
            continue
        else:
            return (user_input - 32) * 5/9
def main():
    while True:
        try:
            user_input=int(input("Press 0 for celsius conversion and 1 for fahrenheit conversion: "))
        except ValueError:
            print("invalid integer")
            continue
        if user_input ==0:
            Celsius_to_fahrenheiTT=celsius_to_fahrenheit()
            print(Celsius_to_fahrenheiTT,"F")

            break
        elif user_input == 1:
            fahrenheit_to_celsiuSS=fahrenheit_to_celsius()
            print(fahrenheit_to_celsiuSS,"C")
            break
        else:
            continue

main()