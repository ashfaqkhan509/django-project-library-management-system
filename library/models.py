from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
# from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Book(models.Model):
    STATUS = [
        ('available', 'Available'),
        ('loaned', 'Loaned'),
        ('lost', 'Lost'),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    status = models.CharField(max_length=50, choices=STATUS, default='available')
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# class Member(models.Model):
#     STATUS = [
#         ('active', 'Active'),
#         ('closed', 'Closed'),
#         ('blacklist', 'Blacklist'),
#     ]
#     # member = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True, max_length=200, null=True, blank=True)
#     membership_date = models.DateTimeField(auto_now_add=True)
#     membership_status = models.CharField(max_length=20, choices=STATUS, default='active')

#     def __str__(self):
#         return self.name
    

class Member(AbstractUser):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('blacklist', 'Blacklist'),
    ]

    USER = [
        ('librarian', 'Librarian'),
        ('student', 'Student'),
    ]

    user_type = models.CharField(choices=USER, max_length=50, default='student')
    membership_date = models.DateTimeField(auto_now_add=True)
    membership_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.username


class IssueBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE)
    issued_date = models.DateField(default=timezone.now)
    returned_date = models.DateField(null=True, blank=True)
    expired_date = models.DateTimeField(default=timezone.datetime.today() + timedelta(days=15))
    fine_per_day = models.PositiveIntegerField(default=0)
    over_due = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return f"{self.book.title} issued to {self.member.name}"
    
    @property
    def get_total_fine(self):
        total_fine = 0
        today = timezone.now()  # Get the current time with timezone info
        if today > self.expired_date:
            self.over_due = True
            days = (today - self.expired_date).days  # Calculate days overdue
            total_fine = self.fine_per_day * days
        return total_fine
    




