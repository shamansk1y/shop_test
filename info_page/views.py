from django.shortcuts import render, get_object_or_404
from main_page.context_data import get_common_context
from .models import InfoPage


def info_page(request, slug):
    page = get_object_or_404(InfoPage, slug=slug)
    data = {
        'page': page
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'info_page.html', context=data)