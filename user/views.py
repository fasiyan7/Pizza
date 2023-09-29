from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def show(request):
    return HttpResponse("Welcome User")


def signupView(request):
        uform = UserCreationForm(request.POST)
        if request.method == "POST":
            if uform.is_valid():
                uname = uform.cleaned_data.get('username')
                pwd = uform.cleaned_data.get('password1')
                user1=User.objects.create_user(username=uname,password=pwd)
                user1.save()
                user = authenticate(request, username=uname, password=pwd)
                login(request,user)
                #return redirect('home')
                return HttpResponse("You are successfully registered")
        else:
            uform = UserCreationForm()
        return render(request,'signup.html', {'form': uform})
