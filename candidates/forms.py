from distutils.command import upload

from django import forms
from candidates.models import candidate
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField


class CandidateRegister(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=12, required=True)
    email= forms.EmailField(max_length=100, required=True)
    cv = forms.FileField()
    gender = forms.ChoiceField(choices=(('',''),('male','Male'),('female', 'Female')))
    country = LazyTypedChoiceField(choices=countries)

    class Meta:
        model = candidate
        fields= ('name', 'phone', 'email', 'cv', 'gender', 'country')




