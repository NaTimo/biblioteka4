from django.contrib import admin

# Register your models here
from .models import Author, Genre, Book, BookInstance

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "display_books"]
class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    readonly_fields = ("uuid", )
    extra = 0
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "isbn", "display_genre")

    inlines = [BookInstanceInLine]
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "due_back")
    list_filter = ("status", "due_back")
    search_fields = ("uuid", "book__title")
    list_editable = ("due_back", "status")

    fieldsets = (
        ("General", {"fields": ("uuid", "book")}),
        ("Availability", {"fields": ("status", "due_back")}),
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)