from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)


def list_books(request):
   books = Book.objects.all()
   return render(request, 'relationship_app/list_books.html', {'book_list': books})

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    context['average_rating'] = book.get_average_rating() 

  

class register(CreateView):
   form_class = UserCreationForm()
   template_name = 'relationship_app/register.html'
   success_url = reverse_lazy('login')

class LoginView(LoginView):
   template_name = 'relationship_app/login.html'
   redirect_authenticated_user = True



def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'Admin'

@user_passes_test(is_admin)
def Admin(request):
    return render(request, 'relationship_app/admin_view.html')



def is_librarian(user):
   return hasattr(user, 'profile') and user.profile.role == "librarian"

@user_passes_test(is_librarian)
def Librarian(request):
   return render(request, 'relationship_app/librarian_view.html')



def is_member(user):
   return hasattr(user, 'profile') and user.profile.role == "member"

@user_passes_test(is_member)
def Member(request):
   return render(request, 'relationship_app/member_view.html')

