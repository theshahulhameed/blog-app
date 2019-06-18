from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView
)

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('post/create/', BlogCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
]