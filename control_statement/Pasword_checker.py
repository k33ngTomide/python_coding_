if __name__ == '__main__':
    print("This is pycharm")
user_password = input("Enter your password:  ")
password = len(user_password)

while password < 8:
    user_password = input("Enter your password:  ")

print("Your password is Secure, the length is ", password)
