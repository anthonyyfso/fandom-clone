from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.pages_create, name='pages.create'),
    path('<slug:slug>/', views.page_detail, name='pages.detail'),
    path('', views.pages_list, name='pages.list'),
    path('<slug:page_slug>/edit/', views.pages_update, name='pages.edit'),
    path('search', views.PageSearch, name='pages.search'),
    path('details/create/<slug:page_slug>/', views.details_create, name='details.create'),
]
