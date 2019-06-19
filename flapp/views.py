from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm



def index(request):
	return render(request,"index.html")

def post_list(request):
	posts = Post.objects.all()[:4]
	context = {'posts': posts}
	return render(request, 'blog/post_list.html', context)

def Authors(request):
	return render(request, 'blog/Authors.html')

def post_detail(request, **kwargs):
	post = get_object_or_404(Post, slug=kwargs['slug'])
	context = {'post': post}
	return render(request, 'blog/post_detail.html', context)

def sciencetechnology(request):
	posts = Post.objects.filter(category="ST")
	context = {'posts': posts}
	return render(request, 'blog/post_list.html', context)

def economicsfinance(request):
	posts = Post.objects.filter(category="EF")
	context = {'posts': posts}
	return render(request, 'blog/post_list.html', context)

def worldaffairs(request):
	posts = Post.objects.filter(category="WA")
	context = {'posts': posts}
	return render(request, 'blog/post_list.html', context)

def editorial(request):
	posts = Post.objects.filter(category="E")
	context = {'posts': posts}
	return render(request, 'blog/post_list.html', context)

def bookreviews(request):
	posts = Post.objects.filter(category="BR")
	context = {'posts': posts}
	return render(request, 'blog/post_list.html', context)
