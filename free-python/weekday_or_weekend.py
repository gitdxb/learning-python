from datetime import datetime

def isWeekday(daytime):
    day = daytime.weekday()
    if day < 5:
        return True
    else:
        return False

if isWeekday(datetime.now()):
    print('It\'s weekday')
else:
    print('It\'s a weekend')