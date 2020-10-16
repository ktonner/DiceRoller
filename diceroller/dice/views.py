from django.shortcuts import render
from django.template import Context, Template, loader

# Create your views here.
from django.http import HttpResponse
import random

def roll():
    return random.randint(1,6)

def rollManyOld(request, number):
    roll = 0
    for i in range(number):
        roll += random.randint(1,6)

    # roll = all the dice rolls
    return HttpResponse("Your dice roll was {roll}".format(roll=roll))

def rollMany(request, number):
    roll = 0
    rolls = 0
    rollsList = []
    for i in range(number):
        rolls = random.randint(1,6)
        roll += rolls
        rollsList.append(rolls)

    # roll = all the dice rolls
    s = ", ".join(map(str, rollsList))
    return HttpResponse("Your dice roll was {roll}, with rolls {rolls}.".format(roll=roll, rolls=s))

def rollPage(request):
    # return HttpResponse("Your dice roll was {roll}").format(roll = roll())

    return HttpResponse(
        "Your dice roll was {roll}".format(roll = roll())
        )
    
    s = "Your dice roll was {roll}".format(roll = roll())
    return HttpResponse(s)
    
def index(request):
    context = Context({'my_name': 'Kathleen'})
    template = loader.get_template('dice/index.html')

    return HttpResponse(template.render(context, request))
