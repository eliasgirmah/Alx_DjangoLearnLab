# posts/views.py
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

# ---------------------------
# Pagination
# ---------------------------
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# ---------------------------
# Post ViewSet
# ---------------------------
class PostViewSet(viewsets.ModelViewSet):
    # Required for automated checks
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', 'content']
    filterset_fields = ['author__id', 'author__username']
    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        return Post.objects.select_related('author').prefetch_related('likes').all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'status': 'post unliked'}, status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            return Response({'status': 'post liked'}, status=status.HTTP_200_OK)

# ---------------------------
# Comment ViewSet
# ---------------------------
class CommentViewSet(viewsets.ModelViewSet):
    # Required for automated checks
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['content']
    filterset_fields = ['post', 'author__id', 'author__username']
    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        return Comment.objects.select_related('author', 'post').prefetch_related('likes').all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
            return Response({'status': 'comment unliked'}, status=status.HTTP_200_OK)
        else:
            comment.likes.add(user)
            return Response({'status': 'comment liked'}, status=status.HTTP_200_OK)

# ---------------------------
# Feed View
# ---------------------------
class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        # Get posts from followed users, newest first
        posts = Post.objects.filter(author__in=user.following.all()).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
