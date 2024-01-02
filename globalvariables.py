r = 10
pi = 3.14


def circle_area():
    global r
    # to manipulate global var inside any function
    # we have to use global keyword with var name
    r = r * r
    cArea = pi * r
    return cArea


area = circle_area()
print(area)
