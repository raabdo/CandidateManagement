from django.db import models
from candidates.models import candidate
from django.utils import timezone

# Create your models here.


class interview(models.Model):
    candidate= models.OneToOneField(candidate, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, unique=True)
    interviewer = models.CharField(max_length=50, default='Zhang')
    position = models.CharField(max_length=50, default='Machine Learning engineer')

    def __str__(self):
        return self.candidate.name + ' '+ str(self.date)
