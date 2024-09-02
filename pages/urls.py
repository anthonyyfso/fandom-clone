from django.urls import path
from . import views
from .views import page_detail, PageSearch

urlpatterns = [
    path('create/', views.PagesCreateView.as_view(), name='pages.create'),
    path('<slug:slug>/', views.page_detail, name='pages.detail'),
    path('', views.PagesListView.as_view(), name='pages.list'),
    path('<slug:slug>/edit/', views.PagesUpdateView.as_view(), name='pages.edit'),
    path('search', views.PageSearch, name='pages.search'),
    path('<slug:slug>/details/edit/', views.DetailsCreateView.as_view(), name='details.edit'),
]