from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('group/', views.group_posts),
    path('group/<slug:pk>/', views.post_detail)
]
