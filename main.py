
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

daysText = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 
'seventh', 'eighth', 'ninth','tenth','eleventh','twelfth','thirteenth',
'fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth',
'twentieth','twenty first','twenty second','twenty third','twenty fourth',
'twenty fifth','twenty sixth','twenty seventh','twenty eighth','twenty ninth','thirtieth','thirtieth first']

daysNumber = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th',
'16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']

past = ['quarter past', 'half past', 'quarter to']

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