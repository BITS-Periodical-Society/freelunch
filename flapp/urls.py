from django.conf.urls import url

from . import views
# urlpatterns
app_name = 'flapp'
urlpatterns = [

 url(r'^about', views.about , name="about"),
    url(r'^contributors', views.contributors, name = "contributors" ),
    url(r'^contribute', views.contribute, name= "contribute" ),
    url(r'^science-technology', views.sciencetechnology, name= "sciencetechnology" ),
    url(r'^economics-finanace', views.economicsfinance, name= "economicsfinance" ),
    url(r'^world-affairs', views.worldaffairs, name= "worldaffairs" ),
    url(r'^editorial', views.editorial, name= "editorial" ),
    url(r'^book-reviews', views.bookreviews, name= "book-reviews" ),
]



 