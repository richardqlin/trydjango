from django.urls import path

from .views import (

	ArticleListView, ArticleDetailView, ArticleCreateView, 
	ArticleUpdateView,

	ArticleDeleteView

	)


app_name = 'articles'

urlpatterns = [

 path('', ArticleListView.as_view(), name = 'article-list'),


path('<int:id>/', ArticleDetailView.as_view(), name = 'acticle-detail'),

path('create/', ArticleCreateView.as_view(), name = 'article-create'),

path('<int:id>/update', ArticleUpdateView.as_view(), name = 'article-update'),

path('<int:id>/delete', ArticleDeleteView.as_view(), name = 'article-delete'),

]

