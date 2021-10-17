email = input("Enter your email: ")

user_name_and_domain = email.split("@")

print("Your Username is '{}', and your Domain name is '{}'".format(user_name_and_domain[0], user_name_and_domain[1]))