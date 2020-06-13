import spacy
import subprocess

nlp = spacy.load("en_core_web_sm")

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

daysText = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 
'seventh', 'eighth', 'ninth','tenth','eleventh','twelfth','thirteenth',
'fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth',
'twentieth','twenty-first','twenty-second','twenty-third','twenty-fourth',
'twenty-fifth','twenty-sixth','twenty-seventh','twenty-eighth','twenty-ninth','thirtieth','thirtieth-first']

daysNumber = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th',
'16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']

weekDays = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

#past = ['quarter past', 'half past']


def main():
    inp = inputCron()
    inp = inp.lower()
    copy = 0
    for item in inp.split():
        if item == "-copy":
            copy = 1
            inp = inp[6:]
    DateNTime = nlpDateTime(inp)
    statement = statementCombiner(DateNTime)
    if(isCronValid(statement) == 0):
        print("Your statement is not valid")
        return 0
    if(copy == 1):
        copyToClipBoard(statement)
    print('Your CRON statement is: ' + statement)
    

def copyToClipBoard(s):
    cmd = 'echo ' + s.strip() + '|clip'
    return subprocess.check_call(cmd,shell=True)

def inputCron():
    inp = input('Please write your text statement:')
    return inp

def nlpDateTime(s):
    doc = nlp(s)
    DateNTime = []
    for item in doc.ents:
        if item.label_ == 'TIME' or item.label_ == 'DATE':
            DateNTime.append(str(item))
    return DateNTime

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

def ExtractWeekDay(dateList): ##Done
    datesContainsWeekDays = []
    for d in dateList:
        for w in weekDays:
            if w in d and d not in datesContainsWeekDays:
                datesContainsWeekDays.append(d)
    if not datesContainsWeekDays:
        return '*'
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
    
def ExtractHour(dateList): ##Done
    datesContainsHour = []
    for d in dateList:
        if ':' in d and d not in datesContainsHour:
            datesContainsHour.append(d)
    if not datesContainsHour:
        return '*'
    divided = divisor(datesContainsHour)
    between = 0
    if 'between' in divided:
        between = 1
    hourIndex = []
    for d in divided:
        if ':' in d:
            hourIndex.append(colonDividerHour(d))
    statement = ""
    if len(hourIndex) == 2 and between == 1:
        statement = str(min(hourIndex))+'-'+str(max(hourIndex))
    else:
        for s in hourIndex:
            statement = statement + str(s) + ','
        statement = statement[:-1]
    return statement
       
def ExtractMin(dateList): ##Done
    datesContainsMin = []
    for d in dateList:
        if ':' in d and d not in datesContainsMin:
            datesContainsMin.append(d)
    if not datesContainsMin:
        return '*'
    divided = divisor(datesContainsMin)
    between = 0
    if 'between' in divided:
        between = 1
    minIndex = []
    for d in divided:
        if ':' in d:
            minIndex.append(colonDividerMin(d))
    statement = ""
    if len(minIndex) == 2 and between == 1:
        statement = str(min(minIndex))+'-'+str(max(minIndex))
    else:
        for s in minIndex:
            statement = statement + str(s) + ','
        statement = statement[:-1]
    return statement

def ExtractMonth(dateList): ##Done
    datesContainsMonts = []
    for d in dateList:
        for m in months:
            if m in d and d not in datesContainsMonts:
                datesContainsMonts.append(d)
    if not datesContainsMonts:
        return '*'
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

def ExtractDay(dateList): ## Done
    datesContainsDays = []
    for d in dateList:
        for m in daysText:
            if m in d and d not in datesContainsDays:
                datesContainsDays.append(d)
    for d in dateList:
        for m in daysNumber:
            if m in d and d not in datesContainsDays:
                datesContainsDays.append(d)
    if not datesContainsDays:
        return '*'
    divided = divisor(datesContainsDays)
    between = 0
    if 'between' in divided:
        between = 1
    daysIndex = []
    for d in divided:
        if d in daysText:
            daysIndex.append(daysText.index(d)+1)
        elif d in daysNumber:
            daysIndex.append(daysNumber.index(d)+1)
    statement = ""
    if len(daysIndex) == 2 and between == 1:
        statement = str(min(daysIndex))+'-'+str(max(daysIndex))
    else:
        for s in daysIndex:
            statement = statement + str(s) + ','
        statement = statement[:-1]
    return statement

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
    return hourPart

def colonDividerMin(str):
    space = str.split()
    minPart = ""
    for t in space:
        if ':' in t:
            temp = t.split(':')
            minPart = temp[1]
    return minPart

def statementCombiner(DateNTime):
    min = ExtractMin(DateNTime)
    hour = ExtractHour(DateNTime)
    day = ExtractDay(DateNTime)
    month = ExtractMonth(DateNTime)
    weekDay = ExtractWeekDay(DateNTime)
    combine = str(min) + ' ' + str(hour) + ' ' + str(day) + ' ' + str(month) + ' ' + str(weekDay)
    return combine

def isCronValid(cron):
    min = []
    hour = []
    day =[]
    month = []
    weekDay = []
    cronSplit = cron.split()
    if len(cronSplit) != 5:
        return 0
    for minHypen in cronSplit[0].split('-'):
        for minComma in minHypen.split(','):
            if minComma != "*":
                min.append(int(minComma)) 
            else:
                min.append("*")
    for hourHypen in cronSplit[0].split('-'):
        for hourComma in hourHypen.split(','):
            if hourComma != "*":
                hour.append(int(hourComma))
            else:
                hour.append("*")
    for dayHypen in cronSplit[0].split('-'):
        for dayComma in dayHypen.split(','):
            if dayComma != "*":
                day.append(int(dayComma))
            else:
                day.append("*")
    for monthHypen in cronSplit[0].split('-'):
        for monthComma in monthHypen.split(','):
            if monthComma != "*":
                month.append(int(monthComma))
            else:
                month.append("*")
    for weekDayHypen in cronSplit[0].split('-'):
        for weekDayComma in weekDayHypen.split(','):
            if weekDayComma != "*":
                weekDay.append(int(weekDayComma))
            else:
                weekDay.append("*")
    

    if cronSplit[3] != "*" and cronSplit[2] != "*":
        if len(cronSplit[3]) <= 2 and len(cronSplit[2]) <= 2:
            if int(cronSplit[3]) == 2 and int(cronSplit[2]) > 29:
                return 0
    if month != "*" and day != "*":            
        if len(month) == 1 and len(day) == 1:
            if (int(cronSplit[3]) == 4 or int(cronSplit[3]) == 6 or int(cronSplit[3]) == 9 or int(cronSplit[3]) == 11) and int(cronSplit[2]) == 31:
                return 0
    return 1



if __name__ == '__main__':
    main()

## İki ay aralığı için uğraş