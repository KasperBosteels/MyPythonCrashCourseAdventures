def get_formatted_name(first, last, middle=""):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

def get_formatted_address(first, last, population= '' ):
    if population:
        full_name = first + ' ' + last + ' with a total of ' + population + ' people.'
    else:
        full_name = first + ' ' + last

    return full_name.title()
