import spacy

nlp = spacy.load("en_core_web_sm")
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

daysText = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 
'seventh', 'eighth', 'ninth','tenth','eleventh','twelfth','thirteenth',
'fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth',
'twentieth','twenty first','twenty second','twenty third','twenty fourth',
'twenty fifth','twenty sixth','twenty seventh','twenty eighth','twenty ninth','thirtieth','thirtieth first']

daysNumber = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th',
'16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']

weekDays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

past = ['quarter past', 'half past']

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




def getMonthIndex(m):
    return(months.index(m)+1)








def ExtractWeekDay(dateList): --Done
    datesContainsWeekDays = []
    for d in dateList:
        for w in weekDays:
            if w in d and d not in datesContainsWeekDays:
                datesContainsWeekDays.append(d)
    divided = divisor(datesContainsWeekDays)
    between = 0
    if 'between' in divided:
        between = 1
    daysIndex = []
    for d in divided:
        if d in weekDays:
            daysIndex.append(weekDays.index(d))
    statement = ""
    if len(daysIndex) == 2 and between == 1:
        statement = str(min(daysIndex))+'-'+str(max(daysIndex))
    else:
        for s in daysIndex:
            statement = statement + str(s) + ','
        statement = statement[:-1]
    return statement
    


def ExtractHour(dateList):
    datesContainsHour = []
    for d in dateList:
        if ':' in d and d not in datesContainsHour:
            datesContainsHour.append(d)
        else if 'past' in d and d not in datesContainsHour:
            datesContainsHour.append(d)
    

def ExtractMin(dateList):
    x = 0

def ExtractMonth(dateList): --Done
    datesContainsMonts = []
    for d in dateList:
        for m in months:
            if m in d and d not in datesContainsMonts:
                datesContainsMonts.append(d)
    divided = divisor(datesContainsMonts)
    between = 0
    if 'between' in divided:
        between = 1
    montsIndex = []
    for d in divided:
        if d in months:
            montsIndex.append(months.index(d)+1)
    statement = ""
    if len(montsIndex) == 2 and between == 1:
        statement = str(min(montsIndex))+'-'+str(max(montsIndex))
    else:
        for s in montsIndex:
            statement = statement + str(s) + ','
        statement = statement[:-1]
    return statement


def ExtractDay(dateList):
    x = 0


def combiner(strList):
    str = ''
    for v in strList:
        str = v + " "
    return str

def divisor(strList):
    divided = []
    for v in strList:
        for t in v.split():
            divided.append(t)
    return divided

def colonDividerHour(str):
    space = str.split()
    hourPart = ""

    for t in space:
        if ':' in t:
            temp = t.split(':')
            hourPart = temp[0]

tt = ['between January and May']
print(ExtractMonth(tt))
