from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "first_app/index.html", context)

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/") 

def show(request, number ):
    return HttpResponse("placeholder to display blog number "+ number) 



def edit(request, number ):
    return HttpResponse("placeholder to edit blog "+number ) 

def delete(request,number):
    return redirect("/") 



