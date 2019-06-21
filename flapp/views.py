from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Post, Category
from .forms import PostForm


class PostListView(ListView):
	"""
	Returns posts with category filter.
	"""
	context_object_name = 'posts'
	template_name = 'blog/post_list.html'
	paginate_by = 2

	def get_queryset(self):
		try:
			slug = self.kwargs['slug']
			category = Category.objects.get(slug=slug)
			posts = category.post_set.all().order_by('-published_date')
		except:
			posts = Post.objects.all()
		return posts


class PostDetailView(DetailView):
	"""
	Detail view for a post.
	"""
	model = Post
	context_object_name = 'post'
	template_name = 'blog/post_detail.html'
	slug_url_kwarg = 'slug'


class AuthorListView(ListView):
	model = User
	template_name = 'blog/Authors.html'