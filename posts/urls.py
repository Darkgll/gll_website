from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<str:post_id>', views.post, name='post'),  # TODO make as str:post_name maybe
    path('create-post/', views.create_post, name='create_post'),
    path('update-post/<str:post_id>', views.update_post, name='update_post'),
    path('delete-post/<str:post_id>', views.delete_post, name='delete_post')
]
