from rest_framework import generics
from candidates.models import candidate
from api.serializers import candidateSerializer
from interviews.models import Interview
from api.serializers import interviewSerializer

# Create your views here.

class candidateApiView(generics.ListAPIView):
    queryset = candidate.objects.all()
    serializer_class = candidateSerializer


class interviewApiView(generics.ListAPIView):
    queryset = Interview.objects.all()
    serializer_class = interviewSerializer