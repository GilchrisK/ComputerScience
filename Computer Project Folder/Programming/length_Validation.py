import re

def validate_phone_number(regex, phone_number):
    match = re.search(regex, phone_number)
    if match:
        return True
    return False

# country_code_regex = "(\+\d{1,3})?"
# area_code_regex = "\(?\d{1,4}\)?"
# local_number_regex = "\d{3}[\s.-]?\d{4}"

# pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}") #we compile the data so we can make it a whole object. Makes it easier to use
# pattern = re.compile("\d") # This would pass true is there is even a single number in test_phone_numbers (even if there is a letter)
pattern = re.compile("d\{3}.hello") # This would pass true if there is just one or more of the letters that is inside the square brackets
test_phone_numbers = [
    "+1 (555) 123-4567",
    "555-123-4567",
    "555 123 4567",
    "+44 (0) 20 1234 5678",
    "02012345678",
    "4390872398057839247@gmail.co.uk90587432098574387d5",
    "d",
    "367.hello",
    "invaaaaaaaaalid phone number"
]

for number in test_phone_numbers:
    print(f"{number}: {validate_phone_number(pattern, number)}")






