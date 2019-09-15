from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    print(context)
    return render(request,'my_app/index.html',context)