
from django import forms
from candidates.models import Candidate
from django_countries.fields import CountryField


class CandidateRegister(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=12, required=True)
    email= forms.EmailField(max_length=100, required=True)
    cv = forms.FileField()
    gender = forms.ChoiceField(choices=(('',''),('male','Male'),('female', 'Female')))
    country = CountryField().formfield()

    class Meta:
        model = Candidate
        fields= ('name', 'phone', 'email', 'cv', 'gender', 'country')




