def main():
    user_name = get_name()
    loop_name(user_name)


def loop_name(user_name):
    for i in range(len(user_name)):
        if i % 2 == 0:
            continue
        else:
            print(user_name[i])


def get_name():
    while True:
        user_name = input("Enter your name: ")
        if user_name.isalpha():
            break
        else:
            continue
    return user_name


if __name__ == '__main__':
    main()