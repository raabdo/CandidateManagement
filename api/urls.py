from django.urls import path
from api.views import interviewApiView, candidateApiView


urlpatterns = [
    path('interviews/', interviewApiView.as_view()),
    path('candidates/', candidateApiView.as_view())
]
