from django.urls import path
from AppChat.views import *

urlpatterns = [
    path('', index, name='index'),
    path('loginchat/', loginchat, name='loginchat'),
    path('registerchat/', registerchat, name='registerchat'),
    path('chathome/', chathome, name='chathome'),
    path('chathome/<int:sender>/<int:receiver>/', messagesbox, name='messagesbox'),
]