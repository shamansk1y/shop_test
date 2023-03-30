from django.urls import path
from account.views import add_to_favorite, remove_from_favorite, favorite_list, remove_from_favorite_detail

urlpatterns = [
    path('add/<slug:slug>/', add_to_favorite, name='add_to_favorite'),
    path('remove/<slug:slug>/', remove_from_favorite, name='remove_from_favorite'),
    path('remove-detail/<slug:slug>/', remove_from_favorite_detail, name='remove_from_favorite_detail'),
    path('', favorite_list, name='favorite_list'),
]