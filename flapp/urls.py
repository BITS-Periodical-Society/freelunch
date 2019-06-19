from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
    path('', views.post_list, name='Home'),
    path('Authors/', views.Authors, name='Authors'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.post_list, name="category_post" ),
    # path('about/', views.about , name="about"),
    # path('contributors/', views.contributors, name = "contributors" ),
]