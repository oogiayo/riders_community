from .models import PostModel
from django import forms

class PostForm(forms.ModelForm):
    
    class Meta:
        model = PostModel
        fields = '__all__'
