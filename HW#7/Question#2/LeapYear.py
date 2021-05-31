def leap_year(year):
    if (year.isdigit() == False):
        return "Invalid input"
    else:
        if ( int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0):
            return year + " is a leap year"

print(leap_year("2000"))