def my_sort(lst, ascending = True):
    """
    A Function used to sort a list, either in ascending order or descending order.

    >>>my_sort([2, 4, 6, 3, 1])
    >>>[1, 2, 3, 4, 6]

    >>>my_sort([2, 4, 6, 3, 1], 0) #Provide an argument 0 to sort in descending order
    >>>[6, 4, 3, 2, 1]
    """


    type_err = False
    data_type = str(type(lst[0]))

    for i in lst:
        if str(type(i)) != data_type:
            type_err = True

    while True:
        if not type_err:
            for i in range(len(lst)):
                for j in range(len(lst)-1):
                    if ascending:
                        if lst[j] > lst[j+1]:
                            temp = lst[j]
                            lst[j] = lst[j+1]
                            lst[j+1] = temp
                    else:
                        if lst[j] < lst[j+1]:
                            temp = lst[j]
                            lst[j] = lst[j+1]
                            lst[j+1] = temp

        else:
            print("Provide a list of common data types...")
            break
        
        
        print(lst)
        break


my_sort([2, 4, 6, 3, 1], 0)