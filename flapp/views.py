from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, View
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Post, Section, Writer, Developer, Editor, Tag
from .forms import PostForm, SubscribeForm, TagForm
from .suggest import recommend


class PostListView(ListView):
	"""
	Returns posts with category filter.
	"""
	context_object_name = 'posts'
	template_name = 'blog/post_list.html'
	paginate_by = 4

	def get_queryset(self):
		try:
			section = self.kwargs['section']
			posts = Post.objects.all().filter(section=section)
		except:
			posts = Post.objects.all()
		return posts


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'blog/post_form.html'
	form_class = PostForm

	def form_valid(self, form):
		post = form.save(commit=False)
		post.published_date = timezone.now()
		post.save()
		return super().form_valid(form)


class TagCreateView(LoginRequiredMixin, CreateView):
	model = Tag
	template_name = 'blog/tag_form.html'
	form_class = TagForm

	def form_valid(self, form):
		tag = form.save(commit=False)
		tag.save()
		return HttpResponse('<script type="text/javascript">window.close();</script>')

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
		recommends = recommend(post)
		context[self.context_object_name] = post
		form = SubscribeForm
		return render(request,'blog/post_detail.html', {'post': post, 'recommends': recommends, 'form': form})

	def post(self, request, *args, **kwargs):
		form = SubscribeForm(request.POST)
		if form.is_valid():
			subscriber = form.save(commit=False)
			subscriber.save()
			return HttpResponseRedirect(request.path_info)



def contributor(request):
	developers = Developer.objects.all()
	editors = Editor.objects.all()
	writer = Writer.objects.filter(designation='FO') | Writer.objects.filter(designation='A')
	guest_writer = Writer.objects.filter(designation='GA')

	return render(request, 'blog/Authors.html', {'developers': developers, 'editors': editors, 'writers': writer, 'guest_writers':guest_writer})


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

def SubscribeView(request):
	form = SubscribeForm()

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponse('<script type="text/javascript">window.close()</script>')
	else:
		form = SubscribeForm()
	return render(request, 'blog/subscribe.html', {'form':form})


def Disclaimer(request):
	return render(request, 'blog/disclaimer.html')
