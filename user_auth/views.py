from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterUserForm

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )

def show_user(request):
    """This view displays the username and encrypted password of the user after they have logged in."""
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username":request.user.username,
        "password": request.user.password,
    })

def reg_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ("You have successfully registered!"))
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = RegisterUserForm()
    return render(request, 'authentication/reg_user.html', {
        'form':form,
    })