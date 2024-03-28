
def isValidUsername(username):

    if len(username) > 4 and len(username) < 15:
        return True
    else:
        return False

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

        return lowerCase and upperCase and number and specialChar # for an and statement to be true,
        # all these variables must be true


    else:
        return False



def validate_studentEmail(email):
    if "@gmail.com" in email or "@outlook.com" in email or \
            "@icloud.com" in email or "@yahoo.com" in email:
        if len(email) > 13 and len(email) < 35:
            lowerCase = False
            upperCase = False

            for character in email:
                if character.islower():
                    lowerCase = True
                if character.isupper():
                    upperCase = True

            return lowerCase and upperCase
        else:
            return False





    #VALIDATE THE EMAIL SO THAT IT IS A CERTAIN RANGE OF LETTERS LONG
    #AND SO THAT IT MUST CONTAIN AN @ IN IT


    # is_valid = validate_email("GilchrisKakanou1@gmail.com", verify=True)
    # if is_valid:
    #     return True
    # else:d
    #     return False


#
# if __name__ == '__main__':
#     studentUsername = "Mark"
#     print(isValidUsername(studentUsername))
#
#     passwordInput = "Hello1!"
#     print(isValidPassword(passwordInput))
#
#     is_valid = validate_email("GilchrisKakanou1@gmail.com", verify=True)
#     print(validate_studentEmail(is_valid))