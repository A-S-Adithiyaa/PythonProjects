def converter(number):
    temp_units = {
        1 : str(round((number * 9 / 5) + 32, 3)) + " F", 
        2 : str(round((number - 32) * 5 / 9, 3)) + " C", 
        3 : str(round(number + 273.15, 3)) + " K", 
        4 : str(round(number - 273.15, 3)) + " C", 
        5 : str(round((number - 273.15) * 9/5 + 32, 3)) + " F", 
        6 : str(round((number - 32) * 5/9 + 273.15, 3)) + " K", 
        7 : str(number * 2.54) + " cm" , 
        8 : str(number * 0.393701) + " in", 
        9 : str(number * 0.3048) + " m", 
        10 : str(number * 3.28084) + " ft", 
        11 : str(number * 0.9144) + " m", 
        12 : str(number * 1.09361) + " yd", 
        13 : str(number * 1.60934) + " km", 
        14 : str(number * 0.621371) + " mile", 
        15 : str(number * 4046.86) + " m-square", 
        16 : str(number * 0.000247105) + " acre", 
        17 : str(number * 3.6) + " km/s", 
        18 : str(number * 0.277778) + " m/s", 
        19 : str(number * 0.453592) + " kg", 
        20 : str(number * 2.20462) + " lb", 
        21 : str(number * 101325) + " Pa", 
        22 : str(number / 101325) + " atm", 
        23 : str(number * 133.322) + " Pa", 
        24 : str(number * 0.00750062) + " mmHg", 
        25 : str(number * 0.7457) + " kW", 
        26 : str(number * 1.34102) + " hp", 
        27 : str(number * 0.239006) + " cal", 
        28 : str(number * 4.184) + " J"}

    print("Welcome to the conversion program.")
    print("You are supposed to choose a conversion number from the below table.")
    print('''
        No.\tConversion Name

        01\tC - F
        02\tF - C
        03\tC - K
        04\tK - C
        05\tK - F
        06\tF - K
        07\tin - cm
        08\tcm - in
        09\tft - m
        10\tm - ft
        11\tyd - m
        12\tm - yd
        13\tmile - km
        14\tkm - mile
        15\tacre - m^2
        16\tm^2 - acre
        17\tm/s - km/s
        18\tkm/s - m/s
        19\tlb - kg
        20\tkg - lb
        21\tatm - Pa
        22\tPa - atm
        23\tmmHg - Pa
        24\tPa - mmHg
        25\thp - kW
        26\tkW - hp
        27\tJ - cal
        28\tcal - J
        ''')

    conv_no = int(input("Enter the conversion number : "))
    final_no = temp_units[conv_no]

    print(final_no)

converter(100)