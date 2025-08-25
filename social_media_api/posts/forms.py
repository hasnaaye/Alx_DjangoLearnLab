from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': TagWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Write your comment here',
                                              'rows': 4})
        }

        def clean_content(self):
            content = self.cleaned_data.get('content')
            if not content or content.strip() == '':
                raise forms.ValidationError("Comment cannot be empty.")
            if len(content) < 3:
                raise forms.ValidationError("Comment is too short (minimum 3 characters).")
            return content
