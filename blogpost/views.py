from django.shortcuts import render, get_object_or_404
from blogpost.models import Blog

def blog_post_list(request):

    posts = Blog.objects.filter(is_visible=True).order_by('-pub_date')
    return render(request, 'post_list.html', {'posts': posts})

def blog_post_detail(request, slug):

    post = get_object_or_404(Blog, slug=slug, is_visible=True)
    return render(request, 'post_detail.html', {'post': post})

