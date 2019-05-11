from django.db import models
from django_countries.fields import CountryField
# Create your models here.

#Dynamic filename
def get_upload_path(instance, filename):
    name1, name2 = filename.split('.')
    file_path = 'Cvs/{candidate_name}/{name1}.{name2}'.format(
         candidate_name=instance.name, name1=name1, name2=name2)
    return file_path

class candidate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone= models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    cv = models.FileField(upload_to=get_upload_path)
    gender = models.CharField(choices=(	('',''),('male','Male'),('female', 'Female')), max_length=10, blank=True, null=True)
    country = CountryField(blank=True)

    def __str__(self):
        return self.name