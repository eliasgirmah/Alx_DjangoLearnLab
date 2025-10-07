from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect root to login
    path('accounts/', include('accounts.urls')),
]
