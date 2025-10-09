from django.urls import path
from . import views

urlpatterns = [
    # root / home (alias to PostListView)
    path('', views.PostListView.as_view(), name='home'),

    # post list (alias at /posts/ if you want both)
    path('posts/', views.PostListView.as_view(), name='post-list'),

    # Posts CRUD
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comments CRUD (uses pk for the post as required)
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # Tags & search
    path('tags/<slug:tag_slug>/', views.TagListView.as_view(), name='tag-posts'),
    path('search/', views.search_view, name='search'),

    # Authentication
    path('login/', views.LoginViewCustom.as_view(), name='login'),
    path('logout/', views.LogoutViewCustom.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),

    # Profile (simple view provided below)
    path('profile/', views.profile_view, name='profile'),
]
