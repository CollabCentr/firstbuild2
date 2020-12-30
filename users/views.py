from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'users/index.html',  {'title':"Welcome|CollabCentr"})

def door_in(request):
    return render(request, 'users/belong.html', {'title':"Door In|CollabCentr"})

def login(request):
    return render(request, 'users/doorin.html', {'title':"Login|CollabCentr"})


@login_required
def homeUser(request):
    return render(request, 'users/home.html', {'title':"Home|CollabCenter"})
