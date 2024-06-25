from django.contrib import admin

from . import models

class BookInline(admin.TabularInline):
    model = models.Book

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('author', 'language')
    inlines = [BookInstanceInline]

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_date', 'status', 'id')
    list_filter = ('status', 'due_date')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_date')
        })
    )

admin.site.register(models.BookGenre)
