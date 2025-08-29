from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from blog_app.forms import PostForm


def signup_view(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	else:
		form = SignupForm()
	return render(request, "auth_app/signup.html", {"form": form})

def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect("post_list")
	return render(request, "auth_app/login.html")

def logout_view(request):
	logout(request)
	return redirect("login")
def register_view(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Account created successfully! You can now login.")
			return redirect("login")
	else:
		form = UserCreationForm()
	return render(request, "auth_app/register.html", {"form": form})

def post_create(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)   # abhi save nahi hoga
			post.author = request.user       # logged-in user assign karo
			post.save()                      # ab save hoga
			return redirect("post_list")     # apne urls me jo bhi name diya hai
	else:
		form = PostForm()
	return render(request, "blog_app/post_create.html", {"form": form})
