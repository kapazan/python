# slice the numbers into even and odd
# (*) allows us to pass as many arguments as wished


def slicer_nums(*num):
    list_even = []
    list_odd = []
    for i in num:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)
    print("odd numbers :", list_odd)
    print("even numbers :", list_even)
slicer_nums(34,3,1,34,2,6,2,39)
