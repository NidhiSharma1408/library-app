from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookCreate

def index(request):
    books = Book.objects.all()
    return render(request, 'books/library.html', { 'books':books})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid :
            upload.save()
            return redirect('index')
        else:
            return HttpResponse('<h1>your form is wrong,reload on <a href = {% url "index" %}> reload</a> </h1>')
    else:
        return render(request, 'books/upload_form.html', {'upload_form':upload })
