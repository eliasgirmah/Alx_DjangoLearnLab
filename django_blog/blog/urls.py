from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),  # ✅ use 'home' here
    path('posts/', views.PostListView.as_view(), name='post-list'),  # optional
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # Tags & Search
    path('tags/<str:tag_name>/', views.TagPostListView.as_view(), name='posts-by-tag'),
    path('search/', views.search_view, name='search'),

    # Auth
    path('login/', views.LoginViewCustom.as_view(), name='login'),
    path('logout/', views.LogoutViewCustom.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
]
