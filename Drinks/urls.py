from django.urls import path
from Drinks.views import *
app_name='Drinks'

urlpatterns=[

    path('teachers/',teachers,name='teachers'),
]