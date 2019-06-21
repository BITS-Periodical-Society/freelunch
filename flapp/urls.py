from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list,name='post_list'),
    path('', views.post_list, name='Home'),
    path('Authors/', views.Authors, name='Authors'),
    path('Authors/profile_page', views.profile_page, name='profile_page'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('about/', views.about , name="about"),
    # path('contributors/', views.contributors, name = "contributors" ),
    # path('contribute/', views.contribute, name= "contribute" ),
    # path('science-technology/', views.sciencetechnology, name= "sciencetechnology" ),
    # path('economics-finanace/', views.economicsfinance, name= "economicsfinance" ),
    # path('world-affairs/', views.worldaffairs, name= "worldaffairs" ),
    # path('editorial/', views.editorial, name= "editorial" ),
    # path('book-reviews/', views.bookreviews, name= "book-reviews" ),
]