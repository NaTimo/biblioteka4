from django.contrib import admin

# Register your models here
from .models import Author, Genre, Book, BookInstace

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstace)