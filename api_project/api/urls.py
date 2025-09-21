from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList  # Your ListAPIView

# If you want to use a ViewSet, define the router
router = DefaultRouter()
# Example: if you have a BookViewSet
from .views import BookViewSet
# router.register(r'books-crud', BookViewSet, basename='book')
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]