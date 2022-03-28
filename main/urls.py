from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('category/<str:category_title>', views.category, name='category'),
	path('add_news/', views.add_news, name='add_news'),
	path('news/<int:news_id>', views.one_news, name='one_news')
]