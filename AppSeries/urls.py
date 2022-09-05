from django.urls import path
from AppSeries.views import *

urlpatterns = [
    path('', home, name='home'),
]