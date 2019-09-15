from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
   
    if request.method == "POST":
        request.session['counter'] += 1
        
    context={"unique_id" : get_random_string(length=14)}
    return render(request,"random_word/index.html",context)
