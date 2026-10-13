def ordinal_to_gregorian(year, day_of_year):
    months1 = "31", "29", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"
    months = "31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"
    cnt = 1
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        for i in range(1, 13):
            if day_of_year <= int(months1[i-1]):
                return (year, cnt, day_of_year)
            elif day_of_year >= int(months1[i-1]):
                day_of_year = day_of_year - int(months1[i-1])
                cnt+=1
    else:
        for i in range(1, 13):
            if day_of_year <= int(months[i-1]):
                return (year, cnt, day_of_year)
            elif day_of_year >= int(months[i-1]):
                day_of_year = day_of_year - int(months[i-1])
                cnt+=1