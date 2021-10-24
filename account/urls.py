from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm
from .views import registerView
app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='account/login.html', 
        authentication_form=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(
        next_page='account:dashboard'), name='logout'),
    path('register/', registerView, name='register')
]