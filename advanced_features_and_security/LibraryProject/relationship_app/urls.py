from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView, name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.Admin, name='admin_view'),
    path('librarian/', views.Librarian, name='librarian_view'),
    path('member/', views.Member, name='member_view'),
    path('add_book/', views.Member, name='add_book'),
    path('edit_book/', views.Member, name='edit_book'),
    path('delete_book/', views.Member, name='delete_book'),
]