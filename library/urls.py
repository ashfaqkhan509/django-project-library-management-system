from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'book', BookViewSet)
# router.register(r'members', MemberViewSet)
# router.register(r'issuebook', TransactionViewSet)

urlpatterns = [
    path('', index, name='home'),

    # login/logout
    path('login/', login_view, name='login'),
    path('logout/', Logout, name='logout'),

    # Book
    path('books/', BookListView, name='books'),
    path('books/add/', Book_add_view, name='add_book'),
    path('books/edit/<int:pk>/', edit_book_view, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book_view, name='delete_book'),

    # Member
    path('member_home/', Member_home, name='member_home'),
    path('members/', MemberListView, name='members'),
    path('members/add/', Member_add_view, name='add_member'),
    path('members/edit/<int:pk>/', edit_member_view, name='edit_member'),
    path('members/delete/<int:pk>/', delete_member_view, name='delete_member'),
    
    # Issue book
    path('issue_book_view/', IssueBookListView, name='issue_book_view'),
    path('issue_book/<int:book_id>/', issue_book_view, name='issue_book'),
    path('issue_book/edit/<int:pk>/', edit_issue_book_view, name='edit_issue_book'),
    path('issue_book/delete/<int:pk>/', delete_issue_book_view, name='delete_issue_book'),

    # path('signup', SignUp, name='signup'),
    # path('login/', Login, name='login'),
    # path('logout/', Logout, name='logout'),
    # path('Profile/Edit/', Edit_Profile, name='edit_profile'),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
