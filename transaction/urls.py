from django.urls import path
from . import views


urlpatterns = [
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.transaction_add, name='transaction_add'),
    path('transactions/edit/<int:pk>/', views.transaction_edit, name='transaction_edit'),
    path('transaction/delete/<int:pk>/', views.transaction_delete, name='transaction_delete'),
]