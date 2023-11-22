from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('bhagya/',bhagya,name='bhagya'),
    path('bharath/',bharath,name='bharath'),
]