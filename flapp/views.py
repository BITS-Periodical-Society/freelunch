from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, View
from django.urls import reverse
from .models import Post, Section, Writer, Developer, Editor, Founder, Comment
from .forms import PostForm, CommentForm, SubscribeForm
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


class PostDetailView(View):
	"""
	View for a post.
	"""
	model = Post
	context_object_name = 'post'
	template_name = 'blog/post_detail.html'
	slug_url_kwarg = 'slug'

	def get(self, request, *args, **kwargs):
		context={}
		post = get_object_or_404(Post, slug=self.kwargs['slug'])
		context[self.context_object_name] = post
		form = CommentForm
		return render(request,'blog/post_detail.html', {'post':post, 'form':form})


	def post(self, request, *args, **kwargs):
		context={}
		post = get_object_or_404(Post, slug=self.kwargs['slug'])
		if request.method == "POST":
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit=False)
				comment.post = post
				comment.save()
			return redirect('post_detail', slug=post.slug)
		else:
			form = CommentForm()
			return render(request, 'blog/post_detail.html', {'form':form})



def contributor(request):
	developers = Developer.objects.all()
	editors = Editor.objects.all()
	writer = Writer.objects.all()
	founder = Founder.objects.all()

	return render(request, 'blog/Authors.html', {'developers': developers, 'editors': editors, 'writers': writer, 'founders': founder})


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

class FounderView(DetailView):
	model = Founder
	template_name = 'blog/profile_page.html'
	context_object_name = 'me'
	slug_url_kwarg = 'slug'

def SubscribeView(request):
	form = SubscribeForm()

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
		return redirect('post_list')
	else:
		form = SubscribeForm()
	return render(request, 'blog/subscribe.html', {'form':form})
