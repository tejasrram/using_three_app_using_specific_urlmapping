from django.urls import path
from python.views import *
app_name='nothing'

urlpatterns=[
    path('python/',python,name='python'),
]