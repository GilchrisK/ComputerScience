from validate_email import validate_email

def validate_studentEmail():

    is_valid = validate_email("GilchrisKakanou1@gmail.com",verify=True)

    if is_valid:
        print("Valid email")
    else:
        print("Not a valid email")
validate_studentEmail()


