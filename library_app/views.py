from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from .forms import BookForm
from .models import Book
import requests

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def add_book(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        abstract = request.POST.get('abstract')
        publication_date = request.POST.get('publication_date')
        image_url = request.POST.get('image_url')

        Book.objects.create(
            author=author,
            title=title,
            abstract=abstract,
            publication_date=publication_date,
            image_url=image_url
        )

        return redirect('home')

    return render(request, 'add_book.html')

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to the main page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')  # Redirect to the main page after logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_user(request, user)  # Log the user in after registration
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
