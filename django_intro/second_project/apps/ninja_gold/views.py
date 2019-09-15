from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string
import random 


def index(request):
    if 'gold' not in request.session:
        request.session["gold"]=0

    if 'activities' not in request.session:
        request.session["activities"]=""

    return render(request,"ninja_gold/index.html")


def process(request):
    print(request.POST["btnValue"])
    if request.POST["btnValue"]=="farm":
        num=random.randint(10, 20)
        request.session["gold"]+=num
        request.session["activities"]+="Earned "+str(num)+ " from the farm!\n"

    if request.POST["btnValue"]=="cave":
        num=random.randint(5, 10)
        request.session["gold"]+=num
        request.session["activities"]+="Earned "+str(num)+ " from the cave!\n"

    if request.POST["btnValue"]=="house":
        num=random.randint(2, 5)
        request.session["gold"]+=num
        request.session["activities"]+="Earned "+str(num)+ " from the house!\n"

    if request.POST["btnValue"]=="casino":
        num=random.randint(0, 50)
        request.session["gold"]-=num
        request.session["activities"]+="Earned a casino and lost "+str(num)+ " golds!\n"
    return render(request,"ninja_gold/index.html")


