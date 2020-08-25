from django.shortcuts import render

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

def index(request):
    # return HttpResponse("Your dice roll was {roll}").format(roll = roll())

    return HttpResponse(
        "Your dice roll was {roll}".format(roll = roll())
        )
    
    s = "Your dice roll was {roll}".format(roll = roll())
    return HttpResponse(s)
    
# ("{roll}").format(roll = roll())

# s = "Your dice roll was {roll}".format(roll = roll())
# HttpResponse(s)
