conversion_basics = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}
while True:
    decimal_value = 0

    roman_num = input("Enter any Roman numeral: ")

    if roman_num == 'q':
        break
    
    for i in range(len(roman_num) - 1):
        if conversion_basics[roman_num[i]] < conversion_basics[roman_num[i+1]]:
            decimal_value -= conversion_basics[roman_num[i]]
        else:
            decimal_value += conversion_basics[roman_num[i]]

    decimal_value += conversion_basics[roman_num[-1]]

    print(decimal_value)