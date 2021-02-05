import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import BlogForm
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

def all_news(request):
    queryset = Blog.objects.all()
    # if request.user.is_authenticated:
    context = {
        'news': queryset
    }
    return render(request, "news/news_list.html", context)
    # else:
    #     return redirect('/accounts/login')


@user_passes_test(lambda u: u.is_superuser)
def create_news(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.posted_on = datetime.datetime.now()
            obj.posted_by = request.user
            obj.save()
            return redirect(f'/news/{obj.id}')
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, "news/news_create.html", context)


def single_news(request, id):
    try:
        obj = Blog.objects.get(id=id)
        comments = Comment.objects.filter(blog=id).order_by('posted_on').reverse()
    except ObjectDoesNotExist:
        raise Http404
    context = {
        "obj": obj,
        "comments":  comments
    }
    return render(request, "news/news_detail.html", context)


@user_passes_test(lambda u: u.is_superuser)
def update_news(request, id):
    obj = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect(f'/news/{id}')

    context = {
        "form": form
    }
    return render(request, "news/news_create.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_news(request, id):
    if request.method == 'POST':
        try:
            obj = Blog.objects.get(id=id)
            print(id)
            obj.delete()
            return redirect('/news')
        except ObjectDoesNotExist:
            raise Http404
    obj = get_object_or_404(Blog, id=id)
    context = {
        "obj": obj
    }
    return render(request, "news/news_delete.html", context)


@login_required()
def add_comment_news(request, id):
    if request.method == 'POST':
        commentText = request.POST['comment']

        comment = Comment.objects.create(
            text=commentText,
            blog=Blog.objects.get(id=id),
            posted_by=request.user,
            posted_on=datetime.datetime.now()
        )
        comment.save()
        return redirect('/news/' + str(id))
