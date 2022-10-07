from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from shop.forms import LoginForm
from .forms import RegistrationForm
from django.contrib.auth.models import User
from userprofile.models import UserProfile

def user_login(request):
    errors = ""
    error = True
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    error = False
                    errors = ""
                    return redirect('../../shop/')
                    #return HttpResponse('Authenticated successfully')
                else:
                    #form = LoginForm()
                    error = True
                    errors = 'Disabled account'
                    render(request, 'registration/login.html', {'form': form,
                                                                'error': error,
                                                                'errors': 'Disabled account'})
                    #return HttpResponse('Disabled account')
            else:
                #form = LoginForm()
                error = True
                errors = 'Invalid login'
                render(request, 'registration/login.html', {'form': form,
                                                            'error': error,
                                                            'errors': errors})
                #return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form,
                                                            'error': error,
                                                            'errors': errors})

def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #print("in if ", User.objects.all().filter(email=cd['email']).first())
            if User.objects.all().filter(email=cd['email']).first() is None:
                user = User.objects.create_user(
                    username=cd['first_name'] + " " + cd['last_name'] + " " + cd['email'],
                    email=cd['email'],
                    password=cd['password'],
                    first_name=cd['first_name'],
                    last_name=cd['last_name']
                )
                login(request, authenticate(username=cd['email'], password=cd['password']))
                profile = UserProfile.objects.create(
                    user=user,
                    phone=cd['phone'],
                    address=cd['address'],
                    city=cd['city'],
                    post_code=cd['post_code']
                )
                print('User', user)
                print('profile', profile)
                return redirect('../../shop/')
            else:
                render(request, 'registration/registration.html', {'form': form,
                                                                   'error': True,
                                                                   'errors': 'этот email уже зарегистрирован'})
                print('not create user')
            print("username", cd['first_name'] + " " + cd['last_name'] + " " + cd['email'])
            print("email", cd['email'])
            print("password", cd['password'])
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form,
                                                                   'error': True,
                                                                   'errors': 'этот email уже зарегистрирован'})

