def gregorian_to_ordinal(year, months, day):
    months1 = "31", "29", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"
    months2 = "31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"
    cnt = day
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        for i in range(1, months):
            cnt = cnt + int(months1[i-1])
        return cnt
    else:
        for i in range(1, months):
            cnt = cnt + int(months2[i-1])
        return cnt
