from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from .models import Post, Section, Writer, Developer, Editor, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


class PostCreateView(CreateView):
	model = Post
	template_name = 'blog/post_form.html'
	form_class = PostForm

	def form_valid(self, form):
		post = form.save(commit=False)
		post.published_date = timezone.now()
		post.save()
		return super().form_valid(form)


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


class CommentCreateView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'blog/comment_form.html'
	context_object_name = 'form'

	def get_success_url(self):
		return reverse('post_detail', kwargs={'slug': self.kwargs['slug']})

	def form_valid(self, form):
		post = get_object_or_404(Post, slug=self.kwargs['slug'])
		comment = form.save(commit=False)
		comment.post = post
		comment.save()
		return super().form_valid(form)