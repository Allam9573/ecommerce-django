"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views
from admin_user.views import admin_add_product
from admin_user.views import save_product
from admin_user.views import create_form_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add-product/', admin_add_product, name='add_product'),
    path('save/', save_product, name='save_product'),
    path('form/', create_form_article, name='create_form_article')
]
