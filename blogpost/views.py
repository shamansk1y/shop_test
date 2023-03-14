from django.shortcuts import render, get_object_or_404
from blogpost.models import Blog
from main_page.context_data import get_common_context


def blog_post_list(request):

    posts = Blog.objects.filter(is_visible=True).order_by('-pub_date')
    data = {
        'posts': posts
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'post_list.html', context=data)

def blog_post_detail(request, slug):

    post = get_object_or_404(Blog, slug=slug, is_visible=True)
    data = {
        'post': post
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'post_detail.html', context=data)
