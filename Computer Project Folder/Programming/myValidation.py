#########################################################
# Name: myValidation
# Purpose of this module: Validation of 4 different functions
# Bugs: None
# Notes: UNFINISHED
# Date: 04/05/23
##########################################################

def is_Valid_Length(text, length,switch): # Length Validation

    match switch:
        case 0:
            if len(str(text)) == length:
                return True
            else:
                return False

        case 1:
            if len(str(text)) >= length:
                return True
            else:
                return False

        case 2:
            if len(str(text)) <= length:
                return True
            else:
                return False



def is_Date_Format():

    pass

def is_Email():

    pass

def is_Range():

    pass




if __name__ == '__main__':
    if is_Valid_Length("Gilchris",5,2):     #the last parameter is the SWITCH which passes the Case that will be used
        print("Valid")
    else:
        print("Invalid")






