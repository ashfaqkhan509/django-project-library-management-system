from django import forms
from django.contrib.auth.models import User
from .models import *

# class RegisterForm(forms.ModelForm):
#     password1 = forms.CharField(
#         label='Password', 
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
#     )
#     password2 = forms.CharField(
#         label='Confirm Password', 
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'user_type']

#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
#             'user_type': forms.Select(attrs={'class': 'form-control'}),
#         }

#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords do not match.")
#         return password2

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError("Username already taken.")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("Email already registered.")
#         return email

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        max_length=100
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )

class MemberEditForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'user_type', 'membership_status']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-select'}),
            'membership_status': forms.Select(attrs={'class': 'form-select'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


# class MemberForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         fields = '__all__'
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'membership_date': forms.DateInput(attrs={'class': 'form-control'}),
#             'membership_status': forms.Select(attrs={'class': 'form-control'}),
#         }


YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No')
    ]
class IssueBookForm(forms.ModelForm):
    
    class Meta:
        model = IssueBook
        fields = '__all__'
        exclude = ['expired_date', 'returned_date', 'issued_date']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'borrower': forms.Select(attrs={'class': 'form-control'}),
            'fine_per_day': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'over_due': forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-control d-inline'}),
        }

    def save(self, commit=True):
        instance = super(IssueBookForm, self).save(commit=False)
        if commit:
            # Update the book's status to "loaned"
            instance.book.status = 'loaned'
            instance.book.save()
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        book = kwargs.pop('book', None)
        super(IssueBookForm, self).__init__(*args, **kwargs)
        if book:
            self.fields['book'].initial = book
            self.fields['book'].widget.attrs['readonly'] = True
            self.fields['book'].widget.attrs['class'] = 'form-control'


class MemberForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'user_type', 'membership_status']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'user_type': forms.Select(attrs={'class': 'form-select'}),
            'membership_status': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Member.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Member.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user