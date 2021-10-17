import datetime


today = datetime.date.today()

def calc_time(end_date, start_date = str(today.strftime("%d-%m-%Y")), time_format = 'd'):
    """
    The calc_time() function calculates the amount of time between two given dates, the starting date, if not provided, by default taken as the current date.
    
    The end_date attribute accepts a string, the dates arranged in a format "DD-MM-YYYY)
    """


    time = ""
    end_date = end_date.split("-")
    if start_date:
        start_date = ((start_date).split('-'))

    for i in range(len(start_date)):
        start_date[i] = int(start_date[i])
    for i in range(len(end_date)):
        end_date[i] = int(end_date[i])
    
    years = end_date[2] - start_date[2]
    months = end_date[1] - start_date[1]
    days=  end_date[0] - start_date[0]

    if years < 0 or months < 0 or days < 0:
        print("The given date has already passed! :)\nBut anyhow, here's the info.")
        
        time = time + "You have passed the given, end date by, " + str(abs(days)) + " day(s), " + str(abs(months)) + " month(s), and " + str(abs(years)) + " year(s)."
    else:
        time = time + str(abs(days)) + " day(s), " + str(abs(months)) + " month(s), and " + str(abs(years)) + " year(s)."
    
    print("\n" + time)

calc_time("04-12-2021")