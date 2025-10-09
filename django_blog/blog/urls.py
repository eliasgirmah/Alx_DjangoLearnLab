from django.urls import path
from . import views

urlpatterns = [
    # Posts
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),

    # Authentication
    path('login/', views.LoginViewCustom.as_view(), name='login'),
    path('logout/', views.LogoutViewCustom.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
]
