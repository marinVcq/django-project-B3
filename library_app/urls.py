# yourappname/urls.py
from django.urls import path
from .views import home, login_user, register, logout, add_book

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('add_book/', add_book, name='add_book'),
]
