import calendar
from django.shortcuts import render, redirect
from datetime import datetime,timedelta
from django.views import generic
from django.contrib import messages
from django.utils.safestring import mark_safe

from interviews.models import interview
from interviews.forms import InterviewsRegister
from interviews.utils import Schedule


# Create your views here.

def interviews(request):
    if request.method == 'POST':
        form = InterviewsRegister(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('candidate')
            date = form.cleaned_data.get('date')
            messages.success(request, ('Interview Time {0} created for {1}').format(date, name.name))
            return redirect('home')
    else:
        form = InterviewsRegister()

    return render(request, 'interviews.html', {'form': form})


# Schedule view
class ScheduleView(generic.ListView):
    model = interview
    template_name = 'schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('day', None))

        sc = Schedule(d.year, d.month)
        html_sc = sc.formatmonth(withyear=True)

        context['schedule'] = mark_safe(html_sc)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()
