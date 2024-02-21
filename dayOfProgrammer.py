def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    elif year < 1918:
        if year % 4 == 0:
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)
    

if __name__ == '__main__':
    year = 2017
    print(dayOfProgrammer(year)) # 13.09.2017