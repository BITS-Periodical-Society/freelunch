from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
    path('', views.post_list, name='Home'),
    path('Authors/', views.Authors, name='Authors'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/science-technology/', views.sciencetechnology, name="science-technology" ),
    path('category/economics-finanace/', views.economicsfinance, name="economics-finance" ),
    path('category/world-affairs/', views.worldaffairs, name="world-affairs" ),
    path('category/editorial/', views.editorial, name="editorial" ),
    path('category/book-reviews/', views.bookreviews, name="book-reviews" ),
    # path('about/', views.about , name="about"),
    # path('contributors/', views.contributors, name = "contributors" ),
    # path('contribute/', views.contribute, name= "contribute" ),

]