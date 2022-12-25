from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group_posts, name='group'),
    path('group/<slug:pk>/', views.post_detail)
]
