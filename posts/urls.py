from django.urls import path
from .views import PostListView, PostDetail, PostUpdateView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit')
]
