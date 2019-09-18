from django.shortcuts import render, HttpResponse
from .models import Book
from .models import Author

def index(request):
    if request.method == "POST":
        title=request.POST["title"]
        desc=request.POST["desc"]
        Book.objects.create(title=title,description=desc)
        
    context = {
    "all_the_books": Book.objects.all()
    }
    return render(request,"authors_app/index.html", context)


def viewBook(request, id):
    if request.method == "POST":
        author_id=request.POST["author"]
        this_author=Author.objects.get(id=author_id)
        this_book=Book.objects.get(id=id)
        this_book.authors.add(this_author)
        print("dfghjkl;kjhgfhjkl;",author_id)

    context = {
    "book": Book.objects.get(id=id),
    "authors":Author.objects.all()

    }
    return render(request,"authors_app/books.html",context)


def authors(request):
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        notes=request.POST["notes"]
        Author.objects.create(first_name=first_name,last_name=last_name, notes=notes)
        
    context = {
    "all_the_authors": Author.objects.all()
    }
    return render(request,"authors_app/authors.html", context)


def viewAuthors(request,id):
    if request.method == "POST":
        book_id=request.POST["book"]
        this_book=Book.objects.get(id=book_id)
        this_author=Author.objects.get(id=id)   
        this_author.books.add(this_book)


    context = {
    "author": Author.objects.get(id=id),
    "books":Book.objects.all()

    }
    return render(request,"authors_app/author.html",context)
