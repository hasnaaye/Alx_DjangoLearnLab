from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django import BookForm


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
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def Admin(request):
    return render(request, 'relationship_app/admin_view.html')



def is_librarian(user):
   return hasattr(user, 'userprofile') and user.profile.role == "Librarian"

@user_passes_test(is_librarian)
def Librarian(request):
   return render(request, 'relationship_app/librarian_view.html')



def is_member(user):
   return hasattr(user, 'userprofile') and user.profile.role == "Member"

@user_passes_test(is_member)
def Member(request):
   return render(request, 'relationship_app/member_view.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
   if request.method == 'POST':
      form = BookForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('list-books')
   else:
      form = BookForm()
   return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def add_book(request):
   if request.method == 'POST':
      form = BookForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('list-books')
   else:
      form = BookForm()
   return render(request, 'relationship_app/change_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def add_book(request):
   if request.method == 'POST':
      form = BookForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('list-books')
   else:
      form = BookForm()
   return render(request, 'relationship_app/delete_book.html', {'form': form})
