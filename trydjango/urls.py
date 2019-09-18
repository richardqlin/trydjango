"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from pages import views

from pages.views import home_view, contact_view,about_view,social_view


urlpatterns = [

	path('blog/', include('blog.urls')),

	path('products/' , include('products.urls')),
	path('contact/',contact_view),
	path('about/<int:id>',about_view,name ='product-detail'),

	path('',home_view,name='home'),

	path('social/',social_view),
    path('admin/', admin.site.urls),
]


