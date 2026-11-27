from django.shortcuts import render
from tasks import shared_task


# Create your views here.
def multiplayer(r, x):
    shared_task.delay(r,x)
    
