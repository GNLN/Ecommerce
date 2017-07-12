"""Return URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from  .import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9,a-z,\-]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^return_order/add/$', views.ReturnCreate.as_view(), name='add_return'),

    url(r'^return_items/$', views.return_statusView.as_view(), name='return_items'),

    url(r'^all_products/$',views.all_ProductsView.as_view(), name='product_items'),

    url(r'^(products/(?P<proid>[0-9,a-z,\-]+))/$', views.each_product, name='each_product'),

    url(r'^return_order/edit/(?P<pk>[0-9,a-z,\-]+)/$', views.ReturnUpdate.as_view(), name='update_return'),

    url(r'^return_order/delete/(?P<pk>[0-9,a-z,\-]+)/$', views.ReturnDelete.as_view(), name='delete_return'),

    url(r'^product_order/add/$', views.ProductCreate.as_view(), name='add_product'),

    url(r'^products_present/$', views.ProductView.as_view(), name="all_products"),

    url(r'^(product/detail/(?P<proid>[0-9,a-z,\-]+))/$', views.InventoryDetailView, name='each_product_info'),
]
