from lxml import html
import requests
import datetime

def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + datetime.timedelta(n)

dates = []
start_date = datetime.date(2015, 12, 5)
# Data from 5 december 2015
end_date = datetime.date.today()
for dt in daterange(start_date, end_date):
    if dt.weekday() == 2 or dt.weekday() == 5:
        dates.append(dt)

for date in dates:
    
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

