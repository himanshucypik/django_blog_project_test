from django.shortcuts import render, get_object_or_404, redirect
from blog_app.models import Post
from .models import Comment
from .forms import CommentForm

def add_comment(request, post_id):
	post = get_object_or_404(Post, id=post_id)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect("post_detail", pk=post.id)
	else:
		form = CommentForm()

	return render(request, "comments_app/add_comment.html", {"form": form, "post": post})
