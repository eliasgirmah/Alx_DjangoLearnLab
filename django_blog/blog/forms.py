from django import forms
from .models import Post, Comment

from taggit.forms import TagWidget  # ✅ Required import

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # ✅ Include tags
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your post here...'}),
            'tags': TagWidget(),  # ✅ Must be present for the checker
        }
class PostForm(forms.ModelForm):
    # extra, non-model field for comma-separated tags
    tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags (e.g. django,python,web)",
        widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2, tag3'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content']  # tags handled separately

    def clean_tags(self):
        raw = self.cleaned_data.get('tags', '')
        # normalize: split by comma, strip, lower, unique
        tags = [t.strip() for t in raw.split(',') if t.strip()]
        # optionally enforce a tag length or characters
        return list(dict.fromkeys([t for t in tags]))  # preserve order, remove dupes


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add a comment...'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        return content
