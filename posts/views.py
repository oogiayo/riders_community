from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostCreationForm, PostChangeForm, CommentCreationForm
from django.views.decorators.http import require_POST

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
    comments = post.comment_set.all()
    comment_form = CommentCreationForm()
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)


def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        change_form = PostChangeForm(request.POST, instance=post)
        if change_form.is_valid():
            change_form.save()
            return redirect('posts:detail', post_pk)
    else:
        change_form = PostChangeForm(instance=post)
    context = {
        'post': post,
        'change_form': change_form,
    }
    return render(request, 'posts/update.html', context)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:index')


# 댓글관련 기능
@require_POST
def create_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommentCreationForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        print('오긴옴?')
        return redirect('posts:detail', post_pk)
    context = {
        'comment_form': comment_form,
    }
    return render(request, 'posts:detail', context)


@require_POST
def delete_comment(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('posts:detail', post_pk)
