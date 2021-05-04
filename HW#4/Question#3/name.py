def create_name(first, last):
    if type(first) != str or type(last) != str:
        return "input invalid"
    else:
        name = str(first.capitalize()) + ' ' + str(last.capitalize())
        return name
