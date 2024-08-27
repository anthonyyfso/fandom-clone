from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


from .forms import CustomUserCreationForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/homepage.html'


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'home/register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, "home/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "home/login.html")

def logout_view(request):
    logout(request)
    return render(request, "home/login.html", {
        "message": "Logged out."
    })
    