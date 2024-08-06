def Check_Some(month):
    month = month.lower()
    if month in ["december","january","february"]:
        print("Winter")
    elif month in ["march","april","may"]:
        print("Spring")
    elif month in ["june","july","august"]:
        print("Summer")
    elif month in ["september","october","november"]:
        print("Autumn")
    else:
        print("Invalid Month")

    

month = str(input("Enter the name of the month: "))
Check_Some(month)