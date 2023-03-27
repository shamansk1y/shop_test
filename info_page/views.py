from django.shortcuts import render, get_object_or_404
from main_page.context_data import get_common_context, get_page_context
from .models import InfoPage


def info_page(request, slug):
    page = get_object_or_404(InfoPage, slug=slug)
    data = {
        'page': page
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'info_page.html', context=data)