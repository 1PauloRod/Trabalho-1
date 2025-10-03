from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register_view, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", register_view, name="register"), 
    path("login/", CustomLoginView.as_view(), name="login"), 
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
     # Formulário para enviar email
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),

    # Mensagem de "email enviado"
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    # Formulário para redefinir senha (link enviado por email)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),

    # Mensagem de "senha redefinida"
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
