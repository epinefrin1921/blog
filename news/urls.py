from django.urls import path, include
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.all_news, name='home'),
    path('create/', views.create_news, name='about'),
    path('<int:id>/', views.single_news, name='contact'),
    path('<int:id>/update', views.update_news, name='contact'),
    path('<int:id>/delete', views.delete_news, name='contact'),
    path('<int:id>/comment', views.add_comment_news, name='comment'),
    path('api/', include('news.api_news_urls')),
]
