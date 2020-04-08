import string
import random


def get_details():
    first_name = input("Enter your First name: ")
    last_name = input("Enter your last name: ")
    user_email = input("Enter your Email address: ")

    details = [first_name, last_name, user_email]

    return details


def gen_password(user_details):
    characters = string.ascii_letters
    lenght = 5
    random_password = ''.join(random.choice(characters) for i in range(lenght))
    password = str(user_details[0][0:2] + user_details[1][-2:] + random_password)

    return password


status = True
container = []

while status:

    details = get_details()

    password = gen_password(details)
    print("Your password is: " + str(password))

    password_like = input(
        str("Are you satisfied with your password? If yes type Yes, type No to enter a preferred password: "))

    password_loop = True

    while password_loop:

        if password_like == "Yes":
            details.append(password)

            container.append(details)
            break

        else:
            user_password = input(str("Enter your preferred password. Your password should be at least 7 characters: "))

            pass_len = True

            while pass_len:
                if len(user_password) >= 7:
                    details.append(user_password)
                    container.append(details)

                    pass_len = False
                    password_loop = False

                else:
                    print("Your password is less than 7 characters!")
                    user_password = input(str("Enter password of at least 7 characters: "))

    new_user = input(str("Would you like to enter a new user? Yes or No: "))
    if (new_user == "No"):

        status = False
        for items in container:
            print(items)
    else:
        status = True