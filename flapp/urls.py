from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.post_list,name='post_list'),
    path('', views.post_list, name='Home'),
    path('Authors', views.Authors, name='Authors'),
    path('post_detail', views.post_detail, name='post_detail'),
    url(r'^about', views.about , name="about"),
    url(r'^contributors', views.contributors, name = "contributors" ),
    url(r'^contribute', views.contribute, name= "contribute" ),
    url(r'^science-technology', views.sciencetechnology, name= "sciencetechnology" ),
    url(r'^economics-finanace', views.economicsfinance, name= "economicsfinance" ),
    url(r'^world-affairs', views.worldaffairs, name= "worldaffairs" ),
    url(r'^editorial', views.editorial, name= "editorial" ),
    url(r'^book-reviews', views.bookreviews, name= "book-reviews" ),
]