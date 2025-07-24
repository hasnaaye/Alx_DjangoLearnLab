from django.urls import path
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('about/', views.AboutView.as_view(), name='about'),
]