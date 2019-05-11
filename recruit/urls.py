from django.conf.urls import include
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from recruit import views
from candidates import views as candidate_views
from interviews import views as int_views


urlpatterns= [

    path('', views.home, name='home'),
    path('about/' , views.about, name='about'),
    path('register/', candidate_views.register, name='register'),
    path('candidates/', candidate_views.list, name='list'),
    path('interviews/', int_views.interviews, name='interviews'),
    path('schedule/', int_views.ScheduleView.as_view(), name='schedule'),

]