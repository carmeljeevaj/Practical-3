while True:
    user_name=input("Enter your name: ")
    if user_name.isalpha():
        break
    else:
        continue
for i in range(len(user_name)):
    if i%2==0:
        continue
    else:
        print(user_name[i])

