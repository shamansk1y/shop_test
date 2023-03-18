from django.shortcuts import render, redirect, get_object_or_404
from main_page.context_data import get_page_context
from main_page.forms import ContactUsForm, SubscriptionForm
from shop.models import Category


def handle_post_request(request):

    contact_us = ContactUsForm(request.POST)
    subscription = SubscriptionForm(request.POST)

    if contact_us.is_valid():
        contact_us.save()
        return redirect('/')
    if subscription.is_valid():
        subscription.save()
        return redirect('/')



def index(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'index.html', context=data)

def contacts(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'contact.html', context=data)


def category_list(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'category_list.html', context=data)


def sub_category_list(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    child = cat.children.all()
    context = {
        'cat': cat,
        'child': child,
    }
    return render(request, 'sub_category_list.html', context)