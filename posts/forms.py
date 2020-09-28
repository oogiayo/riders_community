from .models import Post, Comment
from django import forms

class PostCreationForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'


class PostChangeForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'


class CommentCreationForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('post',)
