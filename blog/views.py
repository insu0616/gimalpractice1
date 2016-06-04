from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.urlresolvers import reverse
from django.contrib import messages


# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post_detail': post_detail})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, '글이 생성됐습니다.')
            return redirect(reverse('blog:detail', args=[post.pk]))
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, '댓글이 생성됐습니다.')
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=post_pk)
            comment.save()
            messages.success(request, '댓글이 수정되었습니다.')
            return redirect(comment.post.get_absolute_url())
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })

