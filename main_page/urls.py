from django.urls import path
from .views import index, contacts, sub_category_list

app_name = 'main_page'



urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category/', sub_category_list, name='sub_category_list'),
]