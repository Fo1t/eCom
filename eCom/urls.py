"""eCom URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls import url, handler400, handler403, handler404, handler500
from . import views
from eCom import settings

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),  # admin site
    path('accounts/', include('django.contrib.auth.urls')),
    path('orders/', include(('orders.urls', 'order_create'), namespace='order_create')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
    path('account/', include('account.urls')),
    path('', RedirectView.as_view(url='/shop/', permanent=True)),
    path('Orders/', include('orders.urls')),
    path('fix/', views.FixPage)
]

handler404 = views.page_not_found


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)