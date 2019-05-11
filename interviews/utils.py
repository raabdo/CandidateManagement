from datetime import datetime, timedelta
from calendar import HTMLCalendar
from interviews.models import interview
from time import strftime




class Schedule(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month =month
        super(Schedule, self).__init__()
    #formats a day as a td
    #filters events by day
    def formatday(self, day, interview):
        interviews_per_day = interview.filter(date__day= day)
        d=''

        for interview in interviews_per_day:
            d+= f'<br>{interview.candidate.name}</br>' \
                f'<br>Time: {interview.date.strftime("%H:%M")}</br>'

        if day!=0:
            return f'<td><span class="date">{day}</span><ul>{d}</ul></td>'
        return'<td></td>'


    #formats a week as a tr
    def formatweek(self, theweek, interview):
        week='\n'
        for d, weekday in theweek:
            week+= self.formatday(d, interview)
        return f'<tr> {week} </tr>'


    #formats a month as a table
    def formatmonth(self, withyear=True):
        interviews = interview.objects.filter(date__year=self.year, date__month=self.month)

        sc= f'<table border="0" cellpadding="0" cellspacing="5" class="schedule">\n'
        sc+=f'{self.formatmonthname(self.year, self.month, withyear= withyear)}\n'
        sc+=f'{self.formatweekheader()}\n'

        for week in self.monthdays2calendar(self.year, self.month):
                sc+= f'{self.formatweek(week, interviews)}\n'
        return sc

