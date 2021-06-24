"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('create-book/',views.CreateBookView.as_view(),name='create_book'),
    path('version-book/<pk>/',views.version_book,name='version_book'),
    path('version-book/<pk>/<pk_version>/',views.version_book,name='activate_version_book'),
    path('update-book/<pk>/',views.UpdateBookView.as_view(),name='update_book'),
    path('new-version/<pk>/',views.NewVersionBookView.as_view(),name='new_version'),
    path('item-list/<pk>/',views.ListItemView.as_view(),name='item_list'),
    path('create-item/<book_pk>/',views.CreateItemView.as_view(),name='create_item'),
    path('update-item/<pk>/<book_pk>/',views.UpdateItemView.as_view(),name='update_item')
]