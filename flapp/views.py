from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category
from .forms import PostForm



def index(request):
	return render(request,"index.html")

def post_list(request, **kwargs):
	try:
		slug = kwargs['slug']
		category = Category.objects.get(slug=slug)
		posts = category.post_set.all().order_by('-published_date')
	except:
		posts = Post.objects.all()
	paginator = Paginator(posts, 1)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)

	context = {
		'posts': paginated_queryset,
		'page': page_request_var,
	}

	return render(request, 'blog/post_list.html', context)

def Authors(request):
	return render(request, 'blog/Authors.html')

def post_detail(request, **kwargs):
	post = get_object_or_404(Post, slug=kwargs['slug'])
	context = {'post': post}
	return render(request, 'blog/post_detail.html', context)