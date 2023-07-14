def isValidUsername(username):

    if len(username) > 4 and len(username) < 15:
        return True
    else:
        return False

if __name__ == '__main__':
    studentUsername = "Mark"
    print(isValidUsername(studentUsername))