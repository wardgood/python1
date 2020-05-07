import datetime as dt
from dateutil.rrule import rrule, DAILY

start_date=dt.date(2020,3,1)
end_date=dt.date(2020,3,31)

for x in rrule(DAILY, dtstart=start_date, until=end_date ):
    a=dt.date.isoweekday(x)
    b=x.strftime("%Y%m%d")
    
    if(a==6 or a==7):
        continue
    print(b,a)


