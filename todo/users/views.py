from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from users.models import User
from users.forms import UserCreationForm 


def register(request):
    form = UserCreationForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home_page', user.id)
        else:
            messages.error(request, 'Ошибка во время регистрации, вернитесь на главную страницу и начните регистрацию заново')
    return render(request, 'users/register_page.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home_page', request.user.id)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, f'User {email} does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page', user.id)
        else:
            messages.error(request, 'Email or password does not exist')
    return render(request, 'users/login_page.html', context={})


def logoutUser(request):
    logout(request)
    return redirect('welcome_page')
