from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile_view(request):
    return render(request, 'blog/profile.html')

# -------------------------
# 📰 POST VIEWS
# -------------------------

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        # handle tags after saving post
        tag_names = form.cleaned_data.get('tags') or []
        if tag_names:
            tag_objs = []
            for name in tag_names:
                tag_obj, _ = Tag.objects.get_or_create(name=name)
                tag_objs.append(tag_obj)
            self.object.tags.set(tag_objs)
        return response


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_initial(self):
        initial = super().get_initial()
        tags_qs = self.get_object().tags.values_list('name', flat=True)
        initial['tags'] = ', '.join(tags_qs)
        return initial

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        tag_names = form.cleaned_data.get('tags') or []
        if tag_names:
            tag_objs = []
            for name in tag_names:
                tag_obj, _ = Tag.objects.get_or_create(name=name)
                tag_objs.append(tag_obj)
            self.object.tags.set(tag_objs)
        else:
            self.object.tags.clear()
        return response

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# -------------------------
# 💬 COMMENT VIEWS
# -------------------------

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


# -------------------------
# 🏷️ TAG & SEARCH VIEWS
# -------------------------

class TagListView(ListView):
    model = Post
    template_name = "blog/tag_posts.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        return Post.objects.filter(tags__slug=tag_slug).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
        return context


def search_view(request):
    query = request.GET.get('q', '').strip()
    posts = Post.objects.none()
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct().order_by('-published_date')
    context = {'posts': posts, 'query': query}
    return render(request, 'blog/search_results.html', context)


# -------------------------
# 🔐 AUTHENTICATION VIEWS
# -------------------------

from django.contrib.auth.views import LoginView, LogoutView


class LoginViewCustom(LoginView):
    template_name = 'blog/login.html'


class LogoutViewCustom(LogoutView):
    next_page = reverse_lazy('post-list')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post-list')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})
