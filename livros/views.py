from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Livro, Emprestimo
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import LivroForm
from django.utils import timezone

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser
    
class LivroListAdminView(AdminRequiredMixin, View):
    def get(self, request):
        livros = Livro.objects.all()

        q = request.GET.get("q")
        if q:
            filtered = livros.filter(titulo__icontains=q)
            if filtered.exists():
                livros = filtered
        
        return render(request, "livro/livro_list_admin.html", {"livros": livros})
    
class LivroCreateView(AdminRequiredMixin, View):
    def get(self, request):
        form = LivroForm()
        return render(request, 'livro/livro_form.html', {"form": form})
    
    def post(self, request):
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_livros_admin")
        return render(request, "livro/livro_form.html", {"form": form})
    
class LivroUpdateView(AdminRequiredMixin, View):
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        form = LivroForm(instance=livro)
        return render(request, "livro/livro_form.html", {"form": form})
    
    def post(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()

            if livro.disponivel:
                Emprestimo.objects.filter(livro=livro, data_devolucao__isnull=True).update(data_devolucao=timezone.now())

            return redirect("lista_livros_admin")
        

        return render(request, "livro/livro_form.html", {"form": form})
    
class LivroDeleteView(AdminRequiredMixin, View):
    def post(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        livro.delete()
        return redirect("lista_livros_admin")
        


class LivroListView(LoginRequiredMixin, ListView):
    model = Livro
    template_name = "home.html"
    context_object_name = "livros"

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(titulo__icontains=q)
        return queryset

class MeusEmprestimosListView(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Emprestimo
    template_name = "meus_emprestimos.html"
    context_object_name = "emprestimos"

    def get_queryset(self):
        return Emprestimo.objects.filter(usuario=self.request.user).order_by("-data_emprestimo")

@login_required
def emprestar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if livro.disponivel:
        Emprestimo.objects.create(livro=livro, usuario=request.user)
        livro.disponivel = False
        livro.save()
    return redirect("home")

@login_required
def devolver_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    emprestimo = Emprestimo.objects.filter(
        livro=livro, usuario=request.user, data_devolucao__isnull=True
    ).first()

    if emprestimo:
        emprestimo.data_devolucao = timezone.now()
        emprestimo.save()

        livro.disponivel = True
        livro.save()

    return redirect("meus_emprestimos")
