from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm
from django.views import View

class WelcomeView(View):
    def get(self, request):
        """
        Exibe a página de boas-vindas.
        Se o usuário estiver autenticado, redireciona para a página 'home'.
        """
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, "welcome.html")

def register_view(request):
    """
    Exibe e processa o formulário de registro de usuário.
    - Se o usuário já estiver autenticado, redireciona para 'home'.
    - Se o método for POST, valida o formulário, cria o usuário e faz login automático.
    - Se o método for GET, apenas exibe o formulário vazio.
    """
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
    """
    View personalizada de login.
    - Usa o template 'accounts/login.html'.
    - Redireciona automaticamente usuários já autenticados.
    """
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
