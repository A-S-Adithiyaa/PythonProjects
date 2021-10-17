while True:
    print("Enter the units next to the number")

    height = input("Enter your HEIGHT: ")
    weight = input("Enter your WEIGHT: ")

    weight_in_units = height_in_units = False

    if weight [-2:] == 'kg':
        weight = float(weight[:-2])
        weight_in_units = True

    elif weight[-5:] == 'pound':
        weight = weight[:-5]
        weight = float(weight) / 2.20462
        weight_in_units = True

    if height[-2:] =='cm':
        height = float(height[:-2])
        height_in_units = True

    elif height[-1:] == 'm':
        height = height[:-1]
        height = float(height) * 100
        height_in_units = True

    elif height[-4:] == 'inch':
        height = height[:-4]
        height = float(height) * 2.54
        height_in_units = True

    elif height[-4:] == 'foot':
        height = height[:-4]
        height = float(height) * 30.48
        height_in_units = True

    if (not weight_in_units) and (not height_in_units):
        print("Enter the height units among 'cm', 'm', 'foot' ,'inch'/nweight units among 'kg', 'pound'")
        continue
    
    # height = int(height)
    # weight = int(weight)
    # print(type(height), type(weight))

    BMI = round((weight / height ** 2) * 10000, 1)

    if BMI < 18.5:
        status = "Underweight"
    elif 18.5 <= BMI <= 24.9:
        status = "Normal weight"
    elif 25.0 <= BMI <= 29.9:
        status = "Overweight"
    elif 30.0 <= BMI <= 34.9:
        status = "Obesity class I"
    elif 35.0 <= BMI <= 39.9:
        status = "Obesity class II"
    else:
        status = "Obesity class III"

    print("\nAccording to the given weight and height, your BMI index turns out to be,", BMI, "and your status is,", status)
    break