from django.urls import path
from . import views
from . import views_auth

urlpatterns = [
    # home root and posts list (both)
    path('', views.PostListView.as_view(), name='home'),         # root home
    path('posts/', views.PostListView.as_view(), name='post-list'),

    # CRUD
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Auth
    path('register/', views_auth.register_view, name='register'),
    path('login/', views_auth.login_view, name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
    path('profile/', views_auth.profile_view, name='profile'),
]
