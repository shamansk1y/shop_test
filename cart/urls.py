from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('add_quantity/<int:product_id>/<str:size>/', views.cart_add_quantity, name='cart_add_quantity'),
    path('sub/<int:product_id>/<str:size>/', views.cart_sub, name='cart_sub'),
    path('remove/<int:product_id>/<str:size>/', views.cart_remove, name='cart_remove'),

]
