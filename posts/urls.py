from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:post_id>", views.post, name="post"),  # TODO make as str:post_name maybe
]
