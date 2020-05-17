
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']



def getMonth(s):
    for item in s:
        if item in months:
            yield item

def getMonthAndDate(s):
    month = ''
    day = ''
    for item in s:
        if item in months:
            month = item

        if item.isdigit() or item[0].isdigit():
            day = item

    return (month, day)

for i in getMonthAndDate(text.split()):
    print(i)


def getMonthIndex(m):
    return(months.index(m)+1)


print(getMonthIndex('December'))