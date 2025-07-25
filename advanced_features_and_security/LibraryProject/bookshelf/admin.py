from django.contrib import admin
from .models import Book
from .models import CustomUser, CustomUserAdmin
from django.contrib.auth.admin import UserAdmin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

admin.site.register(Book)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Custom Fields", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )
    list_display = ["username", "email", "date_of_birth", "is_staff"]
    search_fields = ["username", "email"]

admin.site.register(CustomUser, CustomUserAdmin)



