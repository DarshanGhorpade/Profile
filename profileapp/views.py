from django.shortcuts import redirect, render
from django.http import HttpResponse

from profileapp.models import Feedback

from .forms import CreateUserForm, ProfileForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'profileapp/home.html')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {'form': form}
    return render(request, 'profileapp/profile.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in successfully.')
            return redirect("/")
        else:
            messages.info(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'profileapp/login_page.html')


@login_required(login_url='login')
def user_feedback(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        feedback_subject = request.POST.get('subject')
        feedback_message = request.POST.get('message')
        if feedback_subject != '':
            feedback = Feedback.objects.create(name = username, email = email, subject = feedback_subject, message = feedback_message)
            feedback.save()
            messages.success(request, f'{username}, Your feedback is recorded.')
        else:
            messages.info(request, 'Unable to record feedback.')
            return redirect('feedback')
    return render(request, 'profileapp/feedback.html')


def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your account is created, login now.')
            return redirect('login')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'profileapp/register_page.html', context)

    context = {'form': form}
    return render(request, 'profileapp/register_page.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out suuccessfully.')
    return redirect('login')