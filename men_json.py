def remove_unwanted(str):
    s = str.strip()
    s = s.strip("#")
    return s


def to_upper(first, last):
    return remove_unwanted(first.upper()) + " " + remove_unwanted(last.upper())


def LorU(num):
    n = int(num)
    if n < 40:
        return "lower"
    elif n > 40:
        return "upper"
    else:
        return "="


def return_string(this_json):
    return "Hello {0}, \n The answer is {1} {2} then 40".format \
        (to_upper(this_json["first_name"],
                  this_json["last_name"]),
         remove_unwanted(this_json["the_answer"]),
         LorU(remove_unwanted(this_json["the_answer"])))
