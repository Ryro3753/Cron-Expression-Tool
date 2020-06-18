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



def main():
    print("Welcome to Cron Expression Tool, type -help in order to get details of this tool.\n")
    inp = inputCron()
    inp = inp.lower()
    copy = 0
    for item in inp.split():
        if item == "-copy":
            copy = 1
            inp = inp[6:]
        if item == "-help":
            help()
            return 0
    DateNTime = nlpDateTime(inp)
    statement = statementCombiner(DateNTime)
    if(isCronValid(statement) == 0):
        print("Your statement is not valid")
        return 0
    if(copy == 1):
        copyToClipBoard(statement)
    print('Your CRON statement is: ' + statement)
    
#function that print out help
def help(): 
    return """Cron Expression Tool is a tool that converts the given text statement to a Cron Expression. 
    \nThe text should be written as a decent English sentence.
    \nYou will automatically be copying the output as you add the statement “-copy” before your text.
    \nSome Examples: The output of “23rd February at 10:00” is “00 10 23 2 *”.
    \nThe output of “10 May at between 10:00 to 16:30” is “00-30 10-16 10 5 *”.
    \nThe output of “Every Saturday at 19:45” is “45 19 * * 6”.
    \nThe output of “-copy Between 10th to 19th in July” is “* * 10-19 7 *”. 
    Additionally, the output will be copied to your clipboard."""

#function that copy the statement to clipboard of the user
def copyToClipBoard(s):
    cmd = 'echo ' + s.strip() + '|clip'
    return subprocess.check_call(cmd,shell=True)

#function that request input from user
def inputCron():
    inp = input('Please write your text statement:')
    return inp

#function that parse the text by DATE and TIME label
def nlpDateTime(s): 
    doc = nlp(s)
    DateNTime = []
    for item in doc.ents:
        if item.label_ == 'TIME' or item.label_ == 'DATE':
            DateNTime.append(str(item))
    return DateNTime

#function that get month from month List
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

#function that get month index for example December = 12, May = 5
def getMonthIndex(m):
    return(months.index(m)+1)

#function that extract weekDays statements from text like "Tuesday"
def ExtractWeekDay(dateList): 
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
    
#function that finds hours from text statement
def ExtractHour(dateList): 
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
       
#function that finds mins from text statement
def ExtractMin(dateList): 
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

#function that finds month from text statements like "between January to August"
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

#function that finds days of the month in a text like "23rd or thirteenth"
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

#function that combine list of string in a one string
def combiner(strList):
    str = ''
    for v in strList:
        str = v + " "
    return str

# function that divide a string into a list of string
def divisor(strList):
    divided = []
    for v in strList:
        for t in v.split():
            divided.append(t)
    return divided

# function that finds hour part in a time statement
def colonDividerHour(str):
    space = str.split()
    hourPart = ""
    for t in space:
        if ':' in t:
            temp = t.split(':')
            hourPart = temp[0]
    return hourPart

#function that finds min part in a time statement
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

#function that check if Cron is Valid by some varius methods
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
    if cronSplit[3] != "*" and cronSplit[2] != "*":            
        if len(cronSplit[3]) == 1 and len(cronSplit[2]) == 1:
            if (int(cronSplit[3]) == 4 or int(cronSplit[3]) == 6 or int(cronSplit[3]) == 9 or int(cronSplit[3]) == 11) and int(cronSplit[2]) == 31:
                return 0
    return 1



if __name__ == '__main__':
    main()
