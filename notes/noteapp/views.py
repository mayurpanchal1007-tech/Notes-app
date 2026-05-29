from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .form import NoteForm

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'noteapp/note_list.html', {'notes': notes})

def note_create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'noteapp/note_form.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'noteapp/note_form.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'noteapp/note_confirm_delete.html', {'note': note})