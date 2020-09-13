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

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or none, instance=book_sel)
    if book_form.is_valid:
        book_form.save()
        return redirect('index')
    return render(request, 'book/upload_form.html', { 'upload_form':book_form })

def delete_book(reqeust, book_id):
    book_id = int(book_id)
    try: 
        Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
    

