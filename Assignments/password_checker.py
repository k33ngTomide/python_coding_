import re

def password_validator() -> str:

    password = input("Enter a password: ")
    if re.fullmatch("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password):
        return f"Your password is entered as {password}"
    print("Password must contain atleast one uppercase, "
          "one lowercase, one number and one character"
          "\nTry again.")
    password_validator()

if __name__ == '__main__':
    password_validator()


