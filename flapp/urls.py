from django.urls import path
from . import views

urlpatterns = [
	path('', views.PostListView.as_view(), name='post_list'),
    path('', views.PostListView.as_view(), name='Home'),
    path('Authors/', views.AuthorListView.as_view(), name='Authors'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', views.PostListView.as_view(), name="category_post" ),
]