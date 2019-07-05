from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
	path('', views.PostListView.as_view(), name='post_list'),
	path('', views.PostListView.as_view(), name='home'),
	path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
	path('authors/', views.contributor, name='contributor_list'),
	path('editor/<slug:slug>/', views.EdiorView.as_view(), name='editor_info'),
	path('developer/<slug:slug>/', views.DeveloperView.as_view(), name='developer_info'),
	path('writer/<slug:slug>/', views.WriterView.as_view(), name='writer_info'),
	path('founder/<slug:slug>/', views.FounderView.as_view(), name='founder_info'),
	path('section/<slug:section>/', views.PostListView.as_view(), name="section-post" ),
	path('create/', views.PostCreateView.as_view(), name='post_create'),
	path('subscribe/', views.SubscribeView, name='subscribe_form'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
