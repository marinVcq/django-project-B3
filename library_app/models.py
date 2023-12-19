# yourappname/models.py
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    publication_date = models.TextField()
    image_url = models.URLField()
    borrower = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for user profile if needed
