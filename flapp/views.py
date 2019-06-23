from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Post, Section, Writer, Developer, Editor
from .forms import PostForm, CommentForm

class PostListView(ListView):
	"""
	Returns posts with category filter.
	"""
	context_object_name = 'posts'
	template_name = 'blog/post_list.html'
	paginate_by = 2

	def get_queryset(self):
		try:
			section = self.kwargs['section']
			posts = Post.objects.all().filter(section=section)
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


def contributor(request):
	developers = Developer.objects.all()
	editors = Editor.objects.all()
	writer = Writer.objects.all()

	return render(request, 'blog/Authors.html', {'developers': developers, 'editors': editors, 'writer': writer})


class EdiorView(DetailView):
	model = Editor
	template_name = 'blog/profile_page.html'
	context_object_name = 'me'
	slug_url_kwarg = 'slug'


class DeveloperView(DetailView):
	model = Developer
	template_name = 'blog/profile_page.html'
	context_object_name = 'me'
	slug_url_kwarg = 'slug'


class WriterView(DetailView):
	model = Writer
	template_name = 'blog/profile_page.html'
	context_object_name = 'me'
	slug_url_kwarg = 'slug'
