# this function has logical error,
# to read about Leap year go to   https://www.mathsisfun.com/leap-years.html

def IsLeap(Year):
    # Year is an integer
    Year = int(Year)
    if Year <=0:
        print("Years cannot have zero or negative values")
        print("this is not a leap year")
        exit()
    if (Year % 100 ==0 and Year % 400 == 0) or (Year % 100 and Year % 4 ==0):
            print("this is a leap year")
    else:
        print("this is not a Leap Year")

TestYear = input("Enter Year and I will check it if it is leap or not... ")
IsLeap(TestYear)
