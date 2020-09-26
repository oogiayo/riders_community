from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreationForm, PostChangeForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == 'POST':
        creation_form = PostCreationForm(request.POST)
        if creation_form.is_valid():
            creation_form.save()
            return redirect('posts:index')
    else:
        creation_form = PostCreationForm()
    context = {
        'creation_form': creation_form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


def update(request, post_pk):
    change_form = PostChangeForm()
    context = {
        'post_pk': post_pk,
        'change_form': change_form,
    }
    return render(request, 'posts/update.html', context)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:index')
