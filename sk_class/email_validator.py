import re


def email_validator(lisf_of_email: list[str]) -> list[str]:

    list_of_invalid = []
    list_of_valid_emails = []
    for email in lisf_of_email:
         if re.search("^[A-Z]*[a-z]+[A-Z]*[a-z]+", email):
             if re.search("[@]", email):
                if re.search("[.]", email):
                    if re.search("[a-z]{2}$", email):
                     list_of_valid_emails.append(email)
                    else:
                     list_of_invalid.append(email)
                else:
                    list_of_invalid.append(email)
             else:
                list_of_invalid.append(email)
         else:
             list_of_invalid.append(email)
    return list_of_valid_emails


if __name__ == '__main__':
    email_list = ["Wechat.com", "Akint@gmail.com", "@@double.Nig", "Ferrari@kit.ng", "Itunu@gmail.com", "sem@semicolon.africa"]
    print(email_validator(email_list))