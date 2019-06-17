from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    return render(request, 'blog/post_list.html')

def Authors(request):
    return render(request, 'blog/Authors.html')

def post_detail(request):
    return render(request, 'blog/post_detail.html')        

# Create your views here.
def index(request):
	return render(request,"index.html")
