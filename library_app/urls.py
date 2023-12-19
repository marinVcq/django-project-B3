# yourappname/urls.py
from django.urls import path
from .views import home, login_user, register, logout, add_book, edit_book, delete_book

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]
