from django import forms
from datetime import date
from interviews.models import Interview
from candidates.models import Candidate

class InterviewsRegister(forms.ModelForm):

    candidate = forms.ModelChoiceField(queryset=Candidate.objects.all())
    date = forms.DateTimeField(required=True, initial=date.today)
    interviewer = forms.CharField(max_length=50, required=True)
    position = forms.ChoiceField(choices=(('Machine Learning','ML'),('Software Engineering','Software'),('Humane ressources','HR')))

    class Meta:
        model = Interview
        fields = ('candidate', 'date', 'interviewer')
        unique_together = ['date', 'candidate']




