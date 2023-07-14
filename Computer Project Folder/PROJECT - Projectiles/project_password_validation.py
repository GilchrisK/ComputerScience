
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
    from project_tkinterlogin2 import c
    passwordInput = c
    print(isValidPassword(passwordInput))