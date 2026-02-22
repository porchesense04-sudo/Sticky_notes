from django.shortcuts import render
from .models import Note  # correct import from your app

# List all notes
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes_app/note_list.html', {'notes': notes})