from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm
from django.views import View

class WelcomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, "welcome.html")

def register_view(request):
    
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("welcome")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"forms": form})
        

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
