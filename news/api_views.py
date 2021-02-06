import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from .forms import BlogForm
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

def all_news(request):
    querySet = Blog.objects.all()
    # if request.user.is_authenticated:
    listNews = []
    for obj in querySet:
        listNews.append(obj.as_dict())

    return JsonResponse(listNews, safe=False)
    # else:
    #     return redirect('/accounts/login')


# @user_passes_test(lambda u: u.is_superuser)
# def create_news(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.posted_on = datetime.datetime.now()
#             obj.posted_by = request.user
#             obj.save()
#             return redirect(f'/news/{obj.id}')
#     elif request.method=='GET':
#         data = {
#             "Action": "This endpoint is used to post news",
#             "How": "Send following information as POST to this endpoint",
#             "What": "title, desc"
#         }
#         return JsonResponse(data, safe=False)
#     else:
#         raise Http404


def single_news(request, id):
    if request.method == 'GET':
        try:
            obj = Blog.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404
        context = obj.as_dict()
        return JsonResponse(context, safe=False)
    else:
        raise Http404


@user_passes_test(lambda u: u.is_superuser)
def update_news(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Blog, id=id)
        newTitle = request.POST['title']
        newText = request.POST['text']
        obj.title = newTitle
        obj.desc = newText
        obj.save()
        data = {
            "status": "success",
            "message": "Successfully updated item with id " + str(id),
            "blog": obj.as_dict(),
        }
        return JsonResponse(data, safe=False)
    else:
        raise Http404


@user_passes_test(lambda u: u.is_superuser)
def delete_news(request, id):
    if request.method == 'POST':
        try:
            obj = Blog.objects.get(id=id)
            obj.delete()
            data = {
                "status": "success",
                "message": "Successfully deleted item with id " + str(id),
            }
            return JsonResponse(data, safe=False)
        except ObjectDoesNotExist:
            raise Http404
    else:
        raise Http404


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

        data = {
            "status": "success",
            "message": "Successfully commented item with id " + str(id),
            "comment": comment.as_dict(),
        }
        return JsonResponse(data, safe=False)
    else:
        raise Http404
