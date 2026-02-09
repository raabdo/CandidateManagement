from calendar import HTMLCalendar

from interviews.models import Interview


class Schedule(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Schedule, self).__init__()

    def formatday(self, day, interviews):
        interviews_per_day = interviews.filter(date__day=day)
        d = ''
        for interview in interviews_per_day:
            # Using a span for time and a strong tag for the name
            d += (
                f'<li class="calendar-event">'
                f'<span class="event-time">{interview.date.strftime("%H:%M")}</span>'
                f'<span class="event-name">{interview.candidate.name}</span>'
                f'</li>'
            )

        if day != 0:
            # Highlight today if it matches (optional logic can be added here)
            return f'<td class="day"><span class="day-number">{day}</span><ul class="event-list">{d}</ul></td>'
        return '<td class="empty"></td>'

    def formatweek(self, theweek, interviews):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, interviews)
        return f'<tr>{week}</tr>'

    def formatmonth(self, withyear=True):
        interviews = Interview.objects.filter(date__year=self.year, date__month=self.month)

        # Modernized table headers and classes
        sc = f'<table class="calendar-table">\n'
        sc += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        sc += f'{self.formatweekheader()}\n'

        for week in self.monthdays2calendar(self.year, self.month):
            sc += f'{self.formatweek(week, interviews)}\n'
        sc += '</table>'
        return sc