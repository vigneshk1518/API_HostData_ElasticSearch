from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.HostListView.as_view(), name=None),
    path('create/', views.HostCreateView.as_view(), name=None),
    path('<int:pk>/', views.HostDetailView.as_view(), name=None)
]