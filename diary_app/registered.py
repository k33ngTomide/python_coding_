
def register_user(username, password):
    with open('user_db.txt', 'a') as file:
        file.write(f"{username},{password}\n")


def login_user(username, password):
    with open('user_db.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == password:
                return True
    return False

