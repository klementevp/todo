from django.urls import path, include
from users.views import *


urlpatterns = [
    path('register/', register, name='register'), 
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
]