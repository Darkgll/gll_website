from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Create your views here.
def login_user(request):

    if request.user.is_authenticated:
        return redirect('posts:posts')

    if request.method == 'POST':
        try:
            user_data = request.POST['login_email'].lower()
            password = request.POST['password']

            if '@' in user_data and User.objects.get(email=user_data):
                user_name = User.objects.get(email=user_data).username
            else:
                user_name = user_data

            user = authenticate(request, username=user_name, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Welcome back!', extra_tags='alert-success')
                return redirect('posts:posts')
            else:
                messages.error(request, 'Username, an email or password is incorrect', extra_tags='alert-danger')

        except User.DoesNotExist:
            messages.error(request, 'Username, an email or password is incorrect', extra_tags='alert-danger')

    return render(request, 'users/login-form.html')


def logout_user(request):
    logout(request)
    return redirect('users:login')


def register_user(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Thank you for registration!', extra_tags='alert-success')

            login(request, user)
            return redirect('posts:posts')

        else:
            messages.error(
                request, 'Oops! Something went wrong!', extra_tags='alert-danger')

    return render(request, 'users/register-form.html', {
        'form': form
        })