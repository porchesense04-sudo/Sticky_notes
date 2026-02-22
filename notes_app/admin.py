from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # columns shown in the list
    search_fields = ('title', 'content')    # allow searching
    list_filter = ('created_at',)           # filter by date
    ordering = ('-created_at',)             # newest first

# Register Note with custom admin
admin.site.register(Note, NoteAdmin)