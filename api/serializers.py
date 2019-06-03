from rest_framework import serializers

from candidates.models import candidate
from interviews.models import interview


class candidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = candidate
        fields = ('name', 'phone', 'email', 'cv', 'gender', 'country')

class interviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = interview
        fields = ('candidate', 'date', 'interviewer', 'position')