from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    allBooks = Book.objects.all() 
    context = {
        "books": allBooks,
    }
    return render(request, "baseapp/index.html", context)

def authors(request):
    allAuthors = Author.objects.all() 
    context = {
        "authors": allAuthors,
    }
    return render(request, "baseapp/authors.html", context)

def addBook(request):
    
    newTitle = request.POST["newTitle"]
    newDesc = request.POST["newDesc"]

    Book.objects.create(title=newTitle, desc=newDesc)
    return redirect("/")

def addAuthor(request):

    newFName = request.POST["newFirstName"]
    newLName = request.POST["newLastName"]
    newNotes = request.POST["newNotes"]
    
    Author.objects.create(first_name=newFName, last_name=newLName, notes=newNotes)
    return redirect("/authors")

def viewBook(request, id):
    allAuthors = Author.objects.all()
    
    context = {
        "authors": allAuthors,
        "thisBook": Book.objects.get(id=id),
    }
    return render(request, "baseapp/viewbook.html", context)

def addlAuth(request):
    
    pass

def viewAuth(request, id):
    allBooks = Book.objects.all()
    
    context = {
        "books": allBooks,
        "thisAuth": Author.objects.get(id=id),
    }
    return render(request, "baseapp/viewauth.html", context)

def addlBook(request, id):
    bookid = request.POST['addlBook']
    thisauthor = Author.objects.get(id=id)
    addlbook = Book.objects.get(id=bookid)
    thisauthor.books.add(addlbook)

    author_id = thisauthor.id

    return redirect(f"/authors/{author_id}")