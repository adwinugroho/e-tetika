from django.shortcuts import render,redirect

# Create your views here.
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Register user
def registerView(request):
    form    = SignUpForm(request.POST or None)
    context = {
        'form':form,
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get('password1')
            messages.success(request,'Succesfully, account has been created!')
            return redirect('account:login')
        else:
            form = SignUpForm()
    return render(request, 'account/register.html', context)