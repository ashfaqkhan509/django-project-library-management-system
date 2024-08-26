from django.shortcuts import render, redirect, get_object_or_404
# from rest_framework import viewsets
from .models import *
from .serializers import *
# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User, Group
from .decorators import librarian_or_admin_required, student_required
# Create your views here.


def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.user_type == 'librarian':
                    return redirect('books')  # Redirect to the home page or any other page
                else:
                    return redirect('member_home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def Logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

@login_required
@student_required
def Member_home(request):
    books = IssueBook.objects.filter(borrower_id=request.user.id)
    context = {
        'books': books
    }
    return render(request, 'member_home.html', context)




# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter)
#     search_fields = ['title', 'author', 'id']

# class MemberViewSet(viewsets.ModelViewSet):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
    
# class TransactionViewSet(viewsets.ModelViewSet):
#     queryset = IssueBook.objects.all()
#     serializer_class = IssueBookSerializer

# Book Part

@login_required
@librarian_or_admin_required
def BookListView(request):
    book = Book.objects.all().order_by('-add_date')
    paginator = Paginator(book, 4)
    page_number = request.GET.get("page")
    books_obj = paginator.get_page(page_number)
    context = {
        "books_obj": books_obj
    }
    return render(request, 'books.html', context)

@login_required
@librarian_or_admin_required
def Book_add_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('books')
        
    form = BookForm()

    context = {
        'form': form
    }
    return render(request, 'add_book.html', context)

@login_required
@librarian_or_admin_required
def edit_book_view(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('books')
    form = BookForm(instance=book)

    context = {
        'form': form,
        'book': book
    }            

    return render(request, 'edit_book.html', context)

@login_required
@librarian_or_admin_required
def delete_book_view(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book was deleted successfully')
        return redirect('books')
    

# Member Part
@login_required
@librarian_or_admin_required
def MemberListView(request):
    member = Member.objects.all()
    paginator = Paginator(member, 2)
    page_number = request.GET.get('page')
    member_obj = paginator.get_page(page_number)
    context = {
        'member_obj': member_obj
    }

    return render(request, 'members.html', context)

@login_required
@librarian_or_admin_required
def Member_add_view(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member registered successfully!')
            return redirect('members')  # Replace with your desired redirect
    else:
        form = MemberForm()

    context = {
        'form': form,
    }
    return render(request, 'add_member.html', context)

@login_required
@librarian_or_admin_required
def edit_member_view(request, pk):
    member = Member.objects.get(pk=pk)
    if request.method == 'POST':
        form = MemberEditForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member data updated successfully!')
            return redirect('members')
        
    form = MemberEditForm(instance=member)
    context = {
        'form': form,
        'member': member
    }
    return render(request, 'edit_member.html', context)

@login_required
@librarian_or_admin_required
def delete_member_view(request, pk):
    member = Member.objects.get(pk=pk)
    member.delete()
    messages.success(request, 'Member record deleted successfully')
    return redirect('members')


# Issue Book
@login_required
@librarian_or_admin_required
def IssueBookListView(request):
    book = IssueBook.objects.all()
    paginator = Paginator(book, 5)
    page_number = request.GET.get('page')
    issue_book_obj = paginator.get_page(page_number)
    context = {
        'issue_book_obj': issue_book_obj
    }

    return render(request, 'issue_book_list.html', context)


@login_required
@librarian_or_admin_required
def issue_book_view(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = IssueBookForm(request.POST, book=book)
        if form.is_valid():
            form.save()
            return redirect('books')  # Adjust the redirect as needed
    else:
        form = IssueBookForm(book=book)
    
    context = {
        'form': form,
        'book': book
    }
    return render(request, 'issue_book.html', context)

@login_required
@librarian_or_admin_required
def edit_issue_book_view(request, pk):
    issue_book = get_object_or_404(IssueBook, pk=pk)

    if request.method == 'POST':
        form = IssueBookForm(request.POST, instance=issue_book, book=issue_book.book)
        if form.is_valid():
            issue_book = form.save(commit=False)
            issue_book.save()
            return redirect('issue_book_view')  # Redirect to a list or detail view after saving
    else:
        form = IssueBookForm(instance=issue_book, book=issue_book.book)
    
    context = {
        'form': form,
        'issue_book': issue_book
        }

    return render(request, 'edit_issue_book.html', context)

@login_required
@librarian_or_admin_required
def delete_issue_book_view(request, pk):
    issue_book = IssueBook.objects.get(pk=pk)
    issue_book.delete()
    messages.success(request, 'Issued Book record deleted successfully')
    return redirect('issue_book_view')



