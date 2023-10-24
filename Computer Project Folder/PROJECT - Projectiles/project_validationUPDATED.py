# from validate_email import validate_email
def isValidUsername(username):

    if len(username) > 4 and len(username) < 15:
        return True
    else:
        return False

# def isValidPassword(password):
#
#     if len(password) > 5 and len(password) < 15:
#
#         lowerCase = False
#         upperCase = False
#         number = False
#         specialChar = False
#
#         for character in password:
#             if character.isdigit():
#                 number = True
#             if character.islower():
#                 lowerCase = True
#             if character.isupper():
#                 upperCase = True
#             if not character.isalnum():
#                 specialChar = True
#
#         return lowerCase and upperCase and number and specialChar #for an and statement to be true, all these variables msut be true
#
#     else:
#         return False




# def validate_studentEmail(email):
#     is_valid = validate_email("GilchrisKakanou1@gmail.com", verify=True)
#     if is_valid:
#         return True
#     else:
#         return False


def isValidPassword(password):

    if len(password) > 5 and len(password) < 15:

        lowerCase = False
        upperCase = False
        number = False
        specialChar = False

        for character in password:
            if character.isdigit():
                number = True
            if character.islower():
                lowerCase = True
            if character.isupper():
                upperCase = True
            if not character.isalnum():
                specialChar = True

        return lowerCase and upperCase and number and specialChar #for an and statement to be true, all these variables msut be true

    else:
        return False

if __name__ == '__main__':
    from project_tkinterLogin_starterWindow2 import c
    passwordInput = c
    print(isValidPassword(passwordInput))

    from project_tkinterLogin_starterWindow2 import b
    usernameInput = b
    print(isValidUsername(usernameInput))

    # from project_tkinterLogin_starterWindow2 import a
    # emailInput = a




# if __name__ == '__main__':
#     studentUsername = "Mark"
#     print(isValidUsername(studentUsername))
#
#     passwordInput = "Hello1!"
#     print(isValidPassword(passwordInput))
#
#     is_valid = validate_email("GilchrisKakanou1@gmail.com", verify=True)
#     print(validate_studentEmail(is_valid))