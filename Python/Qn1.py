def calculate_days(totaldays):
    years = int(totaldays/365)
    months = int((totaldays-years*365)/30)
    days = int(totaldays - (years*365)-(months*30))
    print("Years=", years)
    print("Months=", months)
    print("Days=", days)


totaldays = int(input("Enter the number of days:"))
calculate_days(totaldays)

