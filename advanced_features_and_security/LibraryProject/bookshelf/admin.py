from django.contrib import admin
from .models import Book
from .models import CustomUser, CustomUserAdmin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

admin.site.register(Book)
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.

