from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog_app/post_detail.html', {'post': post})

def post_create(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)  # database me abhi save mat karo
			post.author = request.user      # current logged-in user ko author set karo
			post.save()                     # ab save karo
			return redirect("post_list")    # post create hone ke baad list page pe bhejo
	else:
		form = PostForm()
	return render(request, "blog_app/post_create.html", {"form": form})
def post_update(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('post_detail', pk=pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog_app/post_update.html', {'form': form})
