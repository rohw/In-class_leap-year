def ly(year):
    if type(year) != int:
        return "Input is not integer"

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return("It is a leap year")
            else:
                return("It is not a leap year")
        else:
            return("It is a leap year")
    else:
        return("It is not a leap year")
