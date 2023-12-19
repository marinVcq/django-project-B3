# yourappname/urls.py
from django.urls import path
from .views import home, login_user, register, logout, add_book, edit_book, delete_book, borrow_book, user_dashboard, release_book

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('borrow_book/<int:book_id>/', borrow_book, name='borrow_book'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('release_book/<int:book_id>/', release_book, name='release_book'),

]
