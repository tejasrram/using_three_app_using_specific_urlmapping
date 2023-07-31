from django.urls import path
from java.views import *
app_name='nothing'

urlpatterns=[
    path('java/',java,name='java'),
]