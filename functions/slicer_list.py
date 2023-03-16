# instead of numbers we can pass a list but (*) should removed.

def slicer_list(num):
    list_even = list()
    list_odd = list()
    for i in num:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)    
    print('even numbers :', list_even)
    print('odd numbers ', list_odd)
    
num_list = list(range(45))
slicer_list(num_list)