"""my_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from account.views import logout_view, login_view, registration_view
from info_page.views import info_page
from orders.views import order_history

urlpatterns = [
    path('', include('main_page.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('blog/', include('blogpost.urls', namespace='blog')),
    path('logout/', logout_view, name='logout_view'),
    path('login/', login_view, name='login_view'),
    path('registration/', registration_view, name='registration_view'),
    path('order_history/', order_history, name='order_history'),
    path('favorite/', include('account.urls')),
    path('<slug:slug>/', info_page, name='info_page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)