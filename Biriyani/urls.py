from django.urls import path
from Biriyani.views import *
app_name='Biriyani'
urlpatterns=[

    path('Chicken_Biriyani/',Chicken_Biriyani,name='Chicken_Biriyani')
]