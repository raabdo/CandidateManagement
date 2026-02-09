from django.urls import path
from recruit import views
from candidates import views as candidate_views
from interviews import views as int_views


urlpatterns= [

    path('', views.home, name='home'),
    path('about/' , views.about, name='about'),
    path('register/', candidate_views.register, name='register'),
    path('candidates/', candidate_views.candidate_list, name='list'),
    path('interviews/', int_views.interviews, name='interviews'),
    path('schedule/', int_views.ScheduleView.as_view(), name='schedule')
]