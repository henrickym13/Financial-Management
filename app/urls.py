from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('', include('category.urls')),
    path('', include('user.urls')),
    path('', include('transaction.urls')),
]
