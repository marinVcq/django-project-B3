from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from .forms import BookForm
from django.http import JsonResponse
from .models import Book
import requests

@login_required
def user_dashboard(request):
    user_borrowed_books = Book.objects.filter(borrower=request.user)
    return render(request, 'user_dashboard.html', {'user_borrowed_books': user_borrowed_books})

@login_required
def release_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, borrower=request.user)
    book.borrower = None
    book.save()
    return redirect('user_dashboard')

def borrow_book(request, book_id):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, id=book_id, borrower=None)
        book.borrower = request.user
        book.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'User not authenticated'}, status=401)

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

@user_passes_test(is_superuser)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        # Update the book fields based on the form data
        book.author = request.POST.get('author')
        book.title = request.POST.get('title')
        book.abstract = request.POST.get('abstract')
        book.publication_date = request.POST.get('publication_date')
        book.image_url = request.POST.get('image_url')

        # Save the updated book
        book.save()

        return redirect('home')
    else:
        return render(request, 'edit_book.html', {'book': book})

@user_passes_test(is_superuser)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('home')

    return render(request, 'delete_book.html', {'book': book})

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
