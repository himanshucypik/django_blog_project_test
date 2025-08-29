from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
	path("admin/", admin.site.urls),
	path("auth/", include("auth_app.urls")),
	path("blog/", include("blog_app.urls")),
	path("comments/", include("comments_app.urls")),
	path("blog/", include("auth_app.urls")),
	path("", lambda request: redirect("blog/")),

]
