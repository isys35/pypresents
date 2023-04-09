from django.contrib.auth import views as auth_views

path('accounts/login/', auth_views.LoginView.as_view()),