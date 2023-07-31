from django.urls import path
from mern.views import *
app_name='nothing'

urlpatterns=[
    path('mern/',mern,name='mern'),
]