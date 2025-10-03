from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from accounts import views
from livros.views import LivroListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")), 
    path("livros/", include("livros.urls")),
    path("home/", LivroListView.as_view(), name="home"),
    path("", views.WelcomeView.as_view(), name="welcome")
]
