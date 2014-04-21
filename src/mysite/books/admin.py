from django.forms import ModelForm
from django.contrib import admin
from mysite.books.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Book, BookAdmin)