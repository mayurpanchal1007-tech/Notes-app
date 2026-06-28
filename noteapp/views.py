from django.shortcuts import render

def login_page(request):
    return render(request, 'noteapp/login.html')

def signup_page(request):
    return render(request, 'noteapp/signup.html')

def note_list(request):
    return render(request, 'noteapp/note_list.html')

def note_form(request, pk=None):
    return render(request, 'noteapp/note_form.html')