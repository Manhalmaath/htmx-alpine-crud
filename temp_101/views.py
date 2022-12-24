from http.client import HTTPResponse

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from json import loads

from temp_101.forms import BlogForm
from temp_101.models import Blog


def index(request):
    return render(request, 'temp_101/index.html')


def blog_all(request):
    return JsonResponse([blog.serialize() for blog in Blog.objects.all()], safe=False)


def blog_create(request):
    blog_form = BlogForm(loads(request.body) or None)
    if request.method == 'POST' and blog_form.is_valid():
        blog_form.save()
        messages.success(request, 'blog created successfully!')
        return JsonResponse(blog_form.instance.serialize())
    return JsonResponse(blog_form.instance.serialize())


def blog_update(request):
    data = loads(request.body)
    blog = get_object_or_404(Blog, id=data['id'])
    blog_form = BlogForm(data, instance=blog)
    if request.method == 'PUT' and blog_form.is_valid():
        blog_form.save()
        messages.success(request, 'blog updated successfully!')
        return JsonResponse(blog_form.instance.serialize())


def blog_delete(request):
    blog = Blog.objects.get(id=loads(request.body)['id'])
    blog.delete()
    messages.success(request, 'blog deleted successfully!')
    return JsonResponse({'message': 'blog deleted successfully!'})


def blog_delete_all(request):
    inputs = loads(request.body)['id_list']
    Blog.objects.filter(id__in=inputs).delete()
    return JsonResponse({'message': 'blogs deleted successfully!'})