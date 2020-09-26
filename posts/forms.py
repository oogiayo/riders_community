from .models import Post
from django import forms

class PostCreationForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'


class PostChangeForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
