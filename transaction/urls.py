from django.urls import path
from . import views


urlpatterns = [
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.transaction_add, name='transaction_add'),
    path('transactions/edit/<int:pk>/', views.transaction_edit, name='transaction_edit'),
    path('transaction/delete/<int:pk>/', views.transaction_delete, name='transaction_delete'),
    path('monthly-summary/', views.monthly_summary, name='monthly_summary'),
    path('monthly-history/<int:year>/<int:month>/', views.monthly_history, name='monthly_history')
]