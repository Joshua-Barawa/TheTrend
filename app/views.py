from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


@login_required(login_url='login-user/')
def index(request):
    posts = Post.objects.all()
    comments = Comment.objects.filter()
    post_question(request)
    return render(request, 'html/index.html', {'posts': posts, 'comments': comments})


@login_required(login_url='login-user/')
def post_question(request):
    user = request.user
    if request.method == "POST":
        post = request.POST.get('post')
        new_post = Post(content=post, user=user)
        new_post.save()

    return redirect('index')


@login_required(login_url='login-user/')
def submit_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, "Project was submitted successful")
            return redirect('index')
    else:
        form = ProjectForm()

    return render(request, 'html/project-form.html', {'form': form})


@login_required(login_url='login-user/')
def add_comment(request, id):
    user = request.user
    post = Post.objects.get(id=id)
    print(post.user.username)
    if request.method == "POST":
        comment = request.POST.get('comment')
        new_comment = Comment(reply=comment, post=post, user=user)
        new_comment.save()
    return redirect('index')


@login_required(login_url='login-user/')
def like(request, id):
    post = Post.objects.get(id=id)
    post.likes = post.likes + 1
    post.save()
    return redirect('index')


@login_required(login_url='login-user/')
def dislike(request, id):
    post = Post.objects.get(id=id)
    post.likes = post.likes - 1
    post.save()
    return redirect('index')


@login_required(login_url='login-user/')
def my_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    projects = Project.objects.filter(user=user)
    if request.method == "POST":
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        profile.profile_pic = request.FILES['profile_pic']
        user = User.objects.filter(username=user.username).update(username=username, first_name=fullname, email=email)
        profile.save()
    return render(request, 'html/profile.html', {"profile": profile, "projects": projects})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect('index')
        else:
            for error in form.error_messages:
                messages.error(request, form.error_messages[error])
                print(error)
                return render(request, 'html/register.html', {"form": form})
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'html/login.html', {})
    return render(request, 'html/login.html', {})


@login_required(login_url='login-user/')
def logout_user(request):
    logout(request)
    return redirect('login-user')


@login_required(login_url='login-user/')
def delete_account(request, id):
    User.objects.get(id=id).delete()
    return redirect('login-user')
