from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Signupform

def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = Signupform()
    return render(request, 'user/signup.html', {'form': form})

def welcome(request):
    return render(request, 'UserCreationAck.html')


