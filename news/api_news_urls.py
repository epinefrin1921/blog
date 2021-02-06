from django.urls import path, include
from . import api_views

app_name = 'api_news'
urlpatterns = [
    path('', api_views.all_news, name='api_news'),
    # path('create/', api_views.create_news, name='api_create_news'),
    path('<int:id>/', api_views.single_news, name='api_single_news'),
    path('<int:id>/update', api_views.update_news, name='api_update_news'),
    path('<int:id>/delete', api_views.delete_news, name='api_delete_news'),
    path('<int:id>/comment', api_views.add_comment_news, name='api_comment_news'),
]
