from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.MainPage, name='mainpage'),
    url(r'^grid/$', views.ProductListView.as_view(), name='grid'),
    url(r'^index/$', views.index, name='grid'),
    url(r'^product/(?P<pk>[-\w]+)/$', views.ProductDetailView.as_view(), name='product-detail'),
    url(r'^product/edit/(?P<pk>[-\w]+)/$', views.ProductEditView, name='product-edit'),
    url(r'^product/image/remove/(?P<pk>[-\w]+)/(?P<prod_id>[-\w]+)/$', views.image_remove, name='image_remove'),
    url(r'^404/$', views.page404),
]

# url(r'^$', views.index, name='index'),
# url(r'^/$', views.ProductListView.as_view(), name='index'),
# url(r'^login/$', views.user_login, name='user_login')

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#https://green-point.ru/products/category/eco-bio-products