from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'


# Vue pour rediriger /users/ vers /users/login/
def redirect_to_login(request):
    return redirect('users:login')


urlpatterns = [
    # Ajoutez cette ligne pour gérer l'URL /users/
    path('', redirect_to_login, name='users_home'),

    # Vos URLs existantes
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),
         name='password_change'),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),
]
